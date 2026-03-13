# Interval Scheduling - Greedy Algorithm

## Problem Description

The **Interval Scheduling Maximization** problem asks:

> Given a set of intervals (each with a start time and an end time), select the **largest** possible subset of non-overlapping intervals.

Two intervals overlap when one starts before the other finishes.  
A common real-world example is booking as many events as possible in a single lecture hall.

---

## Video Demo

<video src="IntervalScheduling.mp4" controls width="700">
  Your browser does not support the video tag.
</video>

> **Note:** If the video does not display above, you can view it directly in the repository: [IntervalScheduling.mp4](IntervalScheduling.mp4)

---

## Greedy Strategy

The algorithm uses the **Earliest Finish Time** greedy rule:

1. **Sort** all intervals by their finish (end) time in ascending order.
2. **Iterate** through the sorted list. For each interval:
   - If its start time is ≥ the finish time of the last selected interval, **select it** and update the finish-time boundary.
   - Otherwise, **skip it** (it overlaps with the last selected interval).

### Why does this work?

By always choosing the interval that ends earliest, we leave the maximum possible remaining time for future intervals. This local greedy choice leads to a globally optimal solution — a fact that can be proved by an exchange argument.

---

## Project Structure

```
interval-scheduling-greedy/
├── interval_scheduler.py   # Core algorithm
├── main.py                 # Demo script with sample data
└── README.md
```

---

## Example Input

```
Intervals (start, end):
 1. (1,  4)
 2. (3,  5)
 3. (0,  6)
 4. (5,  7)
 5. (3,  9)
 6. (5,  9)
 7. (6, 10)
 8. (8, 11)
 9. (8, 12)
10. (2, 14)
11. (12, 16)
12. (10, 15)
```

## Example Output

```
=============================================
   Interval Scheduling – Greedy Algorithm
=============================================

Total intervals provided: 12

All intervals (start, end):
    1. (1, 4)
    2. (3, 5)
    3. (0, 6)
    4. (5, 7)
    5. (3, 9)
    6. (5, 9)
    7. (6, 10)
    8. (8, 11)
    9. (8, 12)
   10. (2, 14)
   11. (12, 16)
   12. (10, 15)

Selected non-overlapping intervals (4 chosen):
  1. (1, 4)
  2. (5, 7)
  3. (8, 11)
  4. (12, 16)

Done.
```

---

## Running the Program

```bash
python main.py
```

---

## Complexity Analysis

### Time Complexity

| Step | Cost |
|------|------|
| Sorting by finish time | O(n log n) |
| Single linear scan | O(n) |
| **Total** | **O(n log n)** |

The dominant cost is sorting. After that the selection loop visits each interval exactly once.

### Space Complexity

| Storage | Cost |
|---------|------|
| Sorted copy of input | O(n) |
| Output list (≤ n intervals) | O(n) |
| **Total** | **O(n)** |

All extra memory scales linearly with the number of intervals.
