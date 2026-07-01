# Chapter 5: Control Phase — AI-Augmented DMAIC

## Overview

The Control phase ensures your improvements stick. Without robust controls, processes revert to their old state within months. AI helps you build SPC charts, control plans, and automated monitoring alerts faster than any manual approach.

**AI Saves You:** SPC chart setup, control plan drafting, monitoring logic design, handover documentation.

**Python Script:** See [`/scripts/spc_chart.py`](../scripts/spc_chart.py) for a ready-to-run SPC chart generator.

---

## Use Case 1: Python SPC Control Chart

### What the script does:
Input a CSV of process measurements. Output an X-bar chart with UCL/LCL control limits, flagging out-of-control points automatically.

### How to use:
1. Prepare your data as a CSV: `Date, Measurement, Subgroup`
2. Run: `python spc_chart.py --input your_data.csv --metric "Defect Rate %" --output spc_output.png`
3. Chart is saved as PNG, ready to include in your Control phase report

### What the chart shows:
- Centre line (process mean)
- Upper Control Limit (UCL) = mean + 3 sigma
- Lower Control Limit (LCL) = mean - 3 sigma
- Out-of-control points highlighted in red
- Rule violations annotated (Nelson rules)

### Sample output description:
A 12-week run chart showing defect rate trending from 12% (weeks 1-4) to 3.8% (weeks 9-12) post-improvement, with UCL at 8.2% and LCL at 0%. Two out-of-control points flagged in weeks 6-7 (transition period).

---

## Use Case 2: AI-Generated Control Plan

### What AI does:
Generate a full Control Plan from a summary of your Improve phase outputs.

### Prompt:
```
I have completed my Lean Six Sigma Improve phase. Please generate a Control Plan based on this summary:

Process: [describe your process]
Solution implemented: [describe what was changed]
Key metrics to monitor: [list 3-5 metrics]
Target performance: [e.g. defect rate less than 3%]
Process owner: [name/role]

Please create a Control Plan table with these columns:
- Process Step
- What to Control
- Control Method
- Measurement Frequency
- Who is Responsible
- Reaction Plan (if out of control)
- Target / Specification
```

### AI Output Example:
| Process Step | What to Control | Control Method | Frequency | Responsible | Reaction Plan | Target |
|-------------|----------------|----------------|-----------|-------------|---------------|--------|
| Item classification | Defect rate % | SPC chart (auto) | Daily | Process Analyst | Escalate to team lead if >5% for 3 consecutive days | Less than 3% |
| QA checkpoint | Check completion rate | Dashboard | Per shift | QA Lead | Investigate and retrain if below 95% | 100% |
| SOP adherence | Compliance audit score | Monthly audit | Monthly | Operations Manager | Coaching session + refresher training | Greater than 95% |
| System validation | Error flag trigger rate | Automated alert | Real-time | IT/Systems | Investigate root cause within 24 hours | Less than 1% |

---

## Use Case 3: AI-Designed Monitoring Alert Logic

### Prompt:
```
I need to set up automated monitoring for my process after a DMAIC improvement. Please design the alert logic.

Metric I am monitoring: [metric name]
Current process mean: [X]
UCL: [X] (or calculate from: mean + 3 x standard deviation)
LCL: [X] (or calculate from: mean - 3 x standard deviation)
Data source: [where the data comes from]
Alerting tool available: [Excel, Power BI, Python, email]

Please:
1. Write the alert trigger conditions (Western Electric / Nelson rules)
2. Draft the alert message for each trigger type
3. Define the escalation path
4. Suggest how to automate this in [your tool]
```

### AI Output Example:
**Alert Conditions for Defect Rate monitoring:**

| Rule | Trigger | Alert Message | Escalation |
|------|---------|---------------|------------|
| Rule 1 | 1 point beyond UCL/LCL | CRITICAL: Defect rate at [X%] - outside control limits. Immediate investigation required. | Process Analyst - same day |
| Rule 2 | 8 consecutive points same side of mean | WARNING: Sustained shift detected in defect rate. Process may have changed. | Team Lead - within 24 hours |
| Rule 3 | 6 points trending up or down | WARNING: Trending pattern detected. Review recent process changes. | Team Lead - within 48 hours |

**Python automation snippet:**
```python
import pandas as pd

def check_spc_alerts(df, metric_col, ucl, lcl, mean):
    alerts = []
    values = df[metric_col].values
    for i, val in enumerate(values):
        if val > ucl or val < lcl:
            alerts.append(f"CRITICAL: Point {i+1} = {val:.2f} is outside control limits (UCL={ucl:.2f}, LCL={lcl:.2f})")
    return alerts
```

---

## Use Case 4: AI-Generated Handover Documentation

### Prompt:
```
I need to create a DMAIC project handover document for the process owner. Please generate:

1. A 1-page project summary (problem, solution, results)
2. A lessons learned section (3-5 key insights)
3. A sustainment checklist for the process owner
4. A 90-day review plan (what to check and when)

Project details:
- Problem: [X]
- Solution implemented: [X]
- Results achieved: [X]
- Process owner: [X]
```

---

## Time Savings Summary

| Task | Manual | AI-Augmented | Saved |
|------|--------|--------------|-------|
| SPC chart setup | 1 day | 5 minutes (script) | 99% |
| Control plan drafting | 2 days | 20 minutes | 98% |
| Alert logic design | 1 day | 30 minutes | 97% |
| Handover documentation | 3 days | 1 hour | 96% |

---

## Python Script Reference

The full SPC chart generator is available at: [`/scripts/spc_chart.py`](../scripts/spc_chart.py)

Features:
- Reads CSV input
- Calculates X-bar, UCL, LCL automatically
- Flags out-of-control points (Nelson Rule 1)
- Outputs chart as PNG
- Prints summary statistics to console

---

[Previous: Chapter 4 - Improve](04-improve.md) | [Back to README](../README.md)
