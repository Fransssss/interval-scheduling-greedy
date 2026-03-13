"""
main.py - Interval Scheduling Greedy Algorithm Demo

Run this file directly to see the greedy interval scheduler in action:
    python main.py
"""

from interval_scheduler import interval_scheduling

# ---------------------------------------------------------------------------
# Sample dataset: 12 intervals (start_time, end_time)
# These represent tasks / events that need a shared resource (e.g. a lecture
# hall). The goal is to schedule as many non-overlapping events as possible.
# ---------------------------------------------------------------------------
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
    (10, 15),
]

print("=" * 45)
print("   Interval Scheduling - Greedy Algorithm")
print("=" * 45)

# Display the full list of input intervals
print(f"\nTotal intervals provided: {len(intervals)}")
print("\nAll intervals (start, end):")
for i, (start, end) in enumerate(intervals, start=1):
    print(f"  {i:2}. ({start}, {end})")

# Run the greedy scheduler
chosen = interval_scheduling(intervals)

# Display the result
print(f"\nSelected non-overlapping intervals ({len(chosen)} chosen):")
for i, (start, end) in enumerate(chosen, start=1):
    print(f"  {i}. ({start}, {end})")

print("\nDone.")
