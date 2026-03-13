"""
main.py

Entry point for the Interval Scheduling Greedy Algorithm demo.

Run with:
    python main.py
"""

from interval_scheduler import schedule_intervals


def main():
    # --- Sample dataset: 11 intervals (start_time, end_time) ---
    # These represent tasks/events that we want to schedule without overlap.
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

    print("=" * 45)
    print("  Interval Scheduling – Greedy Algorithm")
    print("=" * 45)

    # Display all intervals before scheduling
    print("\nAll intervals (start, end):")
    for interval in intervals:
        print(f"  {interval}")

    # Run the greedy scheduling algorithm
    chosen = schedule_intervals(intervals)

    # Display the result
    print(f"\nMaximum non-overlapping intervals selected: {len(chosen)}")
    print("\nChosen schedule:")
    for i, interval in enumerate(chosen, start=1):
        print(f"  {i}. {interval}")

    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()
