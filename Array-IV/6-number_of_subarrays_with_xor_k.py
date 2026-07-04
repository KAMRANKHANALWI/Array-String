# ============================================================
# NUMBER OF SUBARRAYS WITH XOR K
# ============================================================
#
# Problem:
#
# Given an array
# and an integer K,
#
# count the number
# of subarrays whose
# XOR equals K.
#
#
# Example:
#
# arr = [4,2,2,6,4]
#
# K = 6
#
#
# Answer:
#
# 4
#
#
# Valid Subarrays:
#
# [4,2]
#
# [2,2,6]
#
# [6]
#
# [4,2,2,6,4]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# This problem looks very
# similar to:
#
# Longest Subarray Sum K.
#
#
# The only difference is:
#
# Prefix Sum
#
# becomes
#
# Prefix XOR.
#
#
# Prefix Sum Formula:
#
# prefix_sum - K
#
#
# Prefix XOR Formula:
#
# prefix_xor ^ K
#
#
# Therefore,
#
# the entire solution
# becomes almost identical.
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
# calculate XOR
# from scratch.
#
#
# If:
#
# XOR == K
#
# increase answer.
#
#
# TIME  : O(N³)
#
# SPACE : O(1)
#
# ============================================================

def subarray_xor_brute(arr, k):

    n = len(arr)

    count = 0

    for start in range(n):

        for end in range(start, n):

            current_xor = 0

            for index in range(start, end + 1):

                current_xor ^= arr[index]

            if current_xor == k:

                count += 1

    return count


# ============================================================
# 2. BETTER APPROACH
# ============================================================
#
# IDEA:
#
# Instead of
# recalculating XOR,
#
# maintain a
# running XOR.
#
#
# running_xor
#
# ^=
#
# arr[end]
#
#
# If:
#
# running_xor == K
#
# increase answer.
#
#
# TIME  : O(N²)
#
# SPACE : O(1)
#
# ============================================================

def subarray_xor_better(arr, k):

    n = len(arr)

    count = 0

    for start in range(n):

        running_xor = 0

        for end in range(start, n):

            running_xor ^= arr[end]

            if running_xor == k:

                count += 1

    return count


# ============================================================
# 3. OPTIMAL
# (PREFIX XOR + HASH MAP)
# ============================================================
#
# IDEA:
#
# Maintain:
#
# prefix_xor
#
#
# Formula:
#
# required_prefix =
#
# prefix_xor ^ K
#
#
# If required_prefix
# already exists,
#
# then every previous
# occurrence forms
# one valid subarray.
#
#
# Therefore,
#
# store the
# FREQUENCY
# of every
# Prefix XOR.
#
#
# NOTE:
#
# This problem asks
# for COUNT.
#
# Therefore,
#
# store frequency.
#
#
# (Unlike Prefix Sum
# Longest Subarray,
#
# where we stored
# the FIRST occurrence.)
#
#
# TIME  : O(N)
#
# SPACE : O(N)
#
# ============================================================

def subarray_xor_optimal(arr, k):

    prefix_xor = 0

    count = 0

    frequency = {

        0: 1

    }

    for num in arr:

        prefix_xor ^= num

        required_prefix = (

            prefix_xor ^ k

        )

        # Every previous occurrence
        # of required_prefix forms
        # one valid subarray ending
        # at the current index.
        #
        # Therefore,
        # we add its FREQUENCY
        # instead of just 1.

        if required_prefix in frequency:

            count += frequency[

                required_prefix

            ]

        frequency[prefix_xor] = (

            frequency.get(

                prefix_xor,

                0

            )

            + 1

        )

    return count


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [4,2,2,6,4]
#
#
# K = 6
#
#
# Initially:
#
# prefix_xor = 0
#
# frequency = {0:1}
#
#
# ---------------------------------
#
# 4
#
# prefix_xor = 4
#
# Need:
#
# 4 ^ 6 = 2
#
# Not found.
#
#
# frequency:
#
# {0:1,4:1}
#
#
# ---------------------------------
#
# 2
#
# prefix_xor = 6
#
# Need:
#
# 6 ^ 6 = 0
#
# Found.
#
#
# Count = 1
#
#
# frequency:
#
# {0:1,4:1,6:1}
#
#
# ---------------------------------
#
# 2
#
# prefix_xor = 4
#
# Need:
#
# 4 ^ 6 = 2
#
# Not found.
#
#
# frequency:
#
# {0:1,4:2,6:1}
#
#
# ---------------------------------
#
# 6
#
# prefix_xor = 2
#
# Need:
#
# 2 ^ 6 = 4
#
# Found.
#
#
# Frequency of 4
#
# is 2.
#
#
# Therefore:
#
# Count += 2
#
#
# Count = 3
#
#
# ---------------------------------
#
# 4
#
# prefix_xor = 6
#
# Need:
#
# 6 ^ 6 = 0
#
# Found.
#
#
# Count = 4
#
#
# Final Answer:
#
# 4
#
# ============================================================
# DRIVER CODE
# ============================================================

