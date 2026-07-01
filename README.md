# AI + Lean Six Sigma DMAIC Playbook

> **Built for ops professionals, Green Belts, and consulting teams in Ireland and beyond.**

[![Public](https://img.shields.io/badge/Access-Public-brightgreen)](https://github.com/vasanthakumarkm/ai-lean-playbook)
[![DMAIC](https://img.shields.io/badge/Framework-DMAIC-blue)]()
[![AI Tools](https://img.shields.io/badge/Tools-ChatGPT%20%7C%20Copilot%20%7C%20Gemini-orange)]()

---

## Why AI + Lean Six Sigma — and Why Now?

For decades, DMAIC project initiation alone could take 2 weeks: scoping meetings, charter drafts, SIPOC workshops, VOC analysis. In 2026, that timeline is collapsing.

AI tools (ChatGPT, Microsoft Copilot, Gemini) don't replace the rigour of Lean Six Sigma — they eliminate the repetitive, time-consuming setup work, so practitioners can focus on what actually matters: root cause thinking, stakeholder buy-in, and sustainable control.

Most candidates either know Lean Six Sigma **or** AI. This playbook bridges both.

**This playbook demonstrates how AI-augmented initiation can cut project start-up from 2 weeks to 3 days — using a sample NVA Elimination scenario in a customer operations environment.**

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

Reusable `.md` prompt files are stored in [/prompt-templates](prompt-templates/):
- [`project-charter-prompt.md`](prompt-templates/project-charter-prompt.md)
- [`fishbone-prompt.md`](prompt-templates/fishbone-prompt.md)
- [`5-whys-prompt.md`](prompt-templates/5-whys-prompt.md)
- [`control-plan-prompt.md`](prompt-templates/control-plan-prompt.md)
- [`solution-scoring-prompt.md`](prompt-templates/solution-scoring-prompt.md)

---

## Automation Script

A Python SPC Control Chart Generator is available in [`/scripts`](scripts/). It reads sample process data and generates control charts with UCL/LCL boundaries.

> All project examples and data in this playbook are **sample scenarios** created for demonstration purposes.

---

## Who This Is For

- Operations professionals and Green/Black Belts looking to accelerate DMAIC delivery
- Consulting teams preparing AI-enabled transformation proposals
- Anyone bridging process excellence and AI tool adoption

---

## License

Open access. Fork it, adapt it, use it.
