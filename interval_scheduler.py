def interval_scheduling(intervals):
    """
    Solve the Interval Scheduling Maximization problem using a greedy algorithm.

    Strategy:
        Sort all intervals by their finish (end) time, then greedily select each
        interval that does not overlap with the previously selected one.  This
        approach always yields the maximum number of non-overlapping intervals.

    Parameters
    ----------
    intervals : list of tuple
        Each tuple is (start_time, end_time).

    Returns
    -------
    list of tuple
        The selected non-overlapping intervals in the order they were chosen.
    """

    # Step 1: Sort intervals by finish time (greedy choice).
    # Ties are broken by start time, but the exact tie-breaking does not
    # affect the size of the optimal solution.
    sorted_intervals = sorted(intervals, key=lambda interval: interval[1])

    selected = []          # Intervals chosen for the schedule
    last_finish_time = -1  # Finish time of the most recently selected interval

    # Step 2: Iterate through the sorted intervals and greedily pick each one
    # that starts after (or exactly when) the last chosen interval finishes.
    for start, end in sorted_intervals:
        if start >= last_finish_time:
            # This interval does not overlap with the last selected one — pick it.
            selected.append((start, end))
            last_finish_time = end  # Update the finish time boundary

    return selected
