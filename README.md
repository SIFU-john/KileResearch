# Kile Research

## Inference for Humans

Hands-on, beginner-friendly guides to how AI models actually run. Each article teaches **one idea**, takes 5–10 minutes to follow, and ends with something you built and measured yourself.

The articles are published on Medium. This repo holds the runnable code, configs and raw results for every article, so you can reproduce what you read.

## Layout (coming soon)

```
articles/   article sources (Markdown)
scripts/    runnable code for each article
deploy/     Docker and Kubernetes files (Week 4)
results/    raw benchmark outputs, with hardware and versions recorded
```

## Series roadmap

| Week | Theme | Topics |
|---|---|---|
| 1 | Run it | Local models, tokens, measuring speed, quantization |
| 2 | Understand it | Memory bandwidth, KV cache, batching, evaluation |
| 3 | Build with it | Embeddings, RAG, chunking, tool calling |
| 4 | Deploy it | Docker, OpenAI-compatible APIs, Kubernetes, production readiness |
| 5 | Scale it | Transformer internals, serving engines, speculative decoding, benchmarking |

Most code uses only the Python standard library and a local [Ollama](https://ollama.com) install.

Questions or results from your own machine? Open an issue. We'd love to compare numbers.
