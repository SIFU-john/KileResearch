# hello_llm.py
import json
import urllib.request

body = json.dumps({
    "model": "qwen2.5:0.5b",
    "prompt": "Give me one fun fact about octopuses.",
    "stream": False,
}).encode()

req = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=body,
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as resp:
    print(json.load(resp)["response"])
