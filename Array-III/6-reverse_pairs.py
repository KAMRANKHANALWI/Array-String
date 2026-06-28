# ============================================================
# REVERSE PAIRS
# ============================================================
#
# Problem:
#
# Given an integer array,
#
# count the number of
# Reverse Pairs.
#
#
# A Reverse Pair is:
#
# i < j
#
# and
#
# arr[i] > 2 * arr[j]
#
#
# Example:
#
# arr = [1,3,2,3,1]
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
# This problem looks very similar
# to Count Inversions.
#
#
# Difference:
#
# Inversions:
#
# arr[i] > arr[j]
#
#
# Reverse Pairs:
#
# arr[i] > 2 * arr[j]
#
#
# Brute Force checks every pair.
#
#
# But if both halves are sorted,
#
# we can count reverse pairs
# much faster using Merge Sort.
#
#
# IMPORTANT OBSERVATION:
#
# While checking one element
# from the left half,
#
# the right pointer
# never moves backward.
#
#
# Therefore,
#
# counting all reverse pairs
# takes only O(N)
# during every merge.
#
#
# This reduces
#
# O(N²)
#
# to
#
# O(N log N)
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Check every pair.
#
# If:
#
# i < j
#
# and
#
# arr[i] > 2 * arr[j]
#
# increase answer.
#
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def reverse_pairs_brute(arr):

    n = len(arr)

    count = 0

    for i in range(n):

        for j in range(i + 1, n):

            if arr[i] > 2 * arr[j]:

                count += 1

    return count


# ============================================================
# COUNT REVERSE PAIRS
# ============================================================
#
# Left Half:
#
# arr[left ... mid]
#
#
# Right Half:
#
# arr[mid+1 ... right]
#
#
# Both halves
# are already sorted.
#
#
# For every element
# in the left half,
#
# move the right pointer
# until condition fails.
#
#
# Since the right pointer
# never moves backward,
#
# total work is O(N).
#
#
# Example:
#
# Left:
#
# [3,5,8]
#
#
# Right:
#
# [1,2,6]
#
#
# For 3:
#
# 3 > 2×1
#
# True
#
#
# For 5:
#
# Continue from current pointer.
#
#
# Don't restart.
#
#
# This is the optimization.
#
# ============================================================

def count_reverse_pairs(arr, left, mid, right):

    count = 0

    j = mid + 1

    for i in range(left, mid + 1):

        while (

            j <= right

            and

            arr[i] > 2 * arr[j]

        ):

            j += 1

        count += j - (mid + 1)

    return count


# ============================================================
# MERGE
# ============================================================
#
# Same merge function
# used in Merge Sort.
#
#
# Merge two sorted halves
# into one sorted array.
#
#
# TIME  : O(N)
# SPACE : O(N)
#
# ============================================================

def merge(arr, left, mid, right):

    temp = []

    i = left
    j = mid + 1

    while (

        i <= mid

        and

        j <= right

    ):

        if arr[i] <= arr[j]:

            temp.append(arr[i])
            i += 1

        else:

            temp.append(arr[j])
            j += 1

    while i <= mid:

        temp.append(arr[i])
        i += 1

    while j <= right:

        temp.append(arr[j])
        j += 1

    for k in range(left, right + 1):

        arr[k] = temp[k - left]
        
# ============================================================
# MERGE SORT
# ============================================================
#
# Divide the array into
# two halves.
#
# Solve:
#
# Left Half
#
# Right Half
#
# Then:
#
# 1. Count Reverse Pairs
# 2. Merge both halves
#
#
# This is exactly the same
# structure as Merge Sort.
#
#
# TIME  :
#
# O(N log N)
#
# SPACE :
#
# O(N)
#
# ============================================================

def merge_sort(arr, left, right):

    count = 0

    if left >= right:

        return count

    mid = (left + right) // 2

    # Solve left half
    count += merge_sort(
        arr,
        left,
        mid
    )

    # Solve right half
    count += merge_sort(
        arr,
        mid + 1,
        right
    )

    # Count reverse pairs
    count += count_reverse_pairs(
        arr,
        left,
        mid,
        right
    )

    # Merge sorted halves
    merge(
        arr,
        left,
        mid,
        right
    )

    return count


# ============================================================
# 2. OPTIMAL APPROACH
# (MERGE SORT)
# ============================================================
#
# IDEA:
#
# Step 1:
#
# Divide the array.
#
#
# Step 2:
#
# Count reverse pairs
# inside left half.
#
#
# Step 3:
#
# Count reverse pairs
# inside right half.
#
#
# Step 4:
#
# Count reverse pairs
# between both halves.
#
#
# Step 5:
#
# Merge the two halves.
#
#
# Since counting takes O(N)
# at every Merge Sort level,
#
# Total Complexity:
#
# O(N log N)
#
#
# TIME  : O(N log N)
# SPACE : O(N)
#
# ============================================================

def reverse_pairs_optimal(arr):

    copy = arr.copy()

    return merge_sort(
        copy,
        0,
        len(copy) - 1
    )


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [1,3,2,3,1]
#
#
# Divide:
#
# [1,3,2]
#
# [3,1]
#
#
# Continue recursively
# until single elements.
#
#
# While merging:
#
# Left:
#
# [1,2,3]
#
#
# Right:
#
# [1,3]
#
#
# Compare:
#
# 1 > 2×1
#
# False
#
#
# 2 > 2×1
#
# False
#
#
# 3 > 2×1
#
# True
#
#
# Count = 1
#
#
# Continue Merge Sort.
#
#
# Eventually:
#
# Total Reverse Pairs:
#
# 2
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

arr = [1, 3, 2, 3, 1]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Reverse Pairs =",
    reverse_pairs_brute(arr)
)

print()

print("================================================")
print("2. OPTIMAL (MERGE SORT)")
print("================================================")

print(
    "Reverse Pairs =",
    reverse_pairs_optimal(arr)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [2, 4, 3, 5, 1]

print(arr2)

print(
    "Reverse Pairs =",
    reverse_pairs_optimal(arr2)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force -> O(N²),      O(1)")
print("Merge Sort  -> O(N log N), O(N)")