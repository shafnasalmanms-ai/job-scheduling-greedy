# 📅 Job Scheduling with Deadlines – Greedy Algorithm

## 📌 Overview

This project solves the **Job Scheduling with Deadlines** problem using a **greedy algorithm**.  
Given a set of jobs, each with a **deadline** and a **reward**, the goal is to schedule at most one job per unit time to **maximise the total reward**.

The project includes:
- A **Python implementation** of the greedy algorithm.
- An **interactive HTML/JavaScript visualizer** that shows the scheduled timeline and total reward.

---

## 🧠 Algorithm (Greedy)

1. Sort all jobs in **descending order of reward**.
2. Find the **maximum deadline** to know how many time slots exist.
3. Create an array `slots` of size `(max_deadline + 1)`, initially all empty (`-1`).
4. For each job (in sorted order):
   - Try to assign it to the **latest free slot** `t` where `1 ≤ t ≤ deadline`.
   - If such a slot exists, mark it occupied, add the reward, and record the job.
5. Return the **total reward** and the list of **selected jobs**.

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `job_scheduling.py` | Python script with the greedy algorithm |
| `visualizer.html` | HTML/JS visualizer – open in any browser |
| `README.md` | This file |

---

## 🚀 How to Run

### Clone the Repository

```bash
git clone https://github.com/shafnasalmanms-ai/job-scheduling-greedy.git
cd job-scheduling-greedy
```

### Run Python Script

```bash
python job_scheduling.py
```

**Example output:**

```
Total Reward: 180
Chosen jobs (deadline, reward): [(2, 100), (2, 80)]
```

### Web Visualizer

1. Double-click `visualizer.html` or open it in your browser.
2. Click **"Run Scheduling"** to see the timeline and result.

---

## 🧪 Example

**Input:**

```python
jobs = [(2, 100), (1, 50), (2, 80), (1, 30)]
```

**Output:**

```
Total Reward = 180
Selected Jobs = [(2, 100), (2, 80)]
```

**Explanation:**

| Time Slot | Job Assigned | Reward |
|-----------|--------------|--------|
| Slot 2    | Job (2, 100) | 100    |
| Slot 1    | Job (2, 80)  | 80     |

> Jobs `(1, 50)` and `(1, 30)` cannot be scheduled — no free slots remain within their deadlines.

---

## ⏱️ Complexity

| Type  | Complexity |
|-------|------------|
| Time  | O(n²) — due to the nested loop for slot finding |
| Space | O(n) — for the slots array |

> Can be optimised to **O(n log n)** using a **Union-Find / Disjoint Set** data structure.

---
