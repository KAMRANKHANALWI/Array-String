# ============================================================
# COUNT INVERSIONS IN AN ARRAY
# ============================================================
#
# Problem:
#
# Given an array,
# count the number of inversions.
#
#
# An inversion is a pair:
#
# (i, j)
#
# such that:
#
# i < j
#
# and
#
# arr[i] > arr[j]
#
#
# Example:
#
# arr = [5,3,2,4,1]
#
#
# Inversions:
#
# (5,3)
# (5,2)
# (5,4)
# (5,1)
#
# (3,2)
# (3,1)
#
# (2,1)
#
# (4,1)
#
#
# Total:
#
# 8
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Inversion means:
#
# A larger number appears before
# a smaller number.
#
#
# Example:
#
# [1,2,3,4]
#
# Inversions = 0
#
#
# [4,3,2,1]
#
# Maximum inversions
#
#
# Therefore:
#
# Inversion Count can be viewed as:
#
# "How unsorted is the array?"
#
#
# ------------------------------------------------------------
# IMPORTANT INSIGHT
# ------------------------------------------------------------
#
# Whenever you hear:
#
# - Count Pairs
# - Reverse Pairs
# - Inversions
#
# Think:
#
# Merge Sort
#
#
# Because Merge Sort naturally compares:
#
# Left Half
# Right Half
#
# which is exactly what we need.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Check every pair:
#
# (i, j)
#
# where:
#
# j > i
#
#
# If:
#
# arr[i] > arr[j]
#
# count inversion.
#
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def count_inversions_brute(arr):

    n = len(arr)

    count = 0

    for i in range(n):

        for j in range(i + 1, n):

            if arr[i] > arr[j]:

                count += 1

    return count


# ============================================================
# 2. OPTIMAL APPROACH (MERGE SORT)
# ============================================================
#
# KEY OBSERVATION:
#
# During merge step:
#
# Left Half  -> Sorted
# Right Half -> Sorted
#
#
# Example:
#
# Left  = [2,5,8]
#
# Right = [1,6]
#
#
# Compare:
#
# 2 and 1
#
#
# Since:
#
# 2 > 1
#
#
# Then automatically:
#
# 5 > 1
# 8 > 1
#
#
# because Left Half is sorted.
#
#
# Therefore:
#
# Inversions =
#
# all remaining elements
# in left half.
#
#
# Formula:
#
# count += (mid - left + 1)
#
#
# Example:
#
# left pointer = 0
#
# Left:
#
# [2,5,8]
#
# mid = 2
#
#
# Count:
#
# 2 - 0 + 1
#
# = 3
#
#
# representing:
#
# (2,1)
# (5,1)
# (8,1)
#
#
# This is the magic formula.
#
# ============================================================


# ============================================================
# MERGE FUNCTION
# ============================================================

def merge(arr, low, mid, high):

    temp = []

    left = low
    right = mid + 1

    inversion_count = 0

    while left <= mid and right <= high:

        if arr[left] <= arr[right]:

            temp.append(arr[left])
            left += 1

        else:

            temp.append(arr[right])

            inversion_count += (
                mid - left + 1
            )

            right += 1

    while left <= mid:

        temp.append(arr[left])
        left += 1

    while right <= high:

        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):

        arr[i] = temp[i - low]

    return inversion_count


# ============================================================
# MERGE SORT
# ============================================================

def merge_sort(arr, low, high):

    if low >= high:

        return 0

    mid = (low + high) // 2

    inversion_count = 0

    inversion_count += merge_sort(
        arr,
        low,
        mid
    )

    inversion_count += merge_sort(
        arr,
        mid + 1,
        high
    )

    inversion_count += merge(
        arr,
        low,
        mid,
        high
    )

    return inversion_count


# ============================================================
# OPTIMAL WRAPPER
# ============================================================
#
# TIME  : O(N log N)
# SPACE : O(N)
#
# ============================================================

def count_inversions_optimal(arr):

    copy_arr = arr.copy()

    return merge_sort(
        copy_arr,
        0,
        len(copy_arr) - 1
    )


# ============================================================
# DRIVER CODE
# ============================================================

arr = [5, 3, 2, 4, 1]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Inversion Count =",
    count_inversions_brute(arr)
)

print()

print("================================================")
print("2. OPTIMAL (MERGE SORT)")
print("================================================")

print(
    "Inversion Count =",
    count_inversions_optimal(arr)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [1, 2, 3, 4, 5]

print("Array =", arr2)

print(
    "Inversion Count =",
    count_inversions_optimal(arr2)
)

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

arr3 = [5, 4, 3, 2, 1]

print("Array =", arr3)

print(
    "Inversion Count =",
    count_inversions_optimal(arr3)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force -> O(N²), O(1)")
print("Merge Sort  -> O(N log N), O(N)")