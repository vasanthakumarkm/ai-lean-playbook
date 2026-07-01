# Prompt Template: AI-Structured 5 Whys Analysis

**Phase:** Analyse  
**Tool:** ChatGPT / Copilot / Gemini  
**Time to output:** 5 minutes

---

## Copy-Paste Prompt

```
Please help me run a structured 5 Whys root cause analysis.

Problem statement:
[REPLACE: Paste your verified problem statement from the Define phase here.]

Additional context:
- Process: [e.g. inbound catalogue classification]
- Industry: [e.g. warehouse operations]
- Data I have: [e.g. defect rate is 12%, spikes on Mondays, concentrated in 3 item categories]
- Constraints: [e.g. cannot change the ERP system, team of 15 operators]

For each Why iteration:
1. Provide the SHALLOW answer (what most people would say)
2. Provide the DEEP answer (the systemic cause beneath the obvious one)
3. Explain why the deep answer is more useful than the shallow one
4. Identify what evidence I would need to confirm this cause

After 5 iterations, provide:
- The verified root cause statement
- Whether it is a People, Process, System, or Policy issue
- Recommended corrective action type: Immediate fix OR Systemic change OR Both
- A brief explanation of why this root cause is better to solve than the surface symptoms

Important: Do not allow the analysis to stop at obvious answers. Push to the governance, policy, or systemic level.
```

---

## Before vs After Example

**Problem:** Catalogue items are misclassified at 12% defect rate

| Why # | Shallow Answer | Deep Answer (AI-guided) |
|-------|---------------|------------------------|
| Why 1 | Operators make mistakes | Classification rules are ambiguous for multi-category items |
| Why 2 | Operators are not trained | Training references an outdated rule set (version 2019) |
| Why 3 | Training was not updated | No owner is responsible for maintaining classification documentation |
| Why 4 | No ownership exists | Change management process excludes catalogue rule updates |
| Why 5 | - | No KPI exists to track classification accuracy at leadership level |

**Root Cause:** No governance owner for classification rules + no leadership KPI = systemic under-investment in process quality.

---

## Usage Tips

- If AI stops at a shallow answer, use: "Go deeper. What is the systemic reason for that?"
- Ask AI: "Is this a People issue or a System issue?" to push thinking
- Combine with Fishbone analysis: use Fishbone to generate hypotheses, 5 Whys to prove them
- The root cause should be something that, if fixed, prevents recurrence - not just fixes this instance

---

*Part of the AI + Lean Six Sigma DMAIC Playbook | [Back to Chapter 3](../chapters/03-analyse.md)*
