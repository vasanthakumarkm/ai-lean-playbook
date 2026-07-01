# Prompt Template: AI Solution Scoring Matrix

**Phase:** Improve  
**Tool:** ChatGPT / Copilot / Gemini  
**Time to output:** 5 minutes

---

## Copy-Paste Prompt

```
I have completed my Lean Six Sigma Analyse phase and identified my root cause. I now need to evaluate solution options.

Verified root cause:
[REPLACE: Paste your confirmed root cause statement here.]

Project constraints:
- Budget available: [e.g. EUR 10,000 / minimal - people time only]
- Implementation timeline: [e.g. must be live within 8 weeks]
- Team capacity: [e.g. 2 people, 20% of their time]
- Key stakeholder concern: [e.g. must not disrupt operations / must be low IT cost]
- What cannot be changed: [e.g. cannot replace the ERP system / headcount frozen]

Here are my proposed solutions:
1. [Solution A - describe briefly]
2. [Solution B - describe briefly]
3. [Solution C - describe briefly]
4. [Solution D - describe briefly]

Please create a weighted solution scoring matrix. For each solution, score 1-5 on these criteria:
- Impact on root cause (5 = fully addresses root cause, 1 = minimal impact)
- Implementation cost (5 = very low cost, 1 = very high cost)
- Ease of implementation (5 = easy, 1 = highly complex)
- Speed to benefit (5 = impact within 2 weeks, 1 = impact takes more than 6 months)
- Sustainability (5 = self-sustaining, 1 = requires constant monitoring)
- Risk to operations (5 = zero operational risk, 1 = high disruption risk)

Weighting:
- Impact: 35%
- Cost: 20%
- Ease: 15%
- Speed: 15%
- Sustainability: 10%
- Risk: 5%

Provide:
1. The weighted scoring table
2. A ranked list of solutions
3. Your recommended solution(s) with justification
4. Any solution combinations worth considering
5. Top 3 implementation risks for the recommended solution
```

---

## Follow-Up Prompts

**To stress-test the recommendation:**
```
For the recommended solution above, what are the most likely reasons it could fail? How would I mitigate each risk?
```

**To build the business case:**
```
For solution [X], please build a simple business case:
- One-time implementation cost estimate
- Annual benefit (cost saving or revenue protection)
- Payback period
- Key assumptions
```

---

## Usage Tips

- Adjust the weightings to match your stakeholder priorities
- Add criteria specific to your context (e.g. regulatory compliance, staff morale)
- Always sanity-check AI scores against team knowledge
- The scoring is a decision support tool, not a substitute for stakeholder buy-in

---

*Part of the AI + Lean Six Sigma DMAIC Playbook | [Back to Chapter 4](../chapters/04-improve.md)*
