"""
main.py - Interval Scheduling Greedy Algorithm Demo

Run this file directly to see the greedy interval scheduler in action:
    python main.py
"""

import os
import time

# ---------------------------------------------------------------------------
# Animation settings
# ---------------------------------------------------------------------------
STEP_DELAY = 0.9        # seconds between animation steps
SORT_DELAY = 0.5        # seconds during sorting reveal
TIMELINE_WIDTH = 42     # characters wide for the bar chart
MAX_TIME = 16           # rightmost tick on the timeline

# Width of the label column (derived from the format used in draw_dashboard):
#   "  {idx:2}. ({start:2},{end:2}) │"  →  2+2+3+2+1+2+3 = 15 display columns
_LABEL_COLS = len(f"  {12:2}. ({16:2},{16:2}) \u2502")  # 15

# ANSI colour codes (fall back gracefully on terminals that don't support them)
GREEN  = '\033[92m'
RED    = '\033[91m'
YELLOW = '\033[93m'
CYAN   = '\033[96m'
BOLD   = '\033[1m'
DIM    = '\033[2m'
RESET  = '\033[0m'

# ---------------------------------------------------------------------------
# Sample dataset: 12 intervals (start_time, end_time)
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


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def _bar(start, end, color, char):
    """Return a coloured ASCII bar for one interval on the timeline."""
    scale = TIMELINE_WIDTH / MAX_TIME
    b_start = round(start * scale)
    b_end   = round(end   * scale)
    length  = max(1, b_end - b_start)
    return " " * b_start + color + char * length + RESET


def _time_ruler():
    """Return the two-line time ruler string."""
    scale = TIMELINE_WIDTH / MAX_TIME
    numbers = "        "
    ticks   = "        "
    for i in range(TIMELINE_WIDTH + 1):
        t = i / scale
        rt = round(t)
        if abs(t - rt) < 0.01 and rt % 4 == 0:
            label = str(rt)
            numbers += label
            ticks   += "+"
            # pad so next character lines up
            numbers += " " * (len(label) - 1)
            ticks   += "-" * (len(label) - 1)
        elif abs(t - rt) < 0.01 and rt % 2 == 0:
            numbers += ":"
            ticks   += "|"
        else:
            numbers += " "
            ticks   += "-"
    return numbers + "\n" + ticks


def draw_dashboard(display_intervals, selected, rejected, current, last_finish, caption):
    """
    Clear the screen and redraw the full animated dashboard.

    Parameters
    ----------
    display_intervals : list of (start, end)
        Intervals shown in the current order.
    selected : set of (start, end)
        Intervals already confirmed as selected.
    rejected : set of (start, end)
        Intervals already rejected.
    current : (start, end) or None
        Interval currently being examined (highlighted in yellow).
    last_finish : int
        Finish time of the last selected interval (-1 means none yet).
    caption : str
        Status line shown at the bottom.
    """
    clear_screen()
    print(f"{BOLD}{'=' * 52}{RESET}")
    print(f"{BOLD}   Interval Scheduling — Greedy Algorithm{RESET}")
    print(f"{BOLD}{'=' * 52}{RESET}")
    print()
    print(_time_ruler())
    print()

    for idx, (start, end) in enumerate(display_intervals, start=1):
        label = f"  {idx:2}. ({start:2},{end:2}) │"

        if (start, end) in selected:
            bar  = _bar(start, end, GREEN,  "█")
            note = f"  {GREEN}✓ selected{RESET}"
        elif (start, end) in rejected:
            bar  = _bar(start, end, RED + DIM, "░")
            note = f"  {RED}✗ overlaps{RESET}"
        elif (start, end) == current:
            bar  = _bar(start, end, YELLOW, "▓")
            note = f"  {YELLOW}← considering …{RESET}"
        else:
            bar  = _bar(start, end, CYAN + DIM, "▒")
            note = ""

        print(f"{label}{bar}{note}")

    # Last-finish-time marker (indent derived from the label column width)
    if last_finish >= 0:
        scale = TIMELINE_WIDTH / MAX_TIME
        marker_col = round(last_finish * scale)
        indent = " " * (_LABEL_COLS + marker_col)
        print(f"\n{indent}{CYAN}▲  last finish = {last_finish}{RESET}")
    else:
        print()

    print()
    print(f"  {BOLD}► {caption}{RESET}")
    print()


# ---------------------------------------------------------------------------
# Animated greedy walkthrough
# ---------------------------------------------------------------------------

def animate(intervals):
    selected  = set()
    rejected  = set()

    # --- Step 1: Show the raw input ---
    draw_dashboard(intervals, selected, rejected, None, -1,
                   f"Input: {len(intervals)} intervals (unsorted)")
    time.sleep(STEP_DELAY * 1.5)

    # --- Step 2: Sort by finish time ---
    draw_dashboard(intervals, selected, rejected, None, -1,
                   "Sorting by finish time …")
    time.sleep(STEP_DELAY)

    sorted_intervals = sorted(intervals, key=lambda iv: iv[1])

    draw_dashboard(sorted_intervals, selected, rejected, None, -1,
                   "Sorted by finish time — ready to select!")
    time.sleep(STEP_DELAY * 1.5)

    # --- Step 3: Greedy selection ---
    last_finish = -1

    for interval in sorted_intervals:
        start, end = interval

        # Highlight the current candidate
        draw_dashboard(sorted_intervals, selected, rejected, interval,
                       last_finish,
                       f"Considering ({start}, {end})  |  last finish = {last_finish}")
        time.sleep(STEP_DELAY)

        if start >= last_finish:
            selected.add(interval)
            last_finish = end
            draw_dashboard(sorted_intervals, selected, rejected, None,
                           last_finish,
                           f"✓  Selected ({start}, {end})  →  last finish now = {last_finish}")
        else:
            rejected.add(interval)
            draw_dashboard(sorted_intervals, selected, rejected, None,
                           last_finish,
                           f"✗  Rejected ({start}, {end})  — overlaps with last finish {last_finish}")

        time.sleep(STEP_DELAY)

    # --- Step 4: Final result ---
    chosen = sorted(selected, key=lambda iv: iv[1])
    draw_dashboard(sorted_intervals, selected, rejected, None, last_finish,
                   f"Done!  {len(chosen)} non-overlapping intervals selected.")
    time.sleep(STEP_DELAY)

    print(f"  {BOLD}Selected intervals:{RESET}")
    for i, (s, e) in enumerate(chosen, start=1):
        print(f"    {i}. ({s}, {e})")
    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    animate(intervals)
