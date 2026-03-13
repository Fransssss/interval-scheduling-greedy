# interval-scheduling-greedy

A Python implementation of the **Interval Scheduling Maximization** problem using a greedy algorithm.

## What it does

Given a set of intervals (each with a start and end time), it selects the **maximum number of non-overlapping intervals** — the classic "activity selection" problem.

## How it works

Uses the **Earliest Deadline First** strategy: sort intervals by end time, then greedily pick each interval that starts after the last selected one ends.

## Usage

```python
from main import interval_scheduling

intervals = [(1, 4), (3, 5), (5, 7), (6, 10), (8, 11), (12, 14)]
result = interval_scheduling(intervals)
# → [(1, 4), (5, 7), (8, 11), (12, 14)]
```

Run directly:

```bash
python main.py
```