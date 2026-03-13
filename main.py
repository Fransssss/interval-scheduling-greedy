"""
main.py

Entry point for the Interval Scheduling Greedy Algorithm demo.

Run with:
    python main.py
"""

from interval_scheduler import schedule_intervals


def main():
    # Sample dataset with 12 intervals (start_time, end_time)
    # These represent tasks or events that we want to schedule without conflicts.
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
    print("  Interval Scheduling — Greedy Algorithm")
    print("=" * 45)

    # Display all input intervals
    print(f"\nAll intervals ({len(intervals)} total):")
    for start, end in intervals:
        print(f"  Start: {start:>2},  End: {end:>2}")

    # Run the greedy scheduling algorithm
    chosen = schedule_intervals(intervals)

    # Display the selected non-overlapping intervals
    print(f"\nSelected non-overlapping intervals ({len(chosen)} chosen):")
    for start, end in chosen:
        print(f"  Start: {start:>2},  End: {end:>2}")

    print("\nMaximum number of non-overlapping intervals:", len(chosen))
    print("=" * 45)


if __name__ == "__main__":
    main()
