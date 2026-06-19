# ============================================================
# SORT AN ARRAY OF 0s, 1s AND 2s
# ============================================================
#
# Problem:
# --------
#
# Given an array containing only:
#
# 0
# 1
# 2
#
# Sort the array.
#
#
# Example:
#
# Input:
#
# [2, 0, 2, 1, 1, 0]
#
#
# Output:
#
# [0, 0, 1, 1, 2, 2]
#
#
# ============================================================
# OBSERVATION
# ============================================================
#
# Since the array contains only:
#
# 0, 1 and 2
#
# we can do better than a normal sort.
#
#
# Normal Sorting:
#
# O(N log N)
#
#
# But because there are only
# three possible values,
# we can solve it in:
#
# O(N)
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE APPROACH
# ============================================================
#
# IDEA:
# -----
#
# Use the built-in sorting algorithm.
#
#
# Example:
#
# [2,0,2,1,1,0]
#
# sort()
#
# ->
#
# [0,0,1,1,2,2]
#
#
# TIME  : O(N log N)
# SPACE : Depends on sorting implementation
#
# ============================================================

def sort_colors_brute(nums):

    nums.sort()

    return nums


# ============================================================
# 2. BETTER APPROACH (COUNTING)
# ============================================================
#
# IDEA:
# -----
#
# Count:
#
# count0
# count1
# count2
#
#
# Example:
#
# [2,0,2,1,1,0]
#
#
# count0 = 2
# count1 = 2
# count2 = 2
#
#
# Rebuild array:
#
# [0,0,1,1,2,2]
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def sort_colors_better(nums):

    count0 = 0
    count1 = 0
    count2 = 0

    for num in nums:

        if num == 0:
            count0 += 1

        elif num == 1:
            count1 += 1

        else:
            count2 += 1

    index = 0

    for _ in range(count0):

        nums[index] = 0
        index += 1

    for _ in range(count1):

        nums[index] = 1
        index += 1

    for _ in range(count2):

        nums[index] = 2
        index += 1

    return nums


# ============================================================
# 3. OPTIMAL APPROACH
# ============================================================
#
# DUTCH NATIONAL FLAG ALGORITHM
#
# Invented by:
#
# Edsger Dijkstra
#
#
# ============================================================
# CORE IDEA
# ============================================================
#
# Build 3 regions:
#
# 0s on the left
# 1s in the middle
# 2s on the right
#
#
# Maintain:
#
# low
# mid
# high
#
#
# At any point:
#
# ------------------------------------------------------------
#
# 0 ------ low-1
#
# Contains:
#
# ONLY 0s
#
#
# ------------------------------------------------------------
#
# low ------ mid-1
#
# Contains:
#
# ONLY 1s
#
#
# ------------------------------------------------------------
#
# mid ------ high
#
# Contains:
#
# UNKNOWN ELEMENTS
#
# Could be:
#
# 0
# 1
# 2
#
#
# ------------------------------------------------------------
#
# high+1 ------ n-1
#
# Contains:
#
# ONLY 2s
#
# ------------------------------------------------------------
#
#
# VISUALIZATION:
#
# 0s | 1s | UNKNOWN | 2s
#
#
# ============================================================
# CASE 1
# ============================================================
#
# nums[mid] == 0
#
# Example:
#
# [1,0,2,1,0]
#    ^
#   mid
#
#
# 0 belongs to left side.
#
#
# Swap:
#
# nums[low]
# nums[mid]
#
#
# Then:
#
# low += 1
# mid += 1
#
#
# ============================================================
# CASE 2
# ============================================================
#
# nums[mid] == 1
#
# Example:
#
# [1,0,2,1,0]
#  ^
# mid
#
#
# 1 already belongs
# in the middle region.
#
#
# Simply:
#
# mid += 1
#
#
# ============================================================
# CASE 3
# ============================================================
#
# nums[mid] == 2
#
# Example:
#
# [1,0,2,1,0]
#      ^
#     mid
#
#
# 2 belongs to right side.
#
#
# Swap:
#
# nums[mid]
# nums[high]
#
#
# Then:
#
# high -= 1
#
#
# IMPORTANT:
#
# DO NOT MOVE MID
#
#
# Why?
#
# Because after swapping,
# the new element at mid
# is unprocessed.
#
#
# It could be:
#
# 0
# 1
# 2
#
#
# So we must inspect it again.
#
#
# ============================================================
# STOP CONDITION
# ============================================================
#
# Continue while:
#
# mid <= high
#
#
# Once:
#
# mid > high
#
# Unknown region disappears.
#
#
# Array becomes sorted.
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def sort_colors_optimal(nums):

    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        # ====================================================
        # CASE 1
        # ====================================================

        if nums[mid] == 0:

            nums[low], nums[mid] = nums[mid], nums[low]

            low += 1
            mid += 1

        # ====================================================
        # CASE 2
        # ====================================================

        elif nums[mid] == 1:

            mid += 1

        # ====================================================
        # CASE 3
        # ====================================================

        else:

            nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1

    return nums


# ============================================================
# DRIVER CODE
# ============================================================

arr1 = [2, 0, 2, 1, 1, 0]
arr2 = [2, 0, 2, 1, 1, 0]
arr3 = [2, 0, 2, 1, 1, 0]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr1)

print()

print("================================================")
print("1. BRUTE FORCE APPROACH")
print("================================================")

print(sort_colors_brute(arr1))

print()

print("================================================")
print("2. BETTER APPROACH")
print("================================================")

print(sort_colors_better(arr2))

print()

print("================================================")
print("3. DUTCH NATIONAL FLAG ALGORITHM")
print("================================================")

print(sort_colors_optimal(arr3))