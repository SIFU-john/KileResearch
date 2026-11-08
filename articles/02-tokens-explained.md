# Tokens: The Hidden Unit That Controls AI Cost and Speed

*Kile Research · Beginner's Guide to Inference, Week 1 · Part 2 of 4 · ~6 min read*

---

AI models don't read words. They read **tokens**.

A token is a chunk of text. Sometimes it's a whole word, sometimes part of a word, sometimes a single character. Almost everything in AI is counted in tokens:

- 💰 **Cost:** API providers charge per token.
- ⚡ **Speed:** models generate a set number of tokens per second.
- 📏 **Limits:** a model can only "remember" so many tokens at once.

Today you'll see real tokens for yourself.

## What you need

- Ollama and the `qwen2.5:0.5b` model from [Part 1](01-run-your-first-llm-locally.md)
- Python 3 (nothing extra to install)

---

## Step 1: Make sure Ollama is running

```bash
ollama list
```

✅ **You should see** `qwen2.5:0.5b` in the list. If not, run `ollama pull qwen2.5:0.5b`.

---

## Step 2: Create the token counter

Save this as `count_tokens.py`:

```python
"""Count how many tokens a model sees for a piece of text (uses the local Ollama API)."""
import json
import sys
import urllib.request

MODEL = "qwen2.5:0.5b"


def count_tokens(text: str) -> int:
    body = json.dumps({
        "model": MODEL,
        "prompt": text,
        "raw": True,            # skip the chat template so we count only our text
        "stream": False,
        "options": {"num_predict": 1},  # we only care about the input, generate 1 token
    }).encode()
    req = urllib.request.Request("http://localhost:11434/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["prompt_eval_count"]


samples = sys.argv[1:] or [
    "Hello",
    "Hello world",
    "Inference engineering",
    "antidisestablishmentarianism",
    "Bonjour tout le monde",
    "12345678901234567890",
    "🙂🙂🙂",
]

for text in samples:
    n = count_tokens(text)
    print(f"{n:>3} tokens | {len(text):>3} chars | {text}")
```

**How it works:** we send text to the model and ask it to generate just 1 token. Ollama replies with `prompt_eval_count`, which is how many tokens it read from our input. Setting `"raw": True` stops Ollama from adding its own hidden chat formatting, so we count only our text.

---

## Step 3: Run it

```bash
python3 count_tokens.py
```

✅ **You should see** something like this (from our test machine):

```
  1 tokens |   5 chars | Hello
  2 tokens |  11 chars | Hello world
  3 tokens |  21 chars | Inference engineering
  6 tokens |  28 chars | antidisestablishmentarianism
  4 tokens |  21 chars | Bonjour tout le monde
 20 tokens |  20 chars | 12345678901234567890
  3 tokens |   3 chars | 🙂🙂🙂
```

Try your own text too:

```bash
python3 count_tokens.py "Your sentence here" "Another one"
```

---

## Step 4: Read the results

Three patterns stand out:

**1. Common words are cheap.** "Hello" is one token. The model saw it so often in training that it got its own token.

**2. Rare words get split.** "antidisestablishmentarianism" became 6 pieces. The model builds rare words out of smaller chunks it already knows.

**3. Numbers can be expensive.** This model splits numbers into single digits, so 20 digits became 20 tokens. This is one reason small models struggle with arithmetic: they see numbers as a string of separate digits.

> **Rule of thumb:** for English, 1 token ≈ ¾ of a word, or about 4 characters. 1,000 tokens ≈ 750 words. Other languages, code and numbers usually take more tokens.

> **Note:** each model has its own tokenizer, so the same text can give different counts on different models. Try changing `MODEL` to `gemma3:1b` and compare.

---

## Step 5: Find your model's memory limit (the context window)

Every model has a **context window**: the most tokens it can handle at once, counting your prompt *and* its answer together. Check yours:

```bash
ollama show qwen2.5:0.5b
```

✅ **You should see** a line like:

```
context length      32768
```

So this model *can* handle about 32,000 tokens, which is roughly 24,000 words.

There's a catch. By default, Ollama only gives the model a smaller window (often **4,096 tokens**) to save memory. Run `ollama ps` while a model is loaded and check the `CONTEXT` column. If your prompt is longer than that, the oldest text gets dropped without any warning. If a chatbot seems to "forget" the start of a long conversation, this is usually why.

You can raise it per request by adding `"num_ctx"` to `options`:

```python
"options": {"num_ctx": 8192}
```

A bigger window uses more memory. There's a trade-off at every step.

---

## Why this matters

| When you hear... | Think... |
|---|---|
| "$3 per million tokens" | Cost depends on token count, not word count |
| "50 tokens per second" | About 37 words per second |
| "128K context window" | About 96,000 words of combined input and output |

## Recap

- Models read **tokens**, not words.
- Common words = 1 token; rare words and numbers = many tokens.
- The **context window** is the token limit for prompt + answer together.
- Ollama's default window may be smaller than the largest window the model supports.

**Next up, Part 3:** *How Fast Is Your AI, Really?* We'll measure the two speed numbers that matter, time-to-first-token and tokens per second, with a small benchmark script.

*If tokens finally clicked for you, follow along for Part 3.*
