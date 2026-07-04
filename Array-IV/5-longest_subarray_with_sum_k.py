# ============================================================
# LONGEST SUBARRAY WITH SUM K
# ============================================================
#
# Problem:
#
# Given an array
# and an integer K,
#
# find the LENGTH of the
# longest subarray
# whose sum equals K.
#
#
# Example:
#
# arr = [2,3,5,1,9]
#
# K = 10
#
#
# Answer:
#
# 3
#
#
# Because:
#
# [2,3,5]
#
# sums to 10.
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# The biggest challenge is:
#
# How do we know whether
# a previous subarray
# can combine with the
# current element to
# make sum K?
#
#
# Prefix Sum solves this.
#
#
# Suppose:
#
# prefix_sum
#
# is the sum from
# index 0 to i.
#
#
# If:
#
# prefix_sum - K
#
# already existed earlier,
#
# then the subarray
# between them
# has sum exactly K.
#
#
# Therefore,
#
# maintain:
#
# Prefix Sum
#
# +
#
# Hash Map
#
#
# This gives the
# O(N) solution.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Generate every
# possible subarray.
#
#
# For every subarray,
#
# calculate its sum
# from scratch.
#
#
# If:
#
# sum == K
#
# update answer.
#
#
# TIME  : O(N³)
#
# SPACE : O(1)
#
# ============================================================


def longest_subarray_brute(arr, k):

    n = len(arr)

    longest = 0

    for start in range(n):

        for end in range(start, n):

            current_sum = 0

            for index in range(start, end + 1):

                current_sum += arr[index]

            if current_sum == k:

                longest = max(longest, end - start + 1)

    return longest


# ============================================================
# 2. BETTER APPROACH
# ============================================================
#
# IDEA:
#
# Instead of
# recalculating the sum,
#
# maintain a running sum.
#
#
# Fix:
#
# start
#
#
# Extend:
#
# end
#
#
# running_sum += arr[end]
#
#
# If:
#
# running_sum == K
#
# update answer.
#
#
# TIME  : O(N²)
#
# SPACE : O(1)
#
# ============================================================


def longest_subarray_better(arr, k):

    n = len(arr)

    longest = 0

    for start in range(n):

        running_sum = 0

        for end in range(start, n):

            running_sum += arr[end]

            if running_sum == k:

                longest = max(longest, end - start + 1)

    return longest


# ============================================================
# 3. OPTIMAL
# (PREFIX SUM + HASH MAP)
# ============================================================
#
# IDEA:
#
# Maintain:
#
# prefix_sum
#
#
# Store the FIRST
# occurrence of every
# prefix sum.
#
#
# If:
#
# prefix_sum == K
#
# then
#
# subarray starts
# from index 0.
#
#
# Otherwise,
#
# check whether:
#
# prefix_sum - K
#
# already exists.
#
#
# If yes,
#
# the subarray
# between them
# has sum K.
#
#
# IMPORTANT:
#
# Store only the
# FIRST occurrence
# of every prefix sum.
#
#
# This gives the
# longest subarray.
#
#
# TIME  : O(N)
#
# SPACE : O(N)
#
# ============================================================


def longest_subarray_optimal(arr, k):

    prefix_sum = 0

    longest = 0

    prefix_map = {}

    for index in range(len(arr)):

        prefix_sum += arr[index]

        # Entire prefix itself
        # equals K.

        if prefix_sum == k:

            longest = index + 1

        remaining = prefix_sum - k

        if remaining in prefix_map:

            longest = max(longest, index - prefix_map[remaining])

        # Store only the
        # first occurrence.

        if prefix_sum not in prefix_map:

            prefix_map[prefix_sum] = index

    return longest


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [10,5,2,7,1,9]
#
#
# K = 15
#
#
# Prefix Sum:
#
# 10
#
# 15
#
# 17
#
# 24
#
# 25
#
# 34
#
#
# Current:
#
# prefix = 24
#
#
# Need:
#
# 24 - 15
#
# =
#
# 9
#
#
# 9 is not present.
#
#
# Next:
#
# prefix = 25
#
#
# Need:
#
# 10
#
#
# 10 exists
#
# at index 0.
#
#
# Therefore:
#
# subarray:
#
# [5,2,7,1]
#
#
# Length:
#
# 4
#
#
# Longest = 4
#
# ============================================================
# DRIVER CODE
# ============================================================

