# Prompt Template: AI-Generated Project Charter

**Phase:** Define  
**Tool:** ChatGPT / Copilot / Gemini  
**Time to output:** 60 seconds

---

## Copy-Paste Prompt

```
I need to create a Lean Six Sigma Project Charter. Here is the plain-English problem:

[REPLACE: Describe your problem in 2-3 sentences. Include: what is going wrong, where it is happening, and what the rough impact is.]

Context:
- Industry/function: [e.g. warehouse operations / financial services / retail]
- Process affected: [e.g. inbound classification / order fulfilment / invoicing]
- Rough scale: [e.g. 2,000 transactions per day / EUR 5M annual revenue impacted]
- Key stakeholder: [e.g. VP Operations / Finance Director]

Please generate a complete Project Charter with these sections:
1. Problem Statement (2-3 sentences, quantified where possible)
2. Project Goal (SMART format: Specific, Measurable, Achievable, Relevant, Time-bound)
3. Scope - In (what is included)
4. Scope - Out (what is excluded)
5. Business Impact (quantified in cost, time, or quality terms)
6. Project Sponsor (role title)
7. Project Team (suggested roles)
8. Timeline (suggested phases with durations)
9. Success Metrics (3-5 measurable KPIs)
10. Key Risks (top 3)
```

---

## Usage Tips

- Replace all text in `[REPLACE: ...]` brackets with your real information
- The more specific your input, the better the output
- Ask AI to revise specific sections: "Revise section 4 to exclude legacy systems"
- Use the output as a starting draft - validate figures with your team before sign-off

---

## Example Before/After

**Your input:**
```
Our warehouse catalogue classification process has a 12% defect rate, causing rework and customer complaints. This is happening in the FC operations team across 3 shifts. We estimate 30 minutes of rework per shift at EUR 25/hour.
```

**AI Charter (excerpt):**
```
Problem Statement: Incorrectly classified catalogue items are generating a 12% defect rate in FC operations, resulting in approximately 1.5 hours of daily rework (EUR 13,500 annual cost) and downstream customer-facing fulfilment errors.

Project Goal: Reduce catalogue defect rate from 12% to less than 3% within 90 days, achieving EUR 10,000+ annual cost saving.

Success Metrics:
1. Catalogue defect rate (target: less than 3%)
2. Daily rework time per shift (target: less than 5 minutes)
3. Customer-facing error rate (target: less than 0.5%)
4. Cost of Poor Quality (target: less than EUR 3,000/year)
```

---

*Part of the AI + Lean Six Sigma DMAIC Playbook | [Back to Chapter 1](../chapters/01-define.md)*
