# interval-scheduling-greedy

A Python greedy algorithm that selects the maximum set of non-overlapping intervals from a given list using the Earliest Deadline First strategy.

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