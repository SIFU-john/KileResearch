# Results log: Part NN, [Article title]

*Kile Research · Beginner's Guide to Inference*

Copy this file to `results/NN-short-name.md` and fill it in while you run the experiment. Paste raw output exactly as printed. Don't round or tidy it. Before committing, remove secrets, tokens, local absolute paths, hostnames and personal data.

## Run info

| Field | Value |
|---|---|
| Date (UTC) | YYYY-MM-DD |
| Article | [articles/NN-short-name.md](../articles/NN-short-name.md) |
| Script(s) | [scripts/script_name.py](../scripts/script_name.py) |
| Git commit | `abc1234` |

## Hardware

| Field | Value |
|---|---|
| CPU | e.g. Intel Core i9-8950HK (6 cores / 12 threads) |
| GPU | e.g. none (CPU only) |
| RAM | e.g. 16 GB |
| OS | e.g. macOS 15.x |
| Power state | e.g. plugged in, other apps closed |

## Software versions

| Software | Version | How checked |
|---|---|---|
| Ollama | e.g. 0.40.11 | `ollama --version` |
| Python | e.g. 3.12.x | `python3 --version` |
| Model(s) | e.g. `qwen2.5:0.5b` (digest `abc123...`) | `ollama list` |
| Other | | |

## Settings

- Prompt: `...`
- Options: e.g. `temperature=0`, `num_predict=200`, `num_ctx=2048`
- Runs per configuration: e.g. 3 (first run cold, then warm)
- Anything else that could affect results:

## Raw output

### Configuration A: [name]

```
[paste exact output]
```

### Configuration B: [name]

```
[paste exact output]
```

## Summary table

| Configuration | Metric 1 | Metric 2 | Notes |
|---|---|---|---|
| A | | | |
| B | | | |

Report medians where there are several runs, and say which runs were cold.

## Observations

- **Measured:** [what the numbers show]
- **Surprises or anomalies:** [anything unexpected, failed runs, retries]
- **Interpretation (ours):** [clearly labeled]

## Untested or not reproduced

- [Anything mentioned in the article that wasn't run here, labeled **untested**]
