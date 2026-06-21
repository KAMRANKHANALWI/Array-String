# ============================================================
# FIND THE DUPLICATE NUMBER
# ============================================================
#
# Problem:
#
# Given an array of size:
#
# N + 1
#
# containing numbers from:
#
# 1 to N
#
# There is exactly one duplicate number.
#
# Return the duplicate.
#
#
# Example:
#
# nums = [1,3,4,2,2]
#
# Output:
#
# 2
#
#
# Example:
#
# nums = [3,1,3,4,2]
#
# Output:
#
# 3
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Constraints:
#
# Array Size:
#
# N + 1
#
# Values:
#
# 1 to N
#
#
# By Pigeonhole Principle:
#
# At least one number must repeat.
#
#
# The magical observation:
#
# Treat:
#
# index -> node
#
# value -> next pointer
#
#
# Example:
#
# nums = [1,3,4,2,2]
#
#
# 0 -> 1
# 1 -> 3
# 3 -> 2
# 2 -> 4
# 4 -> 2
#
#
# Which creates:
#
# 0
# |
# v
# 1 -> 3 -> 2 -> 4
#           ^    |
#           |____|
#
#
# A cycle appears.
#
#
# IMPORTANT:
#
# Duplicate Number
#
# =
#
# Entrance of Cycle
#
#
# Therefore:
#
# Find Duplicate Number
#
# becomes
#
# Find Cycle Entrance
#
#
# This is exactly:
#
# Floyd's Cycle Detection Algorithm
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# For every element,
# count how many times it appears.
#
# If count > 1:
#
# return that element.
#
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def find_duplicate_brute(nums):

    n = len(nums)

    for i in range(n):

        count = 0

        for j in range(n):

            if nums[j] == nums[i]:

                count += 1

        if count > 1:

            return nums[i]

    return -1


# ============================================================
# 2. BETTER APPROACH (HASHING)
# ============================================================
#
# IDEA:
#
# Maintain a set.
#
# If element already exists:
#
# return it.
#
#
# Example:
#
# 1 -> insert
# 3 -> insert
# 4 -> insert
# 2 -> insert
# 2 -> already exists
#
# Answer = 2
#
#
# TIME  : O(N)
# SPACE : O(N)
#
# ============================================================

def find_duplicate_better(nums):

    seen = set()

    for num in nums:

        if num in seen:

            return num

        seen.add(num)

    return -1


# ============================================================
# 3. OPTIMAL APPROACH
#    (FLOYD'S CYCLE DETECTION)
# ============================================================
#
# IDEA:
#
# Treat array as a linked list.
#
#
# PHASE 1:
#
# Find meeting point
# inside the cycle.
#
#
# slow moves:
#
# 1 step
#
#
# fast moves:
#
# 2 steps
#
#
# Eventually:
#
# slow == fast
#
#
# PHASE 2:
#
# Move one pointer back
# to the beginning.
#
#
# Move both pointers
# one step at a time.
#
#
# The point where they meet:
#
# Cycle Entrance
#
# =
#
# Duplicate Number
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def find_duplicate_optimal(nums):

    # ========================================================
    # PHASE 1
    #
    # Find meeting point
    # ========================================================

    slow = nums[0]
    fast = nums[0]

    while True:

        slow = nums[slow]

        fast = nums[nums[fast]]

        if slow == fast:

            break

    # ========================================================
    # PHASE 2
    #
    # Find cycle entrance
    # ========================================================

    slow = nums[0]

    while slow != fast:

        slow = nums[slow]

        fast = nums[fast]

    return slow


# ============================================================
# EXTRA VISUALIZATION
# ============================================================
#
# nums = [1,3,4,2,2]
#
#
# Index:
#
# 0  1  2  3  4
#
#
# Value:
#
# 1  3  4  2  2
#
#
# Links:
#
# 0 -> 1
# 1 -> 3
# 3 -> 2
# 2 -> 4
# 4 -> 2
#
#
# Cycle:
#
# 2 -> 4 -> 2
#
#
# Cycle Entrance:
#
# 2
#
#
# Duplicate:
#
# 2
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

nums = [1, 3, 4, 2, 2]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(nums)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Duplicate =",
    find_duplicate_brute(nums)
)

print()

print("================================================")
print("2. BETTER APPROACH (HASHING)")
print("================================================")

print(
    "Duplicate =",
    find_duplicate_better(nums)
)

print()

print("================================================")
print("3. OPTIMAL (FLOYD'S CYCLE DETECTION)")
print("================================================")

print(
    "Duplicate =",
    find_duplicate_optimal(nums)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

nums2 = [3, 1, 3, 4, 2]

print("Input     =", nums2)

print(
    "Duplicate =",
    find_duplicate_optimal(nums2)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute   -> O(N²), O(1)")
print("Better  -> O(N),  O(N)")
print("Optimal -> O(N),  O(1)")