arr = [4, 2, 2, 6, 4]

k = 6

print("================================================")
print("INPUT ARRAY")
print("================================================")

print("Array =", arr)
print("K     =", k)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Number of Subarrays =",
    subarray_xor_brute(arr, k)
)

print()

print("================================================")
print("2. BETTER APPROACH")
print("================================================")

print(
    "Number of Subarrays =",
    subarray_xor_better(arr, k)
)

print()

print("================================================")
print("3. OPTIMAL (PREFIX XOR + HASH MAP)")
print("================================================")

print(
    "Number of Subarrays =",
    subarray_xor_optimal(arr, k)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [5, 6, 7, 8, 9]

k2 = 5

print("Array =", arr2)
print("K     =", k2)

print()

print(
    "Number of Subarrays =",
    subarray_xor_optimal(arr2, k2)
)

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

arr3 = [1, 1, 1, 1]

k3 = 0

print("Array =", arr3)
print("K     =", k3)

print()

print(
    "Number of Subarrays =",
    subarray_xor_optimal(arr3, k3)
)

print()

print("================================================")
print("NO VALID SUBARRAY")
print("================================================")

arr4 = [2, 4, 8]

k4 = 10

print("Array =", arr4)
print("K     =", k4)

print()

print(
    "Number of Subarrays =",
    subarray_xor_optimal(arr4, k4)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force")
print("Time  : O(N³)")
print("Space : O(1)")

print()

print("Better (Running XOR)")
print("Time  : O(N²)")
print("Space : O(1)")

print()

print("Optimal (Prefix XOR + Hash Map)")
print("Time  : O(N)")
print("Space : O(N)")

print()

print("================================================")
print("INTERVIEW NOTES")
print("================================================")

print("Brute Force")
print("-> Generate every subarray.")
print("-> Calculate XOR from scratch.")

print()

print("Better")
print("-> Generate every subarray.")
print("-> Maintain a Running XOR.")
print("-> Avoid recalculating XOR.")

print()

print("Optimal")
print("-> Maintain Prefix XOR.")
print("-> Compute:")
print("   required_prefix = prefix_xor ^ K")
print("-> If required_prefix already")
print("   exists, every occurrence")
print("   contributes one valid subarray.")
print("-> Store the FREQUENCY of")
print("   every Prefix XOR.")

print()

print("================================================")
print("PREFIX SUM vs PREFIX XOR")
print("================================================")

print("Longest Subarray Sum K")
print("↓")
print("Store FIRST occurrence")
print("of every Prefix Sum.")
print("Reason:")
print("Longest Length")

print()

print("Subarrays with XOR K")
print("↓")
print("Store FREQUENCY")
print("of every Prefix XOR.")
print("Reason:")
print("Count ALL subarrays.")

print()

print("================================================")
print("MEMORY TRICK")
print("================================================")

print("Prefix Sum")
print("↓")
print("remaining =")
print("prefix_sum - K")

print()

print("Prefix XOR")
print("↓")
print("required =")
print("prefix_xor ^ K")

print()

print("Golden Formula")
print()

print("required_prefix =")
print("prefix_xor ^ K")

print()

print("If required_prefix")
print("already exists,")
print("every previous")
print("occurrence creates")
print("one more valid")
print("subarray.")

print()

print("Golden Rule")
print()

print("Need LONGEST?")
print("↓")
print("Store FIRST occurrence.")

print()

print("Need COUNT?")
print("↓")
print("Store FREQUENCY.")