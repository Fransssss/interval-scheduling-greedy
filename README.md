# interval-scheduling-greedy

A small Python project that solves the **Interval Scheduling Maximization** problem using a **Greedy Algorithm**.

---

## Problem Description

Given a list of intervals, where each interval represents a task with a `start_time` and an `end_time`, the goal is to **select the maximum number of non-overlapping intervals**.

Two intervals overlap if one starts before the other ends. We want to find the largest subset of intervals such that no two intervals in the subset overlap.

---

## Greedy Strategy

The algorithm uses the following greedy approach:

1. **Sort** all intervals by their **finish time** (earliest finish time first).
2. **Always select** the interval with the earliest finish time that does not conflict with the previously selected interval.

**Why does this work?**  
By picking the interval that ends the soonest, we leave the most room open for future intervals. This locally optimal choice at each step leads to a globally optimal solution — a well-known result in algorithm design.

---

## Project Structure

```
interval-scheduling-greedy/
├── main.py                # Entry point — runs the demo with a sample dataset
├── interval_scheduler.py  # Core algorithm implementation
└── README.md
```

---

## How to Run

```bash
python main.py
```

---

## Example Input

```
All intervals (12 total):
  Start:  1,  End:  4
  Start:  3,  End:  5
  Start:  0,  End:  6
  Start:  5,  End:  7
  Start:  3,  End:  9
  Start:  5,  End:  9
  Start:  6,  End: 10
  Start:  8,  End: 11
  Start:  8,  End: 12
  Start:  2,  End: 14
  Start: 12,  End: 16
  Start: 10,  End: 15
```

## Example Output

```
=============================================
  Interval Scheduling — Greedy Algorithm
=============================================

All intervals (12 total):
  Start:  1,  End:  4
  Start:  3,  End:  5
  Start:  0,  End:  6
  Start:  5,  End:  7
  Start:  3,  End:  9
  Start:  5,  End:  9
  Start:  6,  End: 10
  Start:  8,  End: 11
  Start:  8,  End: 12
  Start:  2,  End: 14
  Start: 12,  End: 16
  Start: 10,  End: 15

Selected non-overlapping intervals (4 chosen):
  Start:  1,  End:  4
  Start:  5,  End:  7
  Start:  8,  End: 11
  Start: 12,  End: 16

Maximum number of non-overlapping intervals: 4
=============================================
```

---

## Complexity Analysis

### Time Complexity: O(n log n)

- Sorting the `n` intervals by finish time takes **O(n log n)**.
- The single pass through the sorted list to select intervals takes **O(n)**.
- Overall: **O(n log n)**, dominated by the sort step.

### Space Complexity: O(n)

- The sorted copy of the intervals list uses **O(n)** space.
- The result list holds at most `n` intervals, also **O(n)**.
- Overall: **O(n)**.
