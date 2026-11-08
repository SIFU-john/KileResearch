# Quantization: How to Make a Model 2× Faster by "Rounding" It

*Kile Research · Beginner's Guide to Inference, Week 1 · Part 4 of 4 · ~7 min read*

---

In Part 3 we found the core rule of inference speed: **every token means reading all of the model's numbers from memory.**

So here's a simple idea: **what if each number took up less space?**

That idea is called **quantization**. It's why you can run AI on a laptop at all. Today you'll run the *same* model at three precision levels and measure the difference yourself.

## What you need

- Ollama + the benchmark script from [Part 3](03-measure-inference-speed.md)
- About 1.5 GB of free disk space for two extra model versions

---

## Step 1: Understand quantization in 60 seconds

A model is billions of numbers (parameters). How precisely you store each one is the choice:

| Format | Bits per number | Analogy |
|---|---|---|
| **FP16** | 16 | Price written as $4.1372 |
| **Q8** (8-bit) | ~8 | Price written as $4.14 |
| **Q4** (4-bit) | ~4–5 | Price written as "about $4" |

Fewer bits mean:

- 📦 **Smaller files**, so less disk space and less RAM
- ⚡ **Faster generation**, so less data to move for every token
- 🎯 **Slightly less accuracy**, because some detail gets rounded away

The surprise is how little accuracy you usually lose at 8-bit, and often at 4-bit too.

---

## Step 2: Download the same model at three precisions

The `qwen2.5:0.5b` you've been using is **already quantized to 4-bit**. Check:

```bash
ollama show qwen2.5:0.5b
```

✅ **You should see** `quantization    Q4_K_M`.

> `Q4_K_M` is a popular 4-bit method. The "K_M" part is a detail of how it rounds. Treat it as "good-quality 4-bit."

Now pull the 8-bit and 16-bit versions of the **same** model:

```bash
ollama pull qwen2.5:0.5b-instruct-q8_0
ollama pull qwen2.5:0.5b-instruct-fp16
```

Most models in the Ollama library offer these variants. Open a model's page on [ollama.com/library](https://ollama.com/library) and click **Tags** to see them.

---

## Step 3: Compare file sizes

```bash
ollama list
```

✅ **You should see** something like:

```
NAME                          SIZE
qwen2.5:0.5b-instruct-fp16    994 MB
qwen2.5:0.5b-instruct-q8_0    531 MB
qwen2.5:0.5b                  397 MB
```

Same model, same knowledge, and the 4-bit version is **60% smaller**.

---

## Step 4: Benchmark all three

Use `benchmark.py` from Part 3. Run each version and look at the warm runs (runs 2 and 3):

```bash
python3 benchmark.py qwen2.5:0.5b
python3 benchmark.py qwen2.5:0.5b-instruct-q8_0
python3 benchmark.py qwen2.5:0.5b-instruct-fp16
```

Then check memory use while a model is loaded:

```bash
ollama ps
```

✅ **Our results** (Intel laptop, CPU only):

| Version | Disk | RAM when loaded | Speed (tok/s) |
|---|---|---|---|
| FP16 | 994 MB | 1.1 GB | ~24 |
| Q8 | 531 MB | 619 MB | ~47 |
| **Q4_K_M** | **397 MB** | **486 MB** | **~57** |

Going from FP16 to Q8 **about doubled the speed**. That fits the Part 3 rule: half the bytes means half the data to move.

Q8 → Q4 gave a smaller boost. At that size, other parts of the computer start to limit speed too. Your exact numbers will vary, but the pattern should hold.

---

## Step 5: Check the quality

Speed is no use if the answers get worse. Ask all three the same question:

```bash
ollama run qwen2.5:0.5b "What is the capital of Australia? Answer in one short sentence."
ollama run qwen2.5:0.5b-instruct-q8_0 "What is the capital of Australia? Answer in one short sentence."
ollama run qwen2.5:0.5b-instruct-fp16 "What is the capital of Australia? Answer in one short sentence."
```

✅ **On our test machine, all three said:** `The capital of Australia is Canberra.`

For simple tasks, you usually can't tell them apart. Differences tend to show up on **harder tasks** like math, long reasoning and exact facts. Try a few questions from your own work and judge for yourself. That's how professionals decide too.

> **Honest caveat:** one question isn't a real quality test. Proper evaluation uses hundreds of test questions. A future article will show you how to set up a mini evaluation.

---

## Step 6: Choose a precision (cheat sheet)

| Your situation | Pick |
|---|---|
| Laptop, limited RAM, you want speed | **Q4_K_M** (Ollama's usual default) |
| You have spare memory and want closer-to-original quality | **Q8** |
| Research or comparisons, plenty of memory | **FP16** |
| Choosing between a bigger model at Q4 and a smaller one at FP16 | Usually the **bigger model at Q4** |

That last row is the key insight. **A 7B model at 4-bit usually beats a 3B model at 16-bit**, and often uses about the same memory.

---

## Clean up (optional)

Free the disk space when you're done:

```bash
ollama rm qwen2.5:0.5b-instruct-fp16
ollama rm qwen2.5:0.5b-instruct-q8_0
```

---

## Week 1 recap: what you can do now

Over four short articles you have:

1. ✅ Run a model locally and called it from code
2. ✅ Seen how models split text into **tokens**
3. ✅ Measured **TTFT**, **tokens/second** and **cold starts**
4. ✅ Used **quantization** to make a model about 2× faster at the same quality

That's the foundation of inference engineering: **measure, understand the bottleneck, then make a trade-off.**

**Coming in Week 2:** what a **GPU** actually does for inference, why the **KV cache** makes long chats slower, and how to serve a model to several users at once.

*Follow along for Week 2. And if you ran the benchmark, share your Q4 vs FP16 numbers in the comments.*
