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
