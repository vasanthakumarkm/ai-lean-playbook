# Chapter 3: Analyse Phase — AI-Augmented DMAIC

## Overview

The Analyse phase is about finding the root cause of your problem — not symptoms. AI dramatically accelerates fishbone diagram generation, 5 Whys analysis, and pattern detection in defect data.

**AI Saves You:** Fishbone brainstorming, structured 5 Whys, defect log pattern analysis, hypothesis generation.

---

## Use Case 1: AI-Generated Fishbone (Ishikawa) Diagram

### What AI does in 2 minutes:
Describe your symptom and AI generates a comprehensive Ishikawa diagram across all 6Ms.

### Prompt:
```
I am running a Lean Six Sigma Analyse phase. My problem symptom is:
[describe the symptom/defect clearly]

My process is in [industry/function] and involves [brief process description].

Please generate a Fishbone (Ishikawa) diagram with potential root causes across these categories:
- Man (People)
- Machine (Equipment/Systems)
- Method (Process)
- Material (Inputs)
- Measurement (Data)
- Mother Nature (Environment)

For each category, list 3-5 specific potential causes relevant to my context.
```

### Before (manual approach):
Facilitated workshop with 6-8 people, 2-3 hours, sticky notes, whiteboard - often misses technical causes.

### After (AI output example):
**Problem: Catalogue items being misclassified at 12% defect rate**

| Category | Potential Root Causes |
|----------|----------------------|
| Man | Insufficient training on classification rules; High staff turnover; No standard work documentation |
| Machine | ERP classification module not updated in 18 months; Slow system response causing skip-clicks; No validation rules in system |
| Method | Classification SOP last updated 2 years ago; No QA checkpoint at classification step; Batch processing without review |
| Material | Vendor-provided product data incomplete; Multiple data formats from different suppliers; Missing mandatory fields |
| Measurement | No real-time defect tracking; Daily defect report reviewed weekly only; No defect category breakdown |
| Environment | High-volume peak periods with reduced accuracy; Remote team lacking real-time support |

---

## Use Case 2: AI-Structured 5 Whys Analysis

### What AI does:
Run iterative 5 Whys analysis with structured depth - AI prevents shallow answers.

### Prompt:
```
Please help me run a structured 5 Whys analysis for this problem:

Problem statement: [your problem statement from Define phase]

For each Why, push past the obvious answer to the systemic cause. After 5 iterations, identify:
1. The verified root cause
2. Whether it is a People, Process, or System issue
3. Recommended corrective action type (immediate fix vs systemic change)
```

### Before vs After Example:

**Problem:** Catalogue items are misclassified at 12% defect rate.

| Why # | Shallow Answer (manual) | Deep Answer (AI-guided) |
|-------|------------------------|------------------------|
| Why 1 | Staff made errors | Classification rules are ambiguous for multi-category items |
| Why 2 | Staff not trained | Training materials reference outdated rule set (v2019) |
| Why 3 | Training not updated | No owner assigned to maintain classification documentation |
| Why 4 | Process gaps exist | Change management process does not include catalogue rule updates |
| Why 5 | - | Governance model has no accountability for classification accuracy KPI |

**Root Cause:** No designated owner for classification rule governance, and no KPI tracking classification accuracy at leadership level.

**Category:** Process + People

**Corrective Action Type:** Systemic — create governance role + add KPI to leadership scorecard.

---

## Use Case 3: AI Pattern Detection in Defect Logs

### What AI does:
Analyse a sample defect log and identify patterns by time, operator, category, shift, etc.

### Prompt:
```
Here is a sample defect log from our process (CSV format):
[paste or describe your data: Date, Shift, Operator, Defect_Type, Item_Category, Source_System]

Please:
1. Identify the top 3 defect patterns by category, time, or operator
2. Highlight any Pareto principle insights (which 20% of causes drive 80% of defects?)
3. Suggest which patterns should be prioritised for root cause investigation
4. Generate a hypothesis statement for each top pattern
```

### AI Output Example (synthetic Amazon-style data):
**Top Patterns Identified:**

| Pattern | % of Defects | Hypothesis |
|---------|-------------|------------|
| Defects spike on Monday morning (Shift 1) | 34% | Weekend system updates changing classification rules not communicated to AM shift |
| 68% of defects from 3 item categories (Electronics, Apparel, Multi-pack) | 68% | These categories have most complex classification rules with highest ambiguity |
| Operator group B has 3x defect rate vs group A | 41% | Group B received different training version or has newer starters |

**Pareto Finding:** 3 of 47 item categories account for 68% of all defects — fix these 3 first.

---

## Use Case 4: Hypothesis Validation Prompt

### Prompt:
```
I have these root cause hypotheses from my Analyse phase:
1. [Hypothesis 1]
2. [Hypothesis 2]
3. [Hypothesis 3]

For each hypothesis, please:
1. Suggest the best statistical test or validation method
2. Tell me what data I need to validate or reject it
3. Describe what a confirmed vs rejected hypothesis would look like
4. Rate the ease of validation (Easy / Medium / Hard)
```

---

## Time Savings Summary

| Task | Manual | AI-Augmented | Saved |
|------|--------|--------------|-------|
| Fishbone diagram workshop | 3 hours | 10 minutes | 94% |
| 5 Whys facilitation | 2 hours | 15 minutes | 88% |
| Defect log pattern analysis | 2 days | 30 minutes | 97% |
| Hypothesis generation | 4 hours | 20 minutes | 92% |

---

[Previous: Chapter 2 - Measure](02-measure.md) | [Next: Chapter 4 - Improve](04-improve.md)
