# ============================================================
# MERGE SORTED ARRAYS WITHOUT EXTRA SPACE
# ============================================================
#
# Problem:
#
# Given two sorted arrays:
#
# arr1 and arr2
#
# Merge them WITHOUT using extra space.
#
#
# Example:
#
# arr1 = [1,3,5,7]
# arr2 = [0,2,6,8,9]
#
#
# Output:
#
# arr1 = [0,1,2,3]
# arr2 = [5,6,7,8,9]
#
#
# IMPORTANT:
#
# We are NOT creating:
#
# [0,1,2,3,5,6,7,8,9]
#
#
# Instead:
#
# arr1 should contain the first n elements
#
# arr2 should contain the remaining m elements
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Think of both arrays as ONE virtual array.
#
#
# Example:
#
# arr1 = [1,3,5,7]
# arr2 = [0,2,6,8,9]
#
#
# Virtual Array:
#
# [1,3,5,7,0,2,6,8,9]
#
#
# Index:
#
# 0 1 2 3 | 4 5 6 7 8
#
#
# Instead of physically merging,
# we compare elements that are
# "gap" distance apart.
#
#
# This idea comes from:
#
# Shell Sort
#
#
# Gap Sequence:
#
# 9 -> 5 -> 3 -> 2 -> 1 -> 0
#
#
# As gap becomes smaller,
# elements move closer to their
# correct position.
#
#
# When gap becomes 1,
# the entire virtual array
# becomes sorted.
#
#
# This is called:
#
# GAP METHOD
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Create a temporary array.
#
# Merge exactly like Merge Sort.
#
# Then:
#
# Copy first n elements into arr1
#
# Copy remaining elements into arr2
#
#
# TIME  : O(N + M)
# SPACE : O(N + M)
#
# ============================================================

def merge_brute(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    temp = []

    i = 0
    j = 0

    while i < n and j < m:

        if arr1[i] <= arr2[j]:

            temp.append(arr1[i])
            i += 1

        else:

            temp.append(arr2[j])
            j += 1

    while i < n:

        temp.append(arr1[i])
        i += 1

    while j < m:

        temp.append(arr2[j])
        j += 1

    for i in range(n):

        arr1[i] = temp[i]

    for j in range(m):

        arr2[j] = temp[n + j]

    return arr1, arr2


# ============================================================
# 2. BETTER APPROACH
# ============================================================
#
# IDEA:
#
# Compare:
#
# largest element of arr1
#
# with
#
# smallest element of arr2
#
#
# If:
#
# arr1[left] > arr2[right]
#
# swap them.
#
#
# Continue until:
#
# left crosses right.
#
#
# Finally:
#
# sort arr1
# sort arr2
#
#
# TIME:
#
# O(min(N,M))
# +
# O(N log N)
# +
# O(M log M)
#
#
# SPACE:
#
# O(1)
#
# ============================================================

def merge_better(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    left = n - 1
    right = 0

    while left >= 0 and right < m:

        if arr1[left] > arr2[right]:

            arr1[left], arr2[right] = (
                arr2[right],
                arr1[left]
            )

            left -= 1
            right += 1

        else:

            break

    arr1.sort()
    arr2.sort()

    return arr1, arr2


# ============================================================
# GAP HELPER FUNCTION
# ============================================================
#
# Gap Sequence:
#
# 9 -> 5 -> 3 -> 2 -> 1 -> 0
#
#
# Formula:
#
# ceil(gap / 2)
#
#
# Example:
#
# gap = 5
#
# next gap = 3
#
# ============================================================

def next_gap(gap):

    if gap <= 1:
        return 0

    return (gap // 2) + (gap % 2)


# ============================================================
# HELPER FUNCTION
# ============================================================
#
# Swap only when:
#
# left element > right element
#
# ============================================================

def swap_if_greater(arr1, arr2, i, j):

    if arr1[i] > arr2[j]:

        arr1[i], arr2[j] = (
            arr2[j],
            arr1[i]
        )


# ============================================================
# 3. OPTIMAL APPROACH (GAP METHOD)
# ============================================================
#
# IDEA:
#
# Treat both arrays as one virtual array.
#
#
# Example:
#
# arr1 = [1,3,5,7]
# arr2 = [0,2,6,8,9]
#
#
# Virtual:
#
# [1,3,5,7,0,2,6,8,9]
#
#
# Compare elements gap distance apart.
#
#
# Three Cases:
#
#
# CASE 1:
#
# Both indices inside arr1
#
#
# CASE 2:
#
# One index in arr1
# One index in arr2
#
#
# CASE 3:
#
# Both indices inside arr2
#
#
# Why right - n ?
#
# Example:
#
# n = len(arr1) = 4
#
#
# Virtual Index:
#
# 4
#
# actually means:
#
# arr2[0]
#
#
# Virtual Index:
#
# 5
#
# actually means:
#
# arr2[1]
#
#
# Therefore:
#
# arr2 index
#
# =
#
# virtual_index - n
#
#
# TIME:
#
# O((N+M) log(N+M))
#
#
# SPACE:
#
# O(1)
#
# ============================================================

def merge_optimal(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    total_length = n + m

    gap = next_gap(total_length)

    while gap > 0:

        left = 0
        right = left + gap

        while right < total_length:

            # ==========================================
            # CASE 1
            #
            # arr1 and arr1
            # ==========================================

            if left < n and right < n:

                swap_if_greater(
                    arr1,
                    arr1,
                    left,
                    right
                )

            # ==========================================
            # CASE 2
            #
            # arr1 and arr2
            # ==========================================

            elif left < n and right >= n:

                swap_if_greater(
                    arr1,
                    arr2,
                    left,
                    right - n
                )

            # ==========================================
            # CASE 3
            #
            # arr2 and arr2
            # ==========================================

            else:

                swap_if_greater(
                    arr2,
                    arr2,
                    left - n,
                    right - n
                )

            left += 1
            right += 1

        gap = next_gap(gap)

    return arr1, arr2


# ============================================================
# DRIVER CODE
# ============================================================

arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

print("================================================")
print("INPUT")
print("================================================")

print("arr1 =", arr1)
print("arr2 =", arr2)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

a1 = arr1.copy()
a2 = arr2.copy()

merge_brute(a1, a2)

print("arr1 =", a1)
print("arr2 =", a2)

print()

print("================================================")
print("2. BETTER APPROACH")
print("================================================")

a1 = arr1.copy()
a2 = arr2.copy()

merge_better(a1, a2)

print("arr1 =", a1)
print("arr2 =", a2)

print()

print("================================================")
print("3. OPTIMAL (GAP METHOD)")
print("================================================")

a1 = arr1.copy()
a2 = arr2.copy()

merge_optimal(a1, a2)

print("arr1 =", a1)
print("arr2 =", a2)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

a1 = [1, 4, 8, 10]
a2 = [2, 3, 9]

print("Before:")
print("arr1 =", a1)
print("arr2 =", a2)

merge_optimal(a1, a2)

print()

print("After:")
print("arr1 =", a1)
print("arr2 =", a2)