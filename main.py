def interval_scheduling(intervals):
    """
    Greedy interval scheduling algorithm (Earliest Deadline First).

    Given a list of intervals (start, end), returns the maximum set of
    non-overlapping intervals.

    Args:
        intervals: list of (start, end) tuples

    Returns:
        List of selected non-overlapping intervals
    """
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    selected = [sorted_intervals[0]]
    last_end = sorted_intervals[0][1]

    for start, end in sorted_intervals[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


if __name__ == "__main__":
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    result = interval_scheduling(intervals)
    print("Selected intervals:", result)
    print("Total intervals selected:", len(result))
