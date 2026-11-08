# Kile Research

## Beginner's Guide to Inference

Hands-on, beginner-friendly guides to how AI models actually run. Each article teaches **one idea**, takes 5–10 minutes to follow, and ends with something you built and measured yourself.

The articles are published on Medium. This repo holds the article sources, runnable code, configs and raw results for every article, so you can reproduce what you read.

**Who it's for:** developers, IT and cloud folks, and curious learners with a beginner-to-intermediate grasp of AI.
**Cadence:** 4 articles per week (Mon / Tue / Thu / Fri).
**Where we're going:** from "I can run a model" to "I can build, evaluate and deploy a small AI service."

```
Week 1  Run it        → local model, tokens, speed, quantization
Week 2  Understand it → memory bandwidth, KV cache, batching, evals
Week 3  Build with it → embeddings, RAG, chunking, tool calling
Week 4  Deploy it     → Docker, OpenAI-compatible APIs, Kubernetes, production readiness
Week 5  Scale it      → transformer internals, serving engines, speculative decoding, benchmarking
```

**Status key:** ✅ Written (source in this repo) · 📝 Planned

---

## Week 1: Run it ✅

| # | Article | You walk away able to... | Code | Status |
|---|---|---|---|---|
| 1 | [Run Your First AI Model on Your Own Laptop](articles/01-run-your-first-llm-locally.md) | Run a local model and call it from Python | [`hello_llm.py`](scripts/hello_llm.py) | ✅ Written |
| 2 | [Tokens: The Hidden Unit That Controls AI Cost and Speed](articles/02-tokens-explained.md) | Count tokens and explain context windows | [`count_tokens.py`](scripts/count_tokens.py) | ✅ Written |
| 3 | [How Fast Is Your AI, Really?](articles/03-measure-inference-speed.md) | Benchmark TTFT, tok/s and cold starts | [`benchmark.py`](scripts/benchmark.py) | ✅ Written |
| 4 | [Quantization: Make a Model 2× Faster by "Rounding" It](articles/04-quantization-explained.md) | Pick a quantization level with data | [`benchmark.py`](scripts/benchmark.py) | ✅ Written |

Week 1 test rig: Ollama 0.40.11 · Intel Core i9-8950HK (CPU only, no GPU) · macOS · Python 3 standard library.

## Week 2: Understand it (Nov 9–13) 📝

| # | Date | Working title | Status |
|---|---|---|---|
| 5 | Mon 11/9 | Why AI Speed Is a Memory Problem, Not a Math Problem | 📝 Planned |
| 6 | Tue 11/10 | The KV Cache: Why Long Chats Get Slower | 📝 Planned |
| 7 | Thu 11/12 | One Model, Many Users: Batching Explained with a Load Test | 📝 Planned |
| 8 | Fri 11/13 | Your First AI Evaluation: Test Quality, Not Just Speed | 📝 Planned |

## Week 3: Build with it (Nov 16–20) 📝

| # | Date | Working title | Status |
|---|---|---|---|
| 9 | Mon 11/16 | Embeddings: How AI Turns Meaning into Numbers | 📝 Planned |
| 10 | Tue 11/17 | Build a RAG System in ~100 Lines of Python | 📝 Planned |
| 11 | Thu 11/19 | Why Your RAG Gives Wrong Answers: Chunking | 📝 Planned |
| 12 | Fri 11/20 | Tool Calling: Teaching a Model to Use Functions | 📝 Planned |

## Week 4: Deploy it (Nov 23–25) 📝

| # | Date | Working title | Status |
|---|---|---|---|
| 13 | Mon 11/23 | Put Your Model in a Container | 📝 Planned |
| 14 | Tue 11/24 | The OpenAI-Compatible API: Why Every AI Server Speaks One Language | 📝 Planned |
| 15 | Wed 11/25 | Your First Model on Kubernetes | 📝 Planned |
| 16 | Wed 11/25 | Production-Ready Inference: Health Checks, Timeouts and Warm-Up | 📝 Planned |

US Thanksgiving week: Parts 15 and 16 both go out on Wednesday.

## Week 5: Scale it (Nov 30 – Dec 4) 📝

| # | Date | Working title | Status |
|---|---|---|---|
| 17 | Mon 11/30 | Follow One Token Through a Transformer | 📝 Planned |
| 18 | Tue 12/1 | Ollama vs vLLM: What Serving Engines Actually Do Differently | 📝 Planned |
| 19 | Thu 12/3 | Speculative Decoding: Guess Fast, Check Once | 📝 Planned |
| 20 | Fri 12/4 | How to Benchmark AI Like a Researcher | 📝 Planned |

Titles for Weeks 2–5 are working titles and may change before publishing.

---

## Repo layout

```
articles/    article sources (Markdown), one file per part: NN-short-name.md
scripts/     runnable code for each article (Python standard library unless noted)
results/     raw benchmark outputs, with hardware and versions recorded
deploy/      Docker and Kubernetes files (Week 4)
templates/   article and results-log templates
STYLE.md     house style and Definition of Done for every article
```

## Run the code

Most scripts need only Python 3 and a local [Ollama](https://ollama.com) install:

```bash
git clone https://github.com/SIFU-john/KileResearch.git
cd KileResearch
ollama pull qwen2.5:0.5b
python3 scripts/hello_llm.py
```

Each article lists its exact prerequisites in a **What you need** section.

## Contributing your numbers

Ran a benchmark on your own machine? Open an issue with your hardware, versions and output. We'd love to compare numbers. Spotted a mistake? Issues and pull requests are welcome.

## License

Code and content are released under the [MIT License](LICENSE). © 2026 Kile Research.
