# Chapter 1: Define Phase — AI-Augmented DMAIC

## Overview

The Define phase sets the foundation for your entire DMAIC project. Traditionally this involves 1-2 weeks of stakeholder meetings, charter workshops, and VOC analysis. With AI, you can compress this to 2-3 hours.

**AI Saves You:** Project Charter drafting, SIPOC mapping, VOC structuring, problem statement writing.

---

## Use Case 1: AI-Generated Project Charter

### What AI does in 60 seconds:
Paste a plain-English problem description and get a structured Project Charter draft.

### Prompt:
```
I need to create a Lean Six Sigma Project Charter. Here is the plain-English problem:
[describe your problem in 2-3 sentences]

Please generate a full Project Charter including: Problem Statement, Project Goal, Scope (in/out), Business Impact (quantified), Project Sponsor, Team Members, Timeline, and Success Metrics.
```

### Before (input):
"Our warehouse is processing too many defective items incorrectly classified in the catalogue. It is slowing down fulfilment and causing customer complaints."

### After (AI output):
| Charter Element | Draft |
|----------------|-------|
| Problem Statement | Incorrectly catalogued items are causing a 12% defect rate in fulfilment, resulting in customer escalations and rework costs. |
| Project Goal | Reduce catalogue defect rate from 12% to less than 3% within 90 days. |
| Scope | Inbound catalogue classification process |
| Business Impact | Estimated EUR 180K annual rework cost reduction |
| Timeline | 12 weeks |

---

## Use Case 2: AI-Structured VOC Analysis

### Prompt:
```
Here are raw survey responses from operations team members:
[paste responses]

Please:
1. Identify the top 5 recurring themes
2. Map each theme to a Critical-to-Quality (CTQ) requirement
3. Draft a formal problem statement: Currently [situation], causing [impact], affecting [who].
```

### Before (raw VOC):
- "Items keep coming through with wrong category codes"
- "We spend 30 mins per shift fixing catalogue errors"
- "Customers complain about wrong product descriptions"

### After (AI structured output):
**CTQ Themes:**
1. Data accuracy > CTQ: Catalogue error rate less than 1%
2. Process efficiency > CTQ: Rework time less than 5 mins/shift
3. System currency > CTQ: Classification rules updated quarterly

**Problem Statement:** "Currently, catalogue items are being misclassified at 12%, causing 30 minutes of rework per shift and fulfilment errors affecting 2,400 daily orders."

---

## Use Case 3: AI-Generated SIPOC Diagram

### Prompt:
```
Generate a SIPOC table for this process:
Process: [describe your process in 1-2 sentences]
Problem: [describe the defect or issue]

Format as a 5-column table: Suppliers | Inputs | Process Steps | Outputs | Customers
```

### AI Output Example:
| Suppliers | Inputs | Process Steps | Outputs | Customers |
|-----------|--------|---------------|---------|----------|
| Vendors | Product data | 1. Receive item data | Classified catalogue entry | Warehouse ops |
| Catalogue team | Classification rules | 2. Apply classification | Item master record | Fulfilment systems |
| IT systems | ERP/WMS data | 3. Validate | Defect flag | End customers |
| Quality team | QA checklists | 4. Approve and publish | Audit trail | Finance |

---

## Time Savings Summary

| Task | Manual | AI-Augmented | Saved |
|------|--------|--------------|-------|
| Project Charter draft | 3 days | 30 minutes | 95% |
| VOC analysis | 5 days | 2 hours | 94% |
| SIPOC mapping | 1 day | 20 minutes | 97% |
| **Total Define phase** | **~2 weeks** | **~3 hours** | **~94%** |

---

## Real-World Reference

Inspired by the Amazon PFV-BIC DMAIC project (catalogue defect mitigation). AI-augmented initiation could cut project start-up from 2 weeks to 3 days.

---

[Next: Chapter 2 - Measure](02-measure.md)
