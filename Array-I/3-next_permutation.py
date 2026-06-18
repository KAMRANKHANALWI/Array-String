# ============================================================
# NEXT PERMUTATION
# ============================================================
#
# Problem:
# --------
#
# Given an array of numbers,
# find the next lexicographically greater permutation.
#
# Example:
#
# [1, 2, 3]
#
# Next Permutation:
#
# [1, 3, 2]
#
#
# Lexicographical Order:
#
# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]
#
#
# The next permutation means:
#
# "The smallest permutation that is
# greater than the current permutation."
#
# ============================================================


# ============================================================
# INTUITION BUILDING
# ============================================================
#
# Consider:
#
# [1, 3, 5, 4, 2]
#
# Look from RIGHT to LEFT.
#
# Suffix:
#
# 5 4 2
#
# Notice:
#
# 5 > 4 > 2
#
# This suffix is already in descending order.
#
#
# IMPORTANT OBSERVATION:
# ----------------------
#
# A descending sequence is already
# the largest possible arrangement
# of those elements.
#
# Therefore:
#
# We cannot generate the next permutation
# by changing only inside this suffix.
#
# We must modify something BEFORE it.
#
#
# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Find the first position from the RIGHT
# where:
#
# arr[i] < arr[i+1]
#
#
# Example:
#
# [1, 3, 5, 4, 2]
#
#          ↑
#
# Moving from right:
#
# 4 > 2
# 5 > 4
#
# Then:
#
# 3 < 5
#
#
# This is called the:
#
# BREAKPOINT
#
# Because this is the first place where
# we can increase the permutation.
#
#
# ============================================================
# WHAT TO DO AFTER FINDING BREAKPOINT?
# ============================================================
#
# Example:
#
# [1, 3, 5, 4, 2]
#     ↑
#
# Breakpoint = 3
#
#
# Elements to the right:
#
# [5, 4, 2]
#
#
# We need:
#
# The smallest element greater than 3.
#
#
# Candidates:
#
# 5
# 4
#
#
# Smallest greater element:
#
# 4
#
#
# Swap:
#
# [1, 4, 5, 3, 2]
#
#
# ============================================================
# WHY REVERSE THE SUFFIX?
# ============================================================
#
# After swapping:
#
# [1, 4, 5, 3, 2]
#
#
# The suffix:
#
# [5, 3, 2]
#
# is still descending.
#
#
# To get the NEXT permutation,
# we need the SMALLEST possible suffix.
#
#
# Smallest arrangement:
#
# [2, 3, 5]
#
#
# Since the suffix is already descending,
# reversing automatically gives:
#
# ascending order.
#
#
# Final Answer:
#
# [1, 4, 2, 3, 5]
#
#
# ============================================================
# BRUTE FORCE APPROACH
# ============================================================
#
# IDEA:
# -----
#
# Generate all permutations.
#
# Sort them.
#
# Find current permutation.
#
# Return the next one.
#
#
# TIME  : O(N!)
# SPACE : O(N!)
#
#
# Not suitable for interviews.
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# STEP 1:
# Find breakpoint.
#
# First index from right such that:
#
# arr[i] < arr[i+1]
#
#
# STEP 2:
# Find first element from right
# greater than arr[i]
#
#
# STEP 3:
# Swap them.
#
#
# STEP 4:
# Reverse everything after breakpoint.
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def next_permutation(nums):

    n = len(nums)

    # ========================================================
    # STEP 1: FIND BREAKPOINT
    # ========================================================

    breakpoint_index = -1

    for i in range(n - 2, -1, -1):

        if nums[i] < nums[i + 1]:

            breakpoint_index = i
            break

    # ========================================================
    # EDGE CASE
    # ========================================================
    #
    # Example:
    #
    # [3,2,1]
    #
    # Entire array is descending.
    #
    # Already the last permutation.
    #
    # Next permutation:
    #
    # [1,2,3]
    #
    # ========================================================

    if breakpoint_index == -1:

        nums.reverse()
        return nums

    # ========================================================
    # STEP 2:
    # FIND SMALLEST ELEMENT GREATER THAN
    # nums[breakpoint_index]
    # ========================================================

    for i in range(n - 1, breakpoint_index, -1):

        if nums[i] > nums[breakpoint_index]:

            nums[i], nums[breakpoint_index] = (
                nums[breakpoint_index],
                nums[i]
            )

            break

    # ========================================================
    # STEP 3:
    # REVERSE THE SUFFIX
    # ========================================================

    left = breakpoint_index + 1
    right = n - 1

    while left < right:

        nums[left], nums[right] = (
            nums[right],
            nums[left]
        )

        left += 1
        right -= 1

    return nums


# ============================================================
# DRIVER CODE
# ============================================================

print("================================================")
print("NEXT PERMUTATION")
print("================================================")

arr1 = [1, 2, 3]

print("Input :", arr1)
print("Output:", next_permutation(arr1[:]))

print()

arr2 = [1, 3, 5, 4, 2]

print("Input :", arr2)
print("Output:", next_permutation(arr2[:]))

print()

arr3 = [3, 2, 1]

print("Input :", arr3)
print("Output:", next_permutation(arr3[:]))

print()

arr4 = [1, 1, 5]

print("Input :", arr4)
print("Output:", next_permutation(arr4[:]))