# Chapter 2: Measure Phase — AI-Augmented DMAIC

## Overview

The Measure phase is about establishing a data baseline: what is the current performance, how do we collect reliable data, and what does good look like? AI accelerates data gap identification, measurement system selection, and baseline dashboard creation.

**AI Saves You:** Data collection planning, MSA guidance, sample size calculations, baseline dashboard setup.

---

## Use Case 1: AI-Identified Data Collection Gaps

### What AI does in 5 minutes:
Describe your process and current data sources - AI identifies what you are missing.

### Prompt:
```
I am running a Lean Six Sigma Measure phase for this process:
[describe your process]

My current data sources are:
[list your data sources]

My defect/problem is:
[describe the issue]

Please:
1. Identify data collection gaps
2. Suggest additional data points I should capture
3. Recommend the right measurement type (discrete vs continuous) for each metric
4. Suggest sample size guidance based on my process volume
```

### Before (manual approach):
Team meeting to review data sources, 2-3 days to identify gaps, manual calculation of sample sizes.

### After (AI output example):
**Data Gaps Identified:**
- Missing: Time-stamp data at classification step (needed to identify shift-pattern defects)
- Missing: Source system ID per defect (needed to pinpoint upstream root cause)
- Missing: Operator ID per transaction (needed for MSA)

**Recommended Metrics:**
| Metric | Type | Recommended Sample Size |
|--------|------|-------------------------|
| Defect rate (%) | Discrete (attribute) | Minimum 300 units per stratum |
| Processing time (mins) | Continuous (variable) | Minimum 30 samples per subgroup |
| Rework cost (GBP) | Continuous (variable) | All transactions (100%) |

---

## Use Case 2: AI-Guided Measurement System Selection

### Prompt:
```
For a Lean Six Sigma project measuring [describe your metric], please:
1. Recommend whether to use discrete or continuous measurement
2. Suggest the appropriate measurement system analysis (MSA) approach
3. Identify potential sources of measurement error
4. Recommend a data collection frequency and period
```

### AI Output Example:
**For catalogue defect rate measurement:**
- Use **Discrete (attribute)** measurement: defective / non-defective
- MSA approach: Attribute Agreement Analysis (2 appraisers, 50 items, 2 rounds)
- Potential measurement errors: Ambiguous classification rules, subjective judgement calls, system lag
- Collection frequency: Daily snapshot, minimum 4-week baseline period

---

## Use Case 3: AI + Copilot Baseline Dashboard

### What AI does:
Generate a baseline performance dashboard structure using Microsoft Copilot in Excel.

### Copilot Prompt (in Excel):
```
I have a dataset with these columns:
- Date, Shift, Operator_ID, Item_ID, Classification_Code, Defect_Flag (Y/N), Rework_Time_Mins, Source_System

Please:
1. Create a summary pivot showing defect rate by week
2. Add a trend line chart showing defect rate over time
3. Calculate the process baseline: mean defect rate, standard deviation, and Cpk if applicable
4. Highlight weeks where defect rate exceeded 10% in red
```

### Baseline Dashboard Template:
Download the Excel template from [`/templates/baseline-dashboard-template.xlsx`](../templates/) (see repo for file).

**Key metrics your baseline dashboard should capture:**
| Metric | Baseline Target | Data Source |
|--------|----------------|-------------|
| Defect Rate % | Current state (no target yet) | Operations system |
| Volume by period | Trend over 8 weeks | Warehouse WMS |
| Rework time (mins/shift) | Current state | Timesheet / manual log |
| Cost of Poor Quality (COPQ) | Calculated: rework rate x hourly cost | Finance system |

---

## Use Case 4: Sample Size Calculator Prompt

### Prompt:
```
I need to calculate the right sample size for my Lean Six Sigma Measure phase.

Process details:
- Daily volume: [X units per day]
- Current estimated defect rate: [X%]
- Confidence level required: 95%
- Margin of error acceptable: +/- 3%

Please calculate the minimum sample size and tell me how many days of data collection I need.
```

---

## Time Savings Summary

| Task | Manual | AI-Augmented | Saved |
|------|--------|--------------|-------|
| Data gap analysis | 2 days | 30 minutes | 94% |
| MSA planning | 1 day | 20 minutes | 97% |
| Baseline dashboard | 3 days | 2 hours | 92% |
| Sample size calculation | 2 hours | 5 minutes | 96% |

---

[Previous: Chapter 1 - Define](01-define.md) | [Next: Chapter 3 - Analyse](03-analyse.md)