arr = [10, 5, 2, 7, 1, 9]

k = 15

print("================================================")
print("INPUT ARRAY")
print("================================================")

print("Array =", arr)
print("K     =", k)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print("Longest Length =", longest_subarray_brute(arr, k))

print()

print("================================================")
print("2. BETTER APPROACH")
print("================================================")

print("Longest Length =", longest_subarray_better(arr, k))

print()

print("================================================")
print("3. OPTIMAL (PREFIX SUM + HASH MAP)")
print("================================================")

print("Longest Length =", longest_subarray_optimal(arr, k))

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [2, 3, 5, 1, 9]

k2 = 10

print("Array =", arr2)
print("K     =", k2)

print()

print("Longest Length =", longest_subarray_optimal(arr2, k2))

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

arr3 = [1, 2, 3, 1, 1, 1, 1]

k3 = 3

print("Array =", arr3)
print("K     =", k3)

print()

print("Longest Length =", longest_subarray_optimal(arr3, k3))

print()

print("================================================")
print("NO SUBARRAY FOUND")
print("================================================")

arr4 = [5, 6, 7]

k4 = 100

print("Array =", arr4)
print("K     =", k4)

print()

print("Longest Length =", longest_subarray_optimal(arr4, k4))

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force")
print("Time  : O(N³)")
print("Space : O(1)")

print()

print("Better (Running Sum)")
print("Time  : O(N²)")
print("Space : O(1)")

print()

print("Optimal (Prefix Sum + Hash Map)")
print("Time  : O(N)")
print("Space : O(N)")

print()

print("================================================")
print("INTERVIEW NOTES")
print("================================================")

print("Brute Force")
print("-> Generate every subarray.")
print("-> Calculate its sum from scratch.")

print()

print("Better")
print("-> Generate every subarray.")
print("-> Maintain a running sum.")
print("-> Avoid recalculating the sum.")

print()

print("Optimal")
print("-> Maintain Prefix Sum.")
print("-> Store the FIRST occurrence")
print("   of every Prefix Sum.")
print("-> If (prefix_sum - K) exists,")
print("   a valid subarray is found.")
print("-> Always keep the earliest")
print("   occurrence for maximum length.")

print()

print("================================================")
print("MEMORY TRICK")
print("================================================")

print("Brute Force")
print("↓")
print("Generate Every Subarray")
print("↓")
print("Calculate Sum")
print("↓")
print("O(N³)")

print()

print("Better")
print("↓")
print("Generate Every Subarray")
print("↓")
print("Running Sum")
print("↓")
print("O(N²)")

print()

print("Optimal")
print("↓")
print("Prefix Sum")
print("↓")
print("Hash Map")
print("↓")
print("prefix_sum - K")
print("↓")
print("Longest Subarray")

print()

print("Golden Formula")
print()
print("prefix_sum - K")
print()
print("If it already exists,")
print("the subarray between")
print("them has sum K.")

print()

print("Golden Rule")
print()
print("Store only the")
print("FIRST occurrence")
print("of every Prefix Sum.")
print()
print("The earliest occurrence")
print("gives the longest")
print("possible subarray.")


"""
# 1.

Brute
↓
Generate Every Subarray
↓
Calculate Sum
↓
O(N³)

# 2.

Better
↓
Generate Every Subarray
↓
Running Sum
↓
O(N²)

# 3.

Optimal
↓
Prefix Sum
↓
Hash Map
↓
prefix_sum - K
↓
Longest Subarray
↓
O(N)

If prefix_sum - K has already been seen, 
then everything between that previous index and 
the current index must sum to K.

"""
