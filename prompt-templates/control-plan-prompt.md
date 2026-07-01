# Prompt Template: AI-Generated Control Plan

**Phase:** Control  
**Tool:** ChatGPT / Copilot / Gemini  
**Time to output:** 10 minutes

---

## Copy-Paste Prompt

```
I have completed my Lean Six Sigma Improve phase and implemented the solution. I now need to create a Control Plan to sustain the improvement.

Project summary:
- Process: [REPLACE: describe your process]
- Problem solved: [REPLACE: what defect or issue was fixed]
- Solution implemented: [REPLACE: describe what was changed or introduced]
- Key metrics to monitor: [REPLACE: list 3-5 KPIs you are now tracking]
- Target performance: [REPLACE: e.g. defect rate less than 3%]
- Process owner: [REPLACE: name or role of the person now responsible]
- Team responsible: [REPLACE: who will monitor and react]

Please generate a complete Control Plan with these columns:
1. Process Step - which step in the process needs controlling
2. What to Control - specific characteristic or metric
3. Control Method - how it will be monitored (SPC chart, dashboard, audit, etc.)
4. Measurement Frequency - how often (real-time, daily, weekly, monthly)
5. Who is Responsible - role title
6. Reaction Plan - exactly what to do if out of control (step-by-step)
7. Target / Specification - the performance standard
8. Escalation Path - who to involve if the reaction plan does not resolve it

Also include:
- A 90-day review schedule (what to review at 30, 60, and 90 days)
- 3 leading indicators that would signal the improvement is at risk BEFORE defects increase
- A process for updating the control plan if the process changes
```

---

## Follow-Up Prompts

**To create the monitoring alert logic:**
```
For the control plan above, write the alert conditions for [specific metric]. Use Western Electric rules (Rule 1: 1 point beyond UCL/LCL, Rule 2: 8 consecutive points same side of mean, Rule 3: 6-point trend). Format as: Trigger condition | Alert message | Who is notified | Response time.
```

**To create the handover document:**
```
Please draft a 1-page project handover summary for the process owner. Include: what was the problem, what was changed, what results were achieved, what they need to monitor going forward, and who to contact if issues arise.
```

---

## Usage Tips

- The Reaction Plan (column 6) is the most important column - be specific, not vague
- Bad reaction plan: "Investigate and fix"
- Good reaction plan: "1. Flag to team lead within 1 hour. 2. Pull last 10 transactions and identify common factor. 3. If training issue: retrain within 24 hours. 4. If system issue: raise IT ticket P2. 5. Review at next daily standup."
- Review the control plan at 30, 60, and 90 days post-implementation
- Pair with the SPC chart script for automated monitoring: see /scripts/spc_chart.py

---

*Part of the AI + Lean Six Sigma DMAIC Playbook | [Back to Chapter 5](../chapters/05-control.md)*
