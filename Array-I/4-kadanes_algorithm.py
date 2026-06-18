# ============================================================
# KADANE'S ALGORITHM
# ============================================================
#
# Problem:
# --------
#
# Given an integer array,
# find the maximum possible subarray sum.
#
# A subarray consists of
# contiguous elements only.
#
#
# Example:
#
# [2, 3, -8, 7, -1, 2, 3]
#
#
# Possible Subarrays:
#
# [2]
# [2,3]
# [3,-8]
# [7]
# [7,-1]
# [7,-1,2]
# [7,-1,2,3]
#
#
# Their sums:
#
# [2]            = 2
# [2,3]          = 5
# [7]            = 7
# [7,-1]         = 6
# [7,-1,2]       = 8
# [7,-1,2,3]     = 11
#
#
# Maximum Sum:
#
# 11
#
#
# Maximum Subarray:
#
# [7, -1, 2, 3]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Consider:
#
# [2, 3, -8, 7]
#
#
# Running Sum:
#
# 2
# 5
# -3
#
#
# After reaching:
#
# current_sum = -3
#
#
# Next Element:
#
# 7
#
#
# Option 1:
#
# Continue:
#
# -3 + 7 = 4
#
#
# Option 2:
#
# Start Fresh:
#
# 7
#
#
# Obviously:
#
# 7 > 4
#
#
# Therefore:
#
# A NEGATIVE PREFIX NEVER HELPS.
#
#
# If current_sum becomes negative,
# discard it immediately.
#
#
# This is the entire intuition
# behind Kadane's Algorithm.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE APPROACH
# ============================================================
#
# IDEA:
# -----
#
# Generate every possible subarray.
#
# For each subarray:
#
# Calculate its sum separately.
#
# Keep track of maximum sum.
#
#
# Example:
#
# [1,2,3]
#
# Subarrays:
#
# [1]
# [1,2]
# [1,2,3]
# [2]
# [2,3]
# [3]
#
#
# TIME  : O(N^3)
# SPACE : O(1)
#
# ============================================================

def max_subarray_sum_brute(nums):

    n = len(nums)

    maximum = float("-inf")

    for start in range(n):

        for end in range(start, n):

            current_sum = 0

            for k in range(start, end + 1):

                current_sum += nums[k]

            maximum = max(maximum, current_sum)

    return maximum


# ============================================================
# 2. BETTER APPROACH
# ============================================================
#
# IDEA:
# -----
#
# Avoid recalculating sum every time.
#
# Reuse previous sum.
#
#
# Example:
#
# [2,3,-8,7]
#
# Start at index 0:
#
# sum = 0
#
# sum += 2   -> 2
# sum += 3   -> 5
# sum += -8  -> -3
# sum += 7   -> 4
#
#
# TIME  : O(N^2)
# SPACE : O(1)
#
# ============================================================

def max_subarray_sum_better(nums):

    n = len(nums)

    maximum = float("-inf")

    for start in range(n):

        current_sum = 0

        for end in range(start, n):

            current_sum += nums[end]

            maximum = max(maximum, current_sum)

    return maximum


# ============================================================
# 3. OPTIMAL APPROACH (KADANE'S ALGORITHM)
# ============================================================
#
# IDEA:
# -----
#
# Maintain:
#
# current_sum
# max_sum
#
#
# If current_sum becomes negative:
#
# discard it
#
# because it will only hurt
# future subarrays.
#
#
# Example:
#
# current_sum = -5
#
# next element = 7
#
# Continuing:
#
# -5 + 7 = 2
#
#
# Starting Fresh:
#
# 7
#
#
# Starting fresh is better.
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def kadanes_algorithm(nums):

    current_sum = 0

    max_sum = float("-inf")

    for num in nums:

        current_sum += num

        max_sum = max(max_sum, current_sum)

        if current_sum < 0:

            current_sum = 0

    return max_sum


# ============================================================
# 4. KADANE'S ALGORITHM
#    WITH SUBARRAY PRINTING
# ============================================================
#
# Interview Follow-Up:
#
# "Can you also return the subarray?"
#
#
# IDEA:
# -----
#
# temp_start:
#
# Potential starting index.
#
#
# Whenever current_sum becomes 0:
#
# next index becomes a candidate start.
#
#
# Whenever max_sum improves:
#
# store:
#
# start
# end
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def kadanes_with_subarray(nums):

    current_sum = 0

    max_sum = float("-inf")

    start = 0
    end = 0

    temp_start = 0

    for i in range(len(nums)):

        current_sum += nums[i]

        if current_sum > max_sum:

            max_sum = current_sum

            start = temp_start
            end = i

        if current_sum < 0:

            current_sum = 0

            temp_start = i + 1

    return max_sum, nums[start:end + 1]


# ============================================================
# EDGE CASE:
# ALL NEGATIVE NUMBERS
# ============================================================
#
# Example:
#
# [-2,-3,-1,-5]
#
#
# Answer:
#
# -1
#
#
# Kadane still works because:
#
# max_sum gets updated BEFORE reset.
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

nums = [2, 3, -8, 7, -1, 2, 3]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(nums)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print("Maximum Sum =", max_subarray_sum_brute(nums))

print()

print("================================================")
print("2. BETTER APPROACH")
print("================================================")

print("Maximum Sum =", max_subarray_sum_better(nums))

print()

print("================================================")
print("3. KADANE'S ALGORITHM")
print("================================================")

print("Maximum Sum =", kadanes_algorithm(nums))

print()

print("================================================")
print("4. KADANE + PRINT SUBARRAY")
print("================================================")

max_sum, subarray = kadanes_with_subarray(nums)

print("Maximum Sum =", max_sum)
print("Subarray    =", subarray)

print()

print("================================================")
print("ALL NEGATIVE TEST CASE")
print("================================================")

negative_nums = [-2, -3, -1, -5]

print("Array       =", negative_nums)
print("Maximum Sum =", kadanes_algorithm(negative_nums))