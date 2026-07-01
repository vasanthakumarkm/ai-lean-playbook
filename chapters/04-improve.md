# Chapter 4: Improve Phase — AI-Augmented DMAIC

## Overview

The Improve phase is where your root causes get solved. AI accelerates solution generation, scoring, and the change management communications needed to get solutions adopted.

**AI Saves You:** Solution brainstorming, structured scoring, change communication drafting, stakeholder messaging.

---

## Use Case 1: AI Solution Evaluation and Scoring Matrix

### What AI does in 5 minutes:
Evaluate and rank solution options against defined criteria (cost, effort, impact, risk).

### Prompt:
```
I have completed my Lean Six Sigma Analyse phase. My verified root cause is:
[describe your root cause]

My project constraints are:
- Budget: [X]
- Timeline: [X weeks]
- Team capacity: [X]
- Key stakeholder concern: [e.g. minimal disruption to operations]

Here are my 4 potential solutions:
1. [Solution A]
2. [Solution B]
3. [Solution C]
4. [Solution D]

Please create a weighted solution scoring matrix. Score each solution on:
- Impact on root cause (1-5)
- Implementation cost (5=low cost, 1=high cost)
- Ease of implementation (1-5)
- Speed to benefit (1-5)
- Risk level (5=low risk, 1=high risk)

Weight impact at 40%, cost at 20%, ease at 20%, speed at 10%, risk at 10%.
Recommend the top 2 solutions with justification.
```

### Before (manual approach):
Team debate, political influencing, consensus-based decision - often selects the easiest not the best solution.

### After (AI output example):
**Solution Scoring Matrix - Catalogue Defect Reduction:**

| Solution | Impact (40%) | Cost (20%) | Ease (20%) | Speed (10%) | Risk (10%) | Weighted Score |
|----------|------------|-----------|-----------|------------|-----------|----------------|
| A: Update SOP + Training | 4 | 4 | 4 | 3 | 5 | 4.0 |
| B: Implement system validation rules | 5 | 2 | 2 | 2 | 3 | 3.3 |
| C: Add QA checkpoint (manual) | 3 | 4 | 5 | 4 | 4 | 3.7 |
| D: Vendor data quality agreement | 4 | 3 | 2 | 1 | 2 | 2.9 |

**Recommendation:** Solution A (SOP + Training) scores highest and delivers quick wins. Combine with Solution C (QA checkpoint) for maximum impact at low cost.

---

## Use Case 2: AI-Generated Change Management Communication

### What AI does:
Draft stakeholder communications for a process change rollout.

### Prompt:
```
I need to communicate a process change to my operations team. Here are the details:

What is changing: [describe the change]
Why it is changing: [the business reason]
Who is affected: [audience]
When it starts: [date]
What they need to do differently: [3-5 key actions]
Who to contact with questions: [name/team]

Please write:
1. A 150-word team communication email (clear, jargon-free, positive tone)
2. A 1-page quick reference guide for the new process
3. A manager FAQ document (top 5 questions managers will ask)
```

### AI Output Example (team email):
```
Subject: Important Update - Catalogue Classification Process (Effective [Date])

Hi Team,

Following our recent process review, we are updating how we classify catalogue items to improve accuracy and reduce rework.

From [Date], please follow these steps:
1. Use the updated Classification Guide (link)
2. Flag any items you are unsure about - do not guess
3. Complete the new QA check before submitting each batch

This change will reduce the rework we have all been dealing with and make your day easier. Training takes 15 minutes and is available [here].

Questions? Contact [Name] at [email].

Thank you for your support.
[Manager Name]
```

---

## Use Case 3: AI-Modelled Solution Scenario

### Prompt:
```
I want to model the expected impact of my proposed solution before implementing it.

Current state:
- Defect rate: [X%]
- Daily volume: [X units]
- Rework cost per defect: [EUR X]
- Annual cost of defects: [EUR X]

Proposed solution: [describe your solution]

Based on similar process improvement cases, please:
1. Estimate the realistic defect rate reduction range (conservative / expected / optimistic)
2. Calculate the projected annual cost saving for each scenario
3. Estimate the break-even point if the solution costs [EUR X] to implement
4. Identify the key assumptions in your model
```

### AI Output Example:
| Scenario | Defect Rate Reduction | Annual Saving | Break-Even |
|----------|----------------------|--------------|------------|
| Conservative | 40% reduction (to 7.2%) | EUR 72,000 | 2.5 months |
| Expected | 65% reduction (to 4.2%) | EUR 117,000 | 1.5 months |
| Optimistic | 80% reduction (to 2.4%) | EUR 144,000 | 1.2 months |

---

## Use Case 4: Pilot Design Prompt

### Prompt:
```
I want to design a pilot test for my solution before full rollout.

Solution: [describe your solution]
Process volume: [X units/day]
Pilot duration I am considering: [X weeks]

Please:
1. Recommend the minimum pilot sample size needed for statistical validity
2. Define pilot success criteria (what metrics prove it is working?)
3. Identify pilot risks and mitigation actions
4. Create a simple pilot tracking sheet structure
```

---

## Time Savings Summary

| Task | Manual | AI-Augmented | Saved |
|------|--------|--------------|-------|
| Solution scoring workshop | 4 hours | 10 minutes | 96% |
| Change comms drafting | 1 day | 20 minutes | 97% |
| Impact modelling | 3 days | 30 minutes | 97% |
| Pilot design | 2 days | 1 hour | 94% |

---

[Previous: Chapter 3 - Analyse](03-analyse.md) | [Next: Chapter 5 - Control](05-control.md)
