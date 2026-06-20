# ============================================================
# MERGE OVERLAPPING INTERVALS
# ============================================================
#
# Problem:
#
# Given a collection of intervals:
#
# [start, end]
#
# merge all overlapping intervals.
#
#
# Example:
#
# Input:
#
# [
#   [1,3],
#   [2,6],
#   [8,10],
#   [15,18]
# ]
#
#
# Output:
#
# [
#   [1,6],
#   [8,10],
#   [15,18]
# ]
#
# Because:
#
# [1,3] and [2,6]
#
# overlap and become:
#
# [1,6]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Two intervals overlap if:
#
# current_start <= previous_end
#
#
# Example:
#
# [1,5]
# [3,7]
#
# Since:
#
# 3 <= 5
#
# overlap exists.
#
#
# Merged Interval:
#
# start = min(starts)
# end   = max(ends)
#
#
# Therefore:
#
# [1,5]
# [3,7]
#
# becomes:
#
# [1,7]
#
#
# IMPORTANT:
#
# Before checking overlaps,
# sort intervals by starting time.
#
# After sorting:
#
# all potential overlaps become adjacent.
#
# Then one linear scan is enough.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Sort intervals.
#
# For every interval:
#
# keep extending its ending point
# by checking future intervals.
#
# This causes repeated work.
#
#
# Example:
#
# [1,3]
# [2,6]
# [4,8]
#
#
# [1,3] checks:
#
# [2,6]
# [4,8]
#
#
# Later:
#
# [2,6]
#
# again checks:
#
# [4,8]
#
#
# Repeated computations.
#
#
# TIME  : O(N²)
# SPACE : O(N)
#
# ============================================================

def merge_intervals_brute(intervals):

    intervals.sort()

    merged = []

    n = len(intervals)

    for i in range(n):

        start = intervals[i][0]
        end = intervals[i][1]

        # Interval already covered
        if merged and end <= merged[-1][1]:
            continue

        for j in range(i + 1, n):

            if intervals[j][0] <= end:

                end = max(
                    end,
                    intervals[j][1]
                )

            else:
                break

        merged.append([start, end])

    return merged


# ============================================================
# 2. OPTIMAL APPROACH
# ============================================================
#
# IDEA:
#
# Step 1:
# Sort intervals by start time.
#
#
# Step 2:
#
# Keep the first interval
# inside the answer.
#
#
# Step 3:
#
# Compare current interval with
# the LAST merged interval.
#
#
# If:
#
# current_start <= previous_end
#
# merge them.
#
#
# Else:
#
# start a new interval.
#
#
# WHY ONLY LAST INTERVAL?
#
# After sorting:
#
# if overlap exists,
# it can only happen with the
# most recently merged interval.
#
#
# TIME:
#
# Sorting  -> O(N log N)
# Traversal -> O(N)
#
# Total:
#
# O(N log N)
#
#
# SPACE:
#
# O(N)
#
# ============================================================

def merge_intervals_optimal(intervals):

    intervals.sort()

    merged = [intervals[0]]

    for current_start, current_end in intervals[1:]:

        last_start, last_end = merged[-1]

        # Overlap exists
        if current_start <= last_end:

            merged[-1][1] = max(
                last_end,
                current_end
            )

        else:

            merged.append(
                [current_start, current_end]
            )

    return merged


# ============================================================
# PRECISE TC ANALYSIS
# ============================================================
#
# BRUTE:
#
# Sorting       -> O(N log N)
# Nested Scan   -> O(N²)
#
# Total:
#
# O(N²)
#
#
# OPTIMAL:
#
# Sorting       -> O(N log N)
# One Traversal -> O(N)
#
# Total:
#
# O(N log N + N)
#
# = O(N log N)
#
# because:
#
# N log N dominates N
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

intervals1 = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]

intervals2 = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]

print("================================================")
print("INPUT INTERVALS")
print("================================================")

print(intervals1)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

result_brute = merge_intervals_brute(intervals1)

print(result_brute)

print()

print("================================================")
print("2. OPTIMAL APPROACH")
print("================================================")

result_optimal = merge_intervals_optimal(intervals2)

print(result_optimal)

print()

print("================================================")
print("OVERLAPPING CHAIN TEST")
print("================================================")

chain_intervals = [
    [1, 3],
    [2, 6],
    [4, 8],
    [8, 10]
]

print("Input :")
print(chain_intervals)

print()

print("Output :")
print(
    merge_intervals_optimal(
        chain_intervals
    )
)

print()

print("================================================")
print("NON-OVERLAPPING TEST")
print("================================================")

non_overlapping = [
    [1, 2],
    [5, 6],
    [8, 10]
]

print("Input :")
print(non_overlapping)

print()

print("Output :")
print(
    merge_intervals_optimal(
        non_overlapping
    )
)

"""
NOTE: Merge Intervals Pattern

1. Sort intervals by start time

2. Compare with last merged interval

If:
current_start <= previous_end

→ Merge

Else

→ Add new interval

TC:
O(N log N)

This exact pattern appears in:
- Insert Interval
- Meeting Rooms
- Calendar Problems
- Employee Free Time
"""
