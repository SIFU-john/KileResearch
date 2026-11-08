# Run Your First AI Model on Your Own Laptop (in 10 Minutes)

*Kile Research · Beginner's Guide to Inference, Week 1 · Part 1 of 4 · ~6 min read*

---

When you type a question into ChatGPT, your words go to a data center. A big computer runs a model on them and sends the answer back. That step, where a trained model runs and makes an answer, is called **inference**.

Inference doesn't need a data center. Small models run fine on a normal laptop with no GPU, no cloud account and no cost.

Today you'll download a model, chat with it, and call it from code. Everything else in this series builds on this setup.

## What you need

- A Mac, Windows or Linux computer with **at least 8 GB of RAM**
- About **1 GB of free disk space**
- 10 minutes

You don't need a GPU. We tested every step below on an older Intel laptop that has no GPU at all.

---

## Step 1: Install Ollama

**Ollama** is a free tool that downloads AI models and runs them for you. It handles the hard parts in the background.

- **Mac / Windows:** download the installer from [ollama.com/download](https://ollama.com/download) and run it.
- **Linux:** run this in a terminal:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

Check that it worked:

```bash
ollama --version
```

✅ **You should see** a version number, for example `ollama version is 0.x.x`.

> **Stuck?** If you see "command not found", close your terminal and open a new one. On Mac/Windows, make sure the Ollama app is running (look for the llama icon in your menu bar or system tray).

---

## Step 2: Download a small model

We'll use **Qwen 2.5 (0.5B)**. "0.5B" means it has about half a billion **parameters**, the numbers the model learned during training. That's tiny next to the big chatbots, so it downloads quickly and runs on almost any machine.

```bash
ollama pull qwen2.5:0.5b
```

✅ **You should see** a progress bar and then `success`. The download is about 400 MB.

---

## Step 3: Chat with it

```bash
ollama run qwen2.5:0.5b
```

You'll get a `>>>` prompt. Ask it something:

```
>>> What is the capital of Australia? Answer in one short sentence.
The capital of Australia is Canberra.
```

Type `/bye` to exit.

🎉 You just ran AI inference on your own hardware, and nothing left your computer.

> **Heads-up:** a 0.5B model is small. It's good for simple questions and it does get things wrong. That's expected. Later in this series you'll see how size and speed trade off.

---

## Step 4: Call the model from code

Chatting is fun, but real apps talk to models through an **API**. While Ollama runs, it serves one on your machine at `http://localhost:11434`.

Try it with `curl`:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:0.5b",
  "prompt": "Give me one fun fact about octopuses.",
  "stream": false
}'
```

✅ **You should see** a block of JSON. Look for the `"response"` field, which holds the model's answer.

Here's the same call in Python, using only the standard library (nothing to install):

```python
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
```

Run it:

```bash
python3 hello_llm.py
```

---

## What just happened?

Here's what happens when you send a prompt:

1. **Load.** Ollama reads the model file from disk into memory (RAM).
2. **Read the prompt.** The model processes your whole prompt at once.
3. **Generate.** The model predicts the answer **one small piece at a time**. Each new piece is added to the text, and then it predicts the next one.

Step 3 is why answers appear word by word in chat apps. It isn't a visual effect. The model really does produce one piece at a time.

Those "pieces" are called **tokens**, and they're the topic of Part 2.

---

## Recap

| You did | Why it matters |
|---|---|
| Installed Ollama | You now have your own local "inference server" |
| Pulled a 0.5B model | Small models are fast, free and private |
| Chatted in the terminal | You saw inference happen live |
| Called the API from Python | This is how real apps use models |

## Try this (optional)

- Pull a slightly bigger model, `ollama pull gemma3:1b`, and ask both models the same question. Which answer is better? Which one is faster?
- Run `ollama list` to see all the models you've downloaded.

**Next up, Part 2:** *Tokens: The Hidden Unit That Controls AI Cost and Speed.* You'll write a 20-line script that shows how a model actually "sees" your text.

*If this helped, follow along. One small, hands-on step at a time.*
