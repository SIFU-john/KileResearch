# Kile Research House Style

This guide applies to every article in the **Beginner's Guide to Inference** series. Start new articles from [`templates/article.md`](templates/article.md) and record experiments with [`templates/results-log.md`](templates/results-log.md).

## 1. Byline and series name

- Every article is credited to **Kile Research**. No individual author names appear in bylines, sign-offs or metadata.
- The series name is **Beginner's Guide to Inference**. Use it exactly as written, apostrophe included.
- The byline is the first line under the title, in this exact format:

  ```markdown
  *Kile Research · Beginner's Guide to Inference, Week N · Part P · ~M min read*
  ```

  `P` is the part number in the series (Week 1 also used "Part P of 4").
- Write in the first person plural: "we tested", "our test machine". Address the reader as "you".

## 2. Voice

- **Professional, curious, approachable.** Write like a knowledgeable colleague, not a textbook.
- **Simple, not simplistic.** Use plain words and short sentences, but don't trade accuracy for simplicity.
- **Define jargon the first time it appears**, in one plain sentence. Bold the term when you define it.
- **One idea per paragraph.** Keep paragraphs to about 2–4 sentences.
- **Analogies help, but label them.** Say when an analogy breaks down.
- **No hype.** Avoid "revolutionary", "game-changing", "blazing fast". Show the number instead.
- **Facts, measurements and opinions stay separate.** Use phrases like "the docs say", "we measured" and "our interpretation is".

## 3. Structure

Every article follows this arc. Adapt section names to the topic, but keep the order.

1. **Title**: specific and clear, no clickbait.
2. **The problem**: a relatable question or observation (2–4 short paragraphs).
3. **Why it matters**: why this affects real AI systems, cost or user experience.
4. **Concept explained**: the one idea, with a diagram, table or analogy.
5. **Hands-on**: "What you need", then numbered steps. Each step ends with a ✅ **You should see** check.
6. **Expected results**: real output from our test rig, with hardware stated, then what it means.
7. **Key takeaways**: 3–5 bullets.
8. **What's next**: a link or teaser to the next part, plus a community prompt (e.g. "post your numbers in the comments").

Also include a **Troubleshooting** section with at least two common failures and fixes, and a **References** section.

## 4. Code and commands

- Scripts live in [`scripts/`](scripts/) and use the Python standard library unless there's a stated reason.
- Keep code short and commented only where the reader needs it. Long code goes in the repo, not inline.
- Every command and every number in an article has actually been run on our test rig, and the raw output is saved in [`results/`](results/). Anything not run is labeled **untested**.
- Never commit secrets, API keys, tokens, local absolute paths (e.g. `/Users/...`) or personal data. Check before every push.

## 5. Medium formatting

- Medium has no native tables: export tables as images (with alt text) or link to the repo copy.
- Long code goes in a gist or a repo link. Keep inline snippets short.
- Every diagram gets alt text.
- Set the subtitle and up to 5 tags before publishing.
- Link each article to its folder or script in this repo.

## 6. Length

- 700–1,200 words, a 5–8 minute read. Optional labs and "Try this" sections can be extra.

## 7. Definition of Done (per article)

- [ ] One clearly stated learning objective
- [ ] 700–1,200 words, 5–8 min read (labs can be extra)
- [ ] "What you need" prerequisites up front
- [ ] Numbered steps, each with a ✅ *You should see* check
- [ ] Every command and number actually run and recorded (hardware stated). Anything untested is labeled **untested**
- [ ] Measured results, documented facts and our interpretation are kept clearly separate
- [ ] Jargon defined the first time it's used; at least one diagram or table where it helps
- [ ] Troubleshooting section (≥2 common failures)
- [ ] 3–5 key takeaways, a "What's next" link, and a community prompt
- [ ] At least 2 authoritative references
- [ ] Scripts committed to `scripts/`, stdlib-only unless justified
- [ ] Byline reads **Kile Research** (no individual author credits)
- [ ] Medium-ready: tables as images or repo links, long code in gists or the repo, diagrams as images with alt text, tags and subtitle set
- [ ] Series hub README updated

## 8. Production workflow

1. **Outline** (3 days before publishing): problem, single objective, experiment design, expected result.
2. **Run the experiment** on the test rig. Save raw output to `results/NN-short-name.md` using the results-log template.
3. **Draft** from `templates/article.md`.
4. **Verify**: rerun every command from a clean shell and check every claim against a primary source.
5. **Edit** against the Definition of Done and cut to length.
6. **Publish** on Medium after approval, then update the hub [`README.md`](README.md).

## 9. File naming

- Articles: `articles/NN-short-name.md` (two-digit part number, lowercase, hyphens).
- Results: `results/NN-short-name.md`, matching the article.
- Scripts: `scripts/descriptive_name.py` (snake_case).
- Deploy files: `deploy/docker/` and `deploy/k8s/`.
