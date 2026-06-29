# ============================================================
# TWO SUM
# ============================================================
#
# Problem:
#
# Given an array of integers
# and a target value,
#
# determine whether there exists
# a pair whose sum equals the target.
#
#
# There are TWO common interview variations:
#
# ------------------------------------------------------------
# Variation 1
# ------------------------------------------------------------
#
# Return:
#
# YES / NO
#
#
# Example:
#
# arr = [2,7,11,15]
#
# target = 9
#
# Answer:
#
# YES
#
#
# ------------------------------------------------------------
# Variation 2 (LeetCode)
# ------------------------------------------------------------
#
# Return:
#
# Indices of the two numbers.
#
#
# Example:
#
# arr = [2,7,11,15]
#
# target = 9
#
# Answer:
#
# [0,1]
#
# because:
#
# arr[0] + arr[1] = 9
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Instead of asking:
#
# "Which number can I pair
# with the current element?"
#
# Ask:
#
# "What number do I NEED
# to complete the target?"
#
#
# If:
#
# current = x
#
# then
#
# needed = target - x
#
#
# Example:
#
# target = 9
#
# current = 2
#
# needed = 7
#
#
# If 7 has already been seen,
#
# then:
#
# 2 + 7 = 9
#
# Answer found.
#
#
# This observation leads to the
# O(N) Hash Map solution.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Try every possible pair.
#
#
# Example:
#
# [2,7,11,15]
#
#
# Check:
#
# 2 + 7
#
# 2 + 11
#
# 2 + 15
#
# 7 + 11
#
# 7 + 15
#
# 11 + 15
#
#
# If any pair equals target,
#
# return True.
#
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def two_sum_brute(arr, target):

    n = len(arr)

    for i in range(n):

        for j in range(i + 1, n):

            if arr[i] + arr[j] == target:

                return True

    return False


# ============================================================
# 2. BETTER APPROACH (HASH MAP)
# ============================================================
#
# IDEA:
#
# Store every number
# we've already visited.
#
#
# For every element:
#
# needed = target - current
#
#
# If needed already exists
# in the hash map,
#
# we found the answer.
#
#
# IMPORTANT:
#
# This approach also returns
# the ORIGINAL INDICES.
#
#
# Therefore,
#
# this is the optimal solution
# for the LeetCode version.
#
#
# TIME  : O(N)
# SPACE : O(N)
#
# ============================================================

def two_sum_hashmap(arr, target):

    visited = {}

    for index, num in enumerate(arr):

        needed = target - num

        if needed in visited:

            return [
                visited[needed],
                index
            ]

        visited[num] = index

    return []


# ============================================================
# 3. OPTIMAL (SORT + TWO POINTERS)
# ============================================================
#
# Interview Variation:
#
# Return only:
#
# True / False
#
#
# Since indices are NOT required,
#
# we may sort the array.
#
#
# IDEA:
#
# Sort array.
#
#
# Maintain:
#
# left
#
# right
#
#
# If:
#
# current_sum < target
#
# move left++
#
#
# If:
#
# current_sum > target
#
# move right--
#
#
# If equal:
#
# pair found.
#
#
# WHY DOES THIS WORK?
#
# Because after sorting:
#
# Moving left
#
# always increases the sum.
#
#
# Moving right
#
# always decreases the sum.
#
#
# TIME:
#
# Sorting -> O(N log N)
#
# Scan    -> O(N)
#
# Total   -> O(N log N)
#
#
# SPACE : O(1)
#
# ============================================================

def two_sum_two_pointers(arr, target):

    nums = sorted(arr)

    left = 0
    right = len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum == target:

            return True

        elif current_sum < target:

            left += 1

        else:

            right -= 1

    return False


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [2,7,11,15]
#
# target = 9
#
#
# -------------------------
# HASH MAP
# -------------------------
#
# visited = {}
#
#
# Current = 2
#
# Needed = 7
#
# Not found
#
# Store:
#
# {2:0}
#
#
# -------------------------
#
# Current = 7
#
# Needed = 2
#
#
# Already exists.
#
#
# Answer:
#
# [0,1]
#
#
# -------------------------
# TWO POINTER
# -------------------------
#
# Sorted:
#
# [2,7,11,15]
#
#
# left = 2
#
# right = 15
#
# sum = 17
#
# Too large.
#
# Move right.
#
#
# left = 2
#
# right = 11
#
# sum = 13
#
# Still large.
#
# Move right.
#
#
# left = 2
#
# right = 7
#
# sum = 9
#
#
# Pair Found.
#
# ============================================================

# ============================================================
# DRIVER CODE
# ============================================================

arr = [2, 7, 11, 15]
target = 9

print("================================================")
print("INPUT ARRAY")
print("================================================")

print("Array  =", arr)
print("Target =", target)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Pair Exists =",
    two_sum_brute(arr, target)
)

print()

print("================================================")
print("2. BETTER APPROACH (HASH MAP)")
print("================================================")

indices = two_sum_hashmap(arr, target)

if indices:

    print("Indices =", indices)

    print(
        "Values  =",
        arr[indices[0]],
        "+",
        arr[indices[1]],
        "=",
        target
    )

else:

    print("No Pair Found")

print()

print("================================================")
print("3. OPTIMAL (SORT + TWO POINTERS)")
print("================================================")

print(
    "Pair Exists =",
    two_sum_two_pointers(arr, target)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [3, 2, 4]
target2 = 6

print("Array  =", arr2)
print("Target =", target2)

print()

print(
    "Hash Map Indices =",
    two_sum_hashmap(arr2, target2)
)

print(
    "Two Pointer      =",
    two_sum_two_pointers(arr2, target2)
)

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

arr3 = [3, 3]
target3 = 6

print("Array  =", arr3)
print("Target =", target3)

print()

print(
    "Hash Map Indices =",
    two_sum_hashmap(arr3, target3)
)

print(
    "Two Pointer      =",
    two_sum_two_pointers(arr3, target3)
)

print()

print("================================================")
print("NO VALID PAIR")
print("================================================")

arr4 = [1, 2, 3, 4]
target4 = 10

print("Array  =", arr4)
print("Target =", target4)

print()

print(
    "Brute Force =",
    two_sum_brute(arr4, target4)
)

print(
    "Hash Map    =",
    two_sum_hashmap(arr4, target4)
)

print(
    "Two Pointer =",
    two_sum_two_pointers(arr4, target4)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force")
print("Time  : O(N²)")
print("Space : O(1)")

print()

print("Hash Map")
print("Time  : O(N)")
print("Space : O(N)")

print()

print("Two Pointer (Sorted Array)")
print("Time  : O(N log N)")
print("Space : O(1)")

print()

print("================================================")
print("INTERVIEW NOTE")
print("================================================")

print("If only YES/NO is required:")
print("-> Two Pointer is a good solution after sorting.")

print()

print("If ORIGINAL INDICES are required (LeetCode):")
print("-> Hash Map is the optimal solution.")

print()

print("Hash Map is the approach most interviewers expect.")