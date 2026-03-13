"""
interval_scheduler.py

Implements the Interval Scheduling Maximization problem using a Greedy Algorithm.

Problem:
    Given a list of intervals, each defined by a (start_time, end_time) pair,
    select the maximum number of non-overlapping intervals.

Greedy Strategy:
    Always pick the interval that finishes the earliest among those that
    are compatible with the previously selected interval.  This leaves as
    much room as possible for subsequent intervals.

Time Complexity:  O(n log n)  – dominated by the sorting step
Space Complexity: O(n)        – for storing the selected intervals
"""


def schedule_intervals(intervals):
    """
    Select the maximum set of non-overlapping intervals.

    Parameters
    ----------
    intervals : list of tuple
        Each tuple is (start_time, end_time) where start_time < end_time.

    Returns
    -------
    list of tuple
        The chosen non-overlapping intervals in the order they were selected.
    """

    # --- Step 1: Sort intervals by their finish time (earliest finish first) ---
    # This is the key insight of the greedy approach: by always choosing the
    # interval that ends the soonest, we leave the maximum amount of time
    # available for future intervals.
    sorted_intervals = sorted(intervals, key=lambda interval: interval[1])

    # --- Step 2: Greedily select compatible intervals ---
    selected = []

    # Keep track of when the last selected interval ends.
    # Initialise to negative infinity so the first interval is always accepted.
    last_end_time = float("-inf")

    for start, end in sorted_intervals:
        # An interval is compatible if it starts at or after the end of the
        # last selected interval (i.e. they do not overlap).
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end  # update the end time of the last selected interval

    return selected
