# interval-scheduling-greedy

A small Python project that solves the **Interval Scheduling Maximization**
problem using a **Greedy Algorithm**.

---

## Problem Description

Given a list of intervals, where each interval represents an activity with a
`start_time` and an `end_time`, find the **maximum number of non-overlapping
intervals** that can be selected.

Two intervals overlap if one starts before the other has finished, i.e.
`interval_A.start < interval_B.end` **and** `interval_B.start < interval_A.end`.

---

## Greedy Strategy

The algorithm uses the classic **Earliest Finish Time** greedy heuristic:

1. **Sort** all intervals by their finish time (ascending).
2. **Iterate** through the sorted list and greedily pick an interval if it
   starts at or after the end time of the previously selected interval.

**Why does this work?**  
By always choosing the interval that ends the soonest, we leave the maximum
amount of "free time" available for future intervals, which can only increase
(or at worst maintain) the total number of intervals we can fit in.

---

## Project Structure

```
interval-scheduling-greedy/
├── interval_scheduler.py   # Core algorithm implementation
├── main.py                 # Entry point with a sample dataset
└── README.md               # This file
```

---

## Example Input

```python
intervals = [
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (3, 9),
    (5, 9),
    (6, 10),
    (8, 11),
    (8, 12),
    (2, 14),
    (12, 16),
]
```

---

## Example Output

```
=============================================
  Interval Scheduling – Greedy Algorithm
=============================================

All intervals (start, end):
  (1, 4)
  (3, 5)
  (0, 6)
  (5, 7)
  (3, 9)
  (5, 9)
  (6, 10)
  (8, 11)
  (8, 12)
  (2, 14)
  (12, 16)

Maximum non-overlapping intervals selected: 4

Chosen schedule:
  1. (1, 4)
  2. (5, 7)
  3. (8, 11)
  4. (12, 16)

=============================================
```

---

## How to Run

```bash
python main.py
```

---

## Time Complexity Analysis

| Step | Operation | Complexity |
|------|-----------|-----------|
| 1 | Sort intervals by finish time | O(n log n) |
| 2 | Single pass to select intervals | O(n) |
| **Total** | | **O(n log n)** |

The bottleneck is the sorting step.  The selection pass is a single linear
scan through the sorted list.

---

## Space Complexity Analysis

| Storage | Complexity |
|---------|-----------|
| Sorted copy of input | O(n) |
| Output list of selected intervals | O(n) |
| **Total** | **O(n)** |

We store a sorted copy of the input and collect the selected intervals, both
of which are at most the size of the input.
