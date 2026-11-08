# How Fast Is Your AI, Really? Measure It in 5 Minutes

*Kile Research · Beginner's Guide to Inference, Week 1 · Part 3 of 4 · ~7 min read*

---

"It feels slow" isn't something you can fix. Inference engineers use **numbers**, and two of them matter most:

| Metric | What it means | What it feels like |
|---|---|---|
| **TTFT** (Time To First Token) | How long until the first word appears | "Is it thinking or frozen?" |
| **Tokens per second** (tok/s) | How fast the rest of the answer streams | "Is it typing fast or crawling?" |

Today you'll build a small benchmark that measures both. Then you'll find a hidden third number that surprises almost everyone.

## What you need

- Ollama with `qwen2.5:0.5b` ([Part 1](01-run-your-first-llm-locally.md))
- Optional: `gemma3:1b` for comparison (`ollama pull gemma3:1b`)
- Python 3, nothing to install

---

## Step 1: Understand the two phases

From Part 1, every request has two phases:

1. **Prefill:** the model reads your whole prompt at once. This phase sets **TTFT**.
2. **Decode:** the model generates the answer one token at a time. This phase sets **tokens/second**.

So we'll start a timer, wait for the first token, then count how fast the rest arrive.

---

## Step 2: Create the benchmark script

Save this as `benchmark.py`:

```python
"""Measure time-to-first-token (TTFT) and tokens/second for a local Ollama model."""
import json
import sys
import time
import urllib.request

MODEL = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5:0.5b"
PROMPT = "Explain what a GPU does in exactly three sentences."
RUNS = 3


def run_once(model: str, prompt: str) -> dict:
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {"temperature": 0, "num_predict": 200},
    }).encode()
    req = urllib.request.Request("http://localhost:11434/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    start = time.perf_counter()
    ttft = None
    with urllib.request.urlopen(req) as resp:
        for line in resp:  # Ollama streams one JSON object per line
            chunk = json.loads(line)
            if ttft is None and chunk.get("response"):
                ttft = time.perf_counter() - start
            if chunk.get("done"):
                final = chunk
    total = time.perf_counter() - start
    return {
        "ttft_s": ttft,
        "total_s": total,
        "output_tokens": final["eval_count"],
        # eval_duration is reported in nanoseconds
        "tokens_per_s": final["eval_count"] / (final["eval_duration"] / 1e9),
        "load_s": final.get("load_duration", 0) / 1e9,
    }


print(f"Model: {MODEL}")
print(f"{'run':>3} | {'load (s)':>8} | {'TTFT (s)':>8} | {'tokens':>6} | {'tok/s':>7} | {'total (s)':>9}")
for i in range(1, RUNS + 1):
    r = run_once(MODEL, PROMPT)
    print(f"{i:>3} | {r['load_s']:>8.2f} | {r['ttft_s']:>8.3f} | {r['output_tokens']:>6} | "
          f"{r['tokens_per_s']:>7.1f} | {r['total_s']:>9.2f}")
```

**Key ideas in the code:**

- `"stream": True` makes Ollama send tokens as they're made, so we can time the first one.
- `temperature: 0` makes answers repeatable, which gives a fairer test.
- `num_predict: 200` caps the answer length so one run can't go on forever.
- Ollama's final message reports `eval_count` (tokens generated) and `eval_duration` (how long that took). We divide them to get tok/s.

---

## Step 3: Start "cold"

Unload the model from memory first, so the first run starts from scratch:

```bash
ollama stop qwen2.5:0.5b
```

---

## Step 4: Run the benchmark

```bash
python3 benchmark.py
```

✅ **You should see** something like this (our older Intel test laptop, CPU only, no GPU):

```
Model: qwen2.5:0.5b
run | load (s) | TTFT (s) | tokens |   tok/s | total (s)
  1 |     1.61 |    1.970 |    105 |    54.1 |      3.91
  2 |     0.00 |    0.024 |     94 |    55.5 |      1.72
  3 |     0.00 |    0.024 |     94 |    56.8 |      1.68
```

Your numbers will be different. Faster machines, especially Apple Silicon Macs or PCs with a GPU, will often be several times quicker.

> **Why did run 1 give 105 tokens and runs 2–3 give 94?** Even at temperature 0, the very first run can come out slightly different. The tok/s figure stays fair because it divides by the actual token count.

---

## Step 5: Read the results (the surprise)

Look at **run 1 against runs 2 and 3**:

- Run 1 TTFT: **~2 seconds**
- Runs 2–3 TTFT: **~0.02 seconds**. That's about **80 times faster**.

Why? Look at the `load` column. On run 1, Ollama spent 1.6 seconds **loading the model from disk into memory**. After that, the model stays loaded (for 5 minutes by default), so later requests skip that step.

That's the hidden third number: the **cold start**. In real products, this is often the biggest delay users notice. That's why production systems keep models "warm" in memory.

Notice also that **tok/s barely changed** (54 → 57). Loading only affects the start. Once generation begins, speed depends on your hardware and the model.

---

## Step 6: Compare two models

```bash
ollama stop gemma3:1b
python3 benchmark.py gemma3:1b
```

Our results:

| Model | Parameters | Warm TTFT | tok/s |
|---|---|---|---|
| qwen2.5:0.5b | 0.5 B | 0.02 s | ~56 |
| gemma3:1b | 1 B | ~0.1 s | ~25 |

**About twice the parameters gave about half the speed.** For every token, the model has to read all of its parameters from memory. More parameters means more data to move, which means fewer tokens per second.

That one idea, **"speed is mostly about moving numbers through memory,"** is the core of inference engineering.

---

## Recap

- **TTFT** = time until the first token; it's mostly the prefill phase, plus loading on a cold start.
- **Tokens/second** = generation speed during decode.
- **Cold starts** (loading the model) can be much slower than everything else. Keep models warm.
- Bigger models are slower because each token needs more data moved through memory.

## Try this (optional)

- Make `PROMPT` 10× longer (paste a few paragraphs). Watch TTFT go up while tok/s stays about the same. That's prefill doing more work.
- Set `num_predict` to `50`, then `500`. Does tok/s change? (It shouldn't change much.)

**Next up, Part 4:** *Quantization: How to Make a Model 2× Faster by "Rounding" It.* If speed comes down to moving numbers through memory, what happens if we make the numbers smaller?

*Post your tok/s results and your hardware in the comments. We'd love to see the spread.*
