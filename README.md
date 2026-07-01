# AI + Lean Six Sigma DMAIC Playbook

> **Built for ops professionals, Green Belts, and consulting teams and beyond.**

[![Public](https://img.shields.io/badge/Access-Public-brightgreen)](https://github.com/vasanthakumarkm/ai-lean-playbook)
[![DMAIC](https://img.shields.io/badge/Framework-DMAIC-blue)]()
[![AI Tools](https://img.shields.io/badge/Tools-ChatGPT%20%7C%20Copilot%20%7C%20Gemini-orange)]()

---

## Why AI + Lean Six Sigma — and Why Now?

For decades, DMAIC project initiation alone could take 2 weeks: scoping meetings, charter drafts, SIPOC workshops, VOC analysis. In 2026, that timeline is collapsing.

AI tools (ChatGPT, Microsoft Copilot, Gemini) don't replace the rigour of Lean Six Sigma — they eliminate the repetitive, time-consuming setup work, so practitioners can focus on what actually matters: root cause thinking, stakeholder buy-in, and sustainable control.

Most candidates either know Lean Six Sigma **or** AI. This playbook bridges both.

**This playbook was inspired by my real project (NVA Elimination CX-ops-AMAZON ) where AI-augmented initiation could have cut project start-up from 2 weeks to 3 days.**

---

## What's Inside

| Chapter | AI Tool | Headline Output |
|---------|---------|----------------|
| [01 — Define](chapters/01-define.md) | ChatGPT | Auto-drafted Project Charter + SIPOC |
| [02 — Measure](chapters/02-measure.md) | Copilot + Excel | Baseline dashboard template |
| [03 — Analyse](chapters/03-analyse.md) | ChatGPT + Python | AI-generated Fishbone + 5 Whys |
| [04 — Improve](chapters/04-improve.md) | ChatGPT | Solution scoring matrix + change comms |
| [05 — Control](chapters/05-control.md) | Python | SPC control chart script |

---

## Prompt Templates

Reusable `.md` prompt files are stored in [`/prompt-templates`](prompt-templates/):

- [`project-charter-prompt.md`](prompt-templates/project-charter-prompt.md)
- [`fishbone-prompt.md`](prompt-templates/fishbone-prompt.md)
- [`5-whys-prompt.md`](prompt-templates/5-whys-prompt.md)
- [`control-plan-prompt.md`](prompt-templates/control-plan-prompt.md)
- [`solution-scoring-prompt.md`](prompt-templates/solution-scoring-prompt.md)

---

## Python Automation

The [`/scripts`](scripts/) folder contains:

- [`spc_chart.py`](scripts/spc_chart.py) — SPC Control Chart Generator: input a CSV of process measurements, output an X-bar chart with UCL/LCL lines, flagging out-of-control points.

---

## How to Use This Playbook

1. Navigate to the chapter matching your current DMAIC phase.
2. Copy the prompt template for the task you need.
3. Paste into ChatGPT / Copilot with your real process data.
4. Use the Python script to generate your SPC chart for the Control phase.

---

## Target Audience

- Operations Managers and Process Analysts
- Lean Six Sigma Green Belts and Black Belts
- Consulting teams in Ireland and the UK
- Anyone transitioning from manual DMAIC to AI-augmented continuous improvement

---

## About the Author

Built by a business transformation professional with hands-on DMAIC project experience in high-volume operations environments. This playbook reflects real project work, not theory.

---

*Star this repo if it's useful. Contributions and feedback welcome.*
