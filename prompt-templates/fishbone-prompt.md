# Prompt Template: AI-Generated Fishbone (Ishikawa) Diagram

**Phase:** Analyse  
**Tool:** ChatGPT / Copilot / Gemini  
**Time to output:** 2 minutes

---

## Copy-Paste Prompt

```
I am running a Lean Six Sigma Analyse phase. My problem symptom is:

[REPLACE: Describe the symptom/defect clearly in 1-2 sentences. Include: what is going wrong, the measured rate or scale if known.]

My process context:
- Industry/function: [e.g. warehouse operations / financial services / healthcare]
- Process: [e.g. inbound catalogue classification / invoice processing / patient discharge]
- Team size: [e.g. 15 operators across 3 shifts]
- Volume: [e.g. 2,000 transactions per day]

Please generate a comprehensive Fishbone (Ishikawa) diagram with potential root causes across all 6 categories:

1. Man (People) - training, skill, behaviour, communication
2. Machine (Equipment/Systems) - technology, tools, software, infrastructure
3. Method (Process) - SOPs, procedures, workflows, standards
4. Material (Inputs) - data quality, raw materials, supplier inputs
5. Measurement (Data/Metrics) - measurement errors, data gaps, reporting lags
6. Mother Nature (Environment) - volume spikes, shift patterns, external pressures

For each category:
- List 4-6 specific, actionable potential causes
- Tailor causes to my industry and process context
- Flag which causes are most likely to be systemic vs one-off

Format as a structured table: Category | Potential Cause | Systemic or One-off?
```

---

## Follow-Up Prompts

After getting your fishbone, use these follow-up prompts:

**To prioritise causes:**
```
From the fishbone diagram above, which 3-5 causes are most likely to explain 80% of the defects? Rank them by likelihood and explain your reasoning.
```

**To convert to hypotheses:**
```
Convert the top 5 root causes into testable hypotheses using this format:
"If [cause], then [effect], which would be visible as [observable evidence]."
```

---

## Usage Tips

- Run this prompt BEFORE your team workshop, not instead of it
- Use the AI output to seed your workshop discussion and avoid blank-page syndrome
- Always validate AI-generated causes with people who work in the process
- The best fishbones combine AI breadth with team expertise

---

*Part of the AI + Lean Six Sigma DMAIC Playbook | [Back to Chapter 3](../chapters/03-analyse.md)*
