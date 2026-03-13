"""
interval_scheduler.py

Implements the Interval Scheduling Maximization problem using a Greedy Algorithm.

The goal is to select the maximum number of non-overlapping intervals from a
given list of (start_time, end_time) pairs.

Greedy Strategy:
    Always pick the interval with the earliest finish time that does not
    overlap with the previously selected interval. This locally optimal
    choice leads to a globally optimal solution.

Time Complexity:  O(n log n) — dominated by sorting the intervals
Space Complexity: O(n) — storing the sorted list and the result list
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
        The selected non-overlapping intervals in the order they were chosen.
    """
    if not intervals:
        return []

    # Step 1: Sort all intervals by their finish time (earliest finish first).
    # This is the key greedy decision: by always choosing the interval that
    # ends the soonest, we leave as much room as possible for future intervals.
    sorted_intervals = sorted(intervals, key=lambda interval: interval[1])

    # Step 2: Always select the first interval (it has the earliest finish time).
    selected = [sorted_intervals[0]]

    # Step 3: Iterate through the remaining intervals.
    for current in sorted_intervals[1:]:
        # The last interval we added to our schedule
        last_selected = selected[-1]

        # Step 4: Check if the current interval overlaps with the last selected one.
        # Two intervals overlap if the current one starts before the last one ends.
        # If they do NOT overlap, we can safely add the current interval.
        if current[0] >= last_selected[1]:
            selected.append(current)

    return selected
