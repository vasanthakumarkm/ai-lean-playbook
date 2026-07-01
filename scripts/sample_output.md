# Sample Output — SPC Control Chart Generator

This file shows what the script produces when run against [`sample_data.csv`](sample_data.csv).

---

## How to Run

```bash
# Standard run using the sample input file
python spc_chart.py --input sample_data.csv --metric "Defect Rate (%)" --output spc_chart.png

# Or use the built-in demo mode (auto-generates its own data)
python spc_chart.py --demo
```

---

## Sample Input (`sample_data.csv`)

Weekly defect rate measurements across 30 weeks.
Weeks 1–12: baseline period (~12% defect rate, pre-improvement).
Weeks 6–7: two injected out-of-control spikes (18.5% and 17.2%).
Weeks 13–30: post-improvement period (~5% defect rate).

```
Date,Measurement
2026-01-06,11.32
2026-01-13,13.08
2026-01-20,10.75
...
2026-07-28,5.14
```

---

## Console Output (sample)

```
Loading data from: sample_data.csv
Loaded 30 observations.

============================================================
 SPC ANALYSIS SUMMARY: Defect Rate (%)
============================================================
 Observations (n)       : 30
 Process Mean (X-bar)   : 8.2973
 Standard Deviation     : 4.1521
 Upper Control Limit    : 20.7537
 Lower Control Limit    : 0.0000
 Out-of-control points  : 2

 Out-of-control details:
  - Point 6: Rule 1: Beyond 3-sigma limits
  - Point 7: Rule 1: Beyond 3-sigma limits

 Process Status: OUT OF CONTROL - INVESTIGATE
============================================================

Chart saved to: spc_chart.png
```

---

## Output Chart Description (`spc_chart.png`)

The saved PNG chart contains:

| Chart Element | Description |
|---|---|
| **Blue line** | Measurement values plotted across all 30 weeks |
| **Blue dots** | In-control data points |
| **Red dots** | Out-of-control points (weeks 6 & 7 — the spikes) |
| **Green line** | Process mean (X-bar = 8.30%) |
| **Yellow dashed lines** | UCL (20.75%) and LCL (0.00%) |
| **Green shaded band** | Control zone between UCL and LCL |
| **Stats box** | Top-left summary: n, mean, std dev, UCL, LCL, OOC count |
| **Annotations** | Red labels on OOC points: "Rule 1" |

### What the chart story tells:
- **Weeks 1–12**: process running at ~12% defect rate — stable but high
- **Weeks 6–7**: two points breach UCL (highlighted red) — triggered investigation
- **Weeks 13–30**: defect rate drops to ~5% after improvement implemented — visible step-change
- **Conclusion**: post-improvement process is in control but UCL/LCL need recalculating for the new baseline

---

## Nelson Rules Applied

The script checks three rules automatically:

| Rule | Description | Triggered? |
|------|-------------|------------|
| Rule 1 | 1 point beyond 3-sigma limits | Yes — points 6 & 7 |
| Rule 2 | 8 consecutive points same side of mean | No |
| Rule 3 | 6 consecutive points trending up or down | No |

---

## Re-running After Improvement

Once the improvement is confirmed stable, recalculate control limits using only the post-improvement data:

```bash
# Create a trimmed CSV with only weeks 13-30
python spc_chart.py --input post_improvement_data.csv --metric "Defect Rate (%) - Post Improvement" --output spc_post_improvement.png
```

This gives you a tighter UCL/LCL reflecting the new process capability — ready for your Control phase report.

---

*Part of the AI + Lean Six Sigma DMAIC Playbook | [Back to Chapter 5 — Control](../chapters/05-control.md)*
