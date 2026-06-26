# ============================================================
# MAJORITY ELEMENT
# (Moore's Voting Algorithm)
# ============================================================
#
# Problem:
#
# Given an array,
# find the element that appears
# more than n/2 times.
#
#
# It is guaranteed that
# exactly one majority element exists.
#
#
# Example:
#
# arr = [2,2,1,1,1,2,2]
#
#
# Frequency:
#
# 2 -> 4 times
#
# 1 -> 3 times
#
#
# Since:
#
# 4 > 7/2
#
# Answer:
#
# 2
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# A majority element appears
# more than n/2 times.
#
#
# Therefore:
#
# There can be only ONE
# majority element.
#
#
# Why?
#
# Suppose:
#
# n = 10
#
# A appears 6 times
#
# B appears 6 times
#
#
# Total becomes:
#
# 12
#
# Impossible.
#
#
# ------------------------------------------------------------
# MOORE'S VOTING INTUITION
# ------------------------------------------------------------
#
# Imagine every occurrence
# of the majority element
# cancels one occurrence
# of every other element.
#
#
# Example:
#
# [2,2,2,1,1]
#
#
# Cancel:
#
# 2 with 1
#
#
# Remaining:
#
# [2,2,1]
#
#
# Cancel again:
#
# 2 with 1
#
#
# Remaining:
#
# [2]
#
#
# The majority element
# can never be completely
# cancelled because it
# appears more than n/2 times.
#
#
# Therefore:
#
# It always survives as
# the final candidate.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# For every element,
# count its frequency.
#
#
# If frequency > n/2,
#
# return that element.
#
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def majority_element_brute(arr):

    n = len(arr)

    for i in range(n):

        count = 0

        for j in range(n):

            if arr[j] == arr[i]:

                count += 1

        if count > n // 2:

            return arr[i]

    return -1


# ============================================================
# 2. BETTER APPROACH (HASH MAP)
# ============================================================
#
# IDEA:
#
# Store frequency of
# every element.
#
#
# Then return the element
# whose frequency > n/2.
#
#
# TIME  : O(N)
# SPACE : O(N)
#
# ============================================================

def majority_element_better(arr):

    frequency = {}

    for num in arr:

        frequency[num] = (
            frequency.get(num, 0) + 1
        )

    limit = len(arr) // 2

    for key in frequency:

        if frequency[key] > limit:

            return key

    return -1


# ============================================================
# 3. OPTIMAL
# (MOORE'S VOTING ALGORITHM)
# ============================================================
#
# Maintain:
#
# candidate
#
# count
#
#
# RULES:
#
# count == 0
#
# -> Choose current element
#    as new candidate.
#
#
# Same element:
#
# count += 1
#
#
# Different element:
#
# count -= 1
#
#
# The final candidate
# is the majority element.
#
#
# Since LeetCode guarantees
# majority exists,
#
# verification pass
# is optional.
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def majority_element_optimal(arr):

    candidate = None

    count = 0

    for num in arr:

        if count == 0:

            candidate = num
            count = 1

        elif num == candidate:

            count += 1

        else:

            count -= 1

    return candidate


# ============================================================
# EXTRA:
# MOORE'S WITH VERIFICATION
# ============================================================
#
# Useful when majority
# element is NOT guaranteed.
#
#
# First:
#
# Find candidate.
#
#
# Second:
#
# Count frequency.
#
#
# If frequency > n/2:
#
# return candidate
#
#
# Else:
#
# return -1
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def majority_element_with_verification(arr):

    candidate = majority_element_optimal(arr)

    count = 0

    for num in arr:

        if num == candidate:

            count += 1

    if count > len(arr) // 2:

        return candidate

    return -1


# ============================================================
# DRY RUN
# ============================================================
#
# arr = [2,2,1,1,1,2,2]
#
#
# candidate = None
#
# count = 0
#
#
# 2
#
# candidate = 2
#
# count = 1
#
#
# 2
#
# count = 2
#
#
# 1
#
# count = 1
#
#
# 1
#
# count = 0
#
#
# 1
#
# candidate = 1
#
# count = 1
#
#
# 2
#
# count = 0
#
#
# 2
#
# candidate = 2
#
# count = 1
#
#
# Final Candidate:
#
# 2
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

arr = [2, 2, 1, 1, 1, 2, 2]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Majority Element =",
    majority_element_brute(arr)
)

print()

print("================================================")
print("2. BETTER APPROACH (HASH MAP)")
print("================================================")

print(
    "Majority Element =",
    majority_element_better(arr)
)

print()

print("================================================")
print("3. OPTIMAL (MOORE'S VOTING)")
print("================================================")

print(
    "Majority Element =",
    majority_element_optimal(arr)
)

print()

print("================================================")
print("WITHOUT MAJORITY ELEMENT")
print("================================================")

arr2 = [1, 2, 3, 4]

print("Array =", arr2)

print(
    "Result =",
    majority_element_with_verification(arr2)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force -> O(N²), O(1)")
print("Hash Map    -> O(N),  O(N)")
print("Moore Vote  -> O(N),  O(1)")