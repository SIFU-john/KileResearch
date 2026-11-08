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
