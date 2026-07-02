# ============================================================
# LONGEST CONSECUTIVE SEQUENCE
# ============================================================
#
# Problem:
#
# Given an unsorted array,
#
# find the length of the
# longest consecutive sequence.
#
#
# Consecutive means:
#
# 1 2 3 4 5
#
# NOT
#
# 1 3 5
#
#
# Example:
#
# arr = [100,4,200,1,3,2]
#
# Answer:
#
# 4
#
# Because:
#
# 1 2 3 4
#
# is the longest sequence.
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# We only want to start
# counting from the FIRST
# element of a sequence.
#
#
# Example:
#
# 1 2 3 4
#
#
# Start from:
#
# 1 ✓
#
#
# Don't start from:
#
# 2
# 3
# 4
#
#
# How do we know whether
# a number is the FIRST?
#
#
# Simply check:
#
# Does (num - 1) exist?
#
#
# If YES
#
# current number is NOT
# the beginning.
#
#
# If NO
#
# current number IS the
# beginning of a sequence.
#
#
# This observation leads
# to the O(N) Hash Set
# solution.
#
# ============================================================


# ============================================================
# HELPER FUNCTION
# ============================================================
#
# Used by Brute Force.
#
# Searches whether
# a number exists
# inside the array.
#
#
# TIME : O(N)
#
# ============================================================

def linear_search(arr, target):

    for num in arr:

        if num == target:

            return True

    return False


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# For every element,
#
# keep searching for:
#
# current + 1
#
# current + 2
#
# current + 3
#
# ...
#
#
# using Linear Search.
#
#
# TIME  : O(N²)
#
# SPACE : O(1)
#
# ============================================================

def longest_consecutive_brute(arr):

    longest = 0

    for num in arr:

        current = num

        length = 1

        while linear_search(arr, current + 1):

            current += 1

            length += 1

        longest = max(

            longest,
            length

        )

    return longest


# ============================================================
# 2. BETTER APPROACH
# ============================================================
#
# IDEA:
#
# Sort the array.
#
#
# Consecutive numbers
# become neighbours.
#
#
# Traverse once.
#
#
# If:
#
# current == previous + 1
#
# increase length.
#
#
# Ignore duplicates.
#
#
# Otherwise,
#
# start a new sequence.
#
#
# TIME  : O(N log N)
#
# SPACE : O(1)
#
# ============================================================

def longest_consecutive_better(arr):

    if not arr:

        return 0

    arr.sort()

    longest = 1

    current_length = 1

    for i in range(1, len(arr)):

        # Ignore duplicates

        if arr[i] == arr[i - 1]:

            continue

        # Consecutive

        elif arr[i] == arr[i - 1] + 1:

            current_length += 1

        # Start new sequence

        else:

            longest = max(

                longest,
                current_length

            )

            current_length = 1

    longest = max(

        longest,
        current_length

    )

    return longest


# ============================================================
# 3. OPTIMAL (HASH SET)
# ============================================================
#
# IDEA:
#
# Store every element
# inside a Hash Set.
#
#
# Only begin counting
# if:
#
# num - 1
#
# does NOT exist.
#
#
# Then keep extending:
#
# num + 1
#
# num + 2
#
# num + 3
#
#
# Every sequence is
# counted exactly once.
#
#
# TIME  : O(N)
#
# SPACE : O(N)
#
# ============================================================

def longest_consecutive_optimal(arr):

    numbers = set(arr)

    longest = 0

    for num in numbers:

        # Only start from
        # beginning.

        if (num - 1) not in numbers:

            current = num

            length = 1

            while (current + 1) in numbers:

                current += 1

                length += 1

            longest = max(

                longest,
                length

            )

    return longest


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [100,4,200,1,3,2]
#
#
# Hash Set:
#
# {100,4,200,1,3,2}
#
#
# 100
#
# 99 absent
#
# Start.
#
# Length = 1
#
#
# 4
#
# 3 exists
#
# Ignore.
#
#
# 3
#
# 2 exists
#
# Ignore.
#
#
# 2
#
# 1 exists
#
# Ignore.
#
#
# 1
#
# 0 absent
#
# Start.
#
#
# 1
# ↓
# 2
# ↓
# 3
# ↓
# 4
#
# Length = 4
#
#
# Longest = 4
#
# ============================================================
# DRIVER CODE
# ============================================================

arr = [100, 4, 200, 1, 3, 2]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Longest Consecutive Length =",
    longest_consecutive_brute(arr)
)

print()

print("================================================")
print("2. BETTER APPROACH (SORTING)")
print("================================================")

print(
    "Longest Consecutive Length =",
    longest_consecutive_better(arr.copy())
)

print()

print("================================================")
print("3. OPTIMAL (HASH SET)")
print("================================================")

print(
    "Longest Consecutive Length =",
    longest_consecutive_optimal(arr)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

print("Array =", arr2)

print(
    "Longest Consecutive Length =",
    longest_consecutive_optimal(arr2)
)

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

arr3 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

print("Array =", arr3)

print(
    "Longest Consecutive Length =",
    longest_consecutive_optimal(arr3)
)

print()

print("================================================")
print("SINGLE ELEMENT")
print("================================================")

arr4 = [10]

print("Array =", arr4)

print(
    "Longest Consecutive Length =",
    longest_consecutive_optimal(arr4)
)

print()

print("================================================")
print("EMPTY ARRAY")
print("================================================")

arr5 = []

print("Array =", arr5)

print(
    "Longest Consecutive Length =",
    longest_consecutive_optimal(arr5)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force")
print("Time  : O(N²)")
print("Space : O(1)")

print()

print("Better (Sorting)")
print("Time  : O(N log N)")
print("Space : O(1)")

print()

print("Optimal (Hash Set)")
print("Time  : O(N)")
print("Space : O(N)")

print()

print("================================================")
print("INTERVIEW NOTES")
print("================================================")

print("Brute Force")
print("-> Search every next element using Linear Search.")

print()

print("Better")
print("-> Sort the array.")
print("-> Consecutive numbers become neighbours.")
print("-> Traverse once while handling duplicates.")

print()

print("Optimal")
print("-> Store all elements in a Hash Set.")
print("-> Start counting ONLY from the")
print("   beginning of a sequence.")
print("-> A number is the beginning if")
print("   (num - 1) is NOT present.")

print()

print("================================================")
print("MEMORY TRICK")
print("================================================")

print("Brute Force")
print("↓")
print("Linear Search")
print("↓")
print("O(N²)")

print()

print("Better")
print("↓")
print("Sort")
print("↓")
print("Compare Neighbours")
print("↓")
print("O(N log N)")

print()

print("Optimal")
print("↓")
print("Hash Set")
print("↓")
print("Start ONLY from")
print("the FIRST element")
print("of a sequence")
print("↓")
print("Expand Forward")
print("↓")
print("O(N)")

print()

print("Golden Rule")
print("↓")
print("Never start")
print("from the middle.")
print("Start only from")
print("the beginning.")