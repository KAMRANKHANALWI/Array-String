# ============================================================
# THREE SUM
# ============================================================
#
# Problem:
#
# Given an integer array,
#
# find all UNIQUE triplets
# whose sum equals zero.
#
#
# Return all unique triplets.
#
#
# Example:
#
# arr = [-1,0,1,2,-1,-4]
#
#
# Answer:
#
# [
#   [-1,-1,2],
#   [-1,0,1]
# ]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Three Sum is simply
#
# Two Sum
#
# +
#
# One Extra Loop.
#
#
# Suppose:
#
# arr =
#
# [-1,0,1,2,-1,-4]
#
#
# Fix:
#
# -1
#
#
# Then we need:
#
# x + y = 1
#
#
# because:
#
# -1 + x + y = 0
#
#
# Therefore,
#
# for every fixed element,
#
# the remaining problem becomes
#
# Two Sum.
#
#
# This leads to:
#
# 1. Brute Force
#
# 2. Better (Hash Set)
#
# 3. Optimal (Sorting + Two Pointers)
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Try every possible triplet.
#
#
# Three nested loops.
#
#
# If:
#
# arr[i] + arr[j] + arr[k] == 0
#
#
# Store the triplet.
#
#
# Since duplicates are possible,
#
# sort every triplet
#
# before storing it.
#
#
# Use a set to avoid
# duplicate triplets.
#
#
# TIME  : O(N³)
#
# SPACE : O(Number of Triplets)
#
# ============================================================


def three_sum_brute(arr):

    n = len(arr)

    unique_triplets = set()

    for i in range(n):

        for j in range(i + 1, n):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:

                    triplet = sorted([arr[i], arr[j], arr[k]])

                    unique_triplets.add(tuple(triplet))

    return [list(triplet) for triplet in unique_triplets]


# ============================================================
# 2. BETTER APPROACH (HASH SET)
# ============================================================
#
# IDEA:
#
# Fix one element.
#
#
# Remaining problem
# becomes:
#
# Two Sum.
#
#
# Maintain a Hash Set.
#
#
# current
#
# +
#
# third
#
# =
#
# -fixed_element
#
#
# If third already exists,
#
# one valid triplet
# has been found.
#
#
# Again,
#
# store triplets inside
# a set to avoid duplicates.
#
#
# TIME  : O(N²)
#
# SPACE : O(N)
#
# ============================================================


def three_sum_better(arr):

    n = len(arr)

    unique_triplets = set()

    for i in range(n):

        seen = set()

        for j in range(i + 1, n):

            third = -(arr[i] + arr[j])

            if third in seen:

                triplet = sorted([arr[i], arr[j], third])

                unique_triplets.add(tuple(triplet))

            seen.add(arr[j])

    return [list(triplet) for triplet in unique_triplets]


# ============================================================
# 3. OPTIMAL
# (SORT + TWO POINTERS)
# ============================================================
#
# IDEA:
#
# Step 1:
#
# Sort the array.
#
#
# Step 2:
#
# Fix one element.
#
#
# Step 3:
#
# Remaining problem
# becomes Two Sum.
#
#
# Maintain:
#
# left
#
# right
#
#
# Depending on
# current sum:
#
# Too Small
#
# -> left++
#
#
# Too Large
#
# -> right--
#
#
# Equal
#
# -> Store answer
#
#
# IMPORTANT:
#
# Skip duplicate values
#
# for:
#
# i
#
# left
#
# right
#
#
# This guarantees
# only UNIQUE triplets.
#
#
# TIME  : O(N²)
#
# SPACE : O(1)
#
# ============================================================


def three_sum_optimal(arr):

    arr.sort()

    answer = []

    n = len(arr)

    for i in range(n):

        # Skip duplicate first element

        if i > 0 and arr[i] == arr[i - 1]:

            continue

        left = i + 1

        right = n - 1

        while left < right:

            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum < 0:

                left += 1

            elif current_sum > 0:

                right -= 1

            else:

                answer.append([arr[i], arr[left], arr[right]])

                left += 1
                right -= 1

                # Skip duplicate values on the left

                while left < right and arr[left] == arr[left - 1]:

                    left += 1

                # Skip duplicate values on the right

                while left < right and arr[right] == arr[right + 1]:

                    right -= 1

    return answer


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [-1,0,1,2,-1,-4]
#
#
# Sort:
#
# [-4,-1,-1,0,1,2]
#
#
# Fix:
#
# -4
#
# Need:
#
# 4
#
# No answer.
#
#
# --------------------------
#
# Fix:
#
# -1
#
#
# left = -1
#
# right = 2
#
#
# Sum:
#
# -1 + -1 + 2
#
# = 0
#
#
# Store:
#
# [-1,-1,2]
#
#
# Move both pointers.
#
#
# Skip duplicates.
#
#
# Continue.
#
#
# Next answer:
#
# [-1,0,1]
#
#
# Final Answer:
#
# [
#   [-1,-1,2],
#   [-1,0,1]
# ]
#
# ============================================================

# ============================================================
# DRIVER CODE
# ============================================================

arr = [-1, 0, 1, 2, -1, -4]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print("Triplets =", three_sum_brute(arr))

print()

print("================================================")
print("2. BETTER APPROACH (HASH SET)")
print("================================================")

print("Triplets =", three_sum_better(arr))

print()

print("================================================")
print("3. OPTIMAL (SORT + TWO POINTERS)")
print("================================================")

print("Triplets =", three_sum_optimal(arr))

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [0, 0, 0]

print("Array =", arr2)

print("Triplets =", three_sum_optimal(arr2))

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

arr3 = [-2, 0, 1, 1, 2]

print("Array =", arr3)

print("Triplets =", three_sum_optimal(arr3))

print()

print("================================================")
print("NO VALID TRIPLETS")
print("================================================")

arr4 = [1, 2, 3, 4]

print("Array =", arr4)

print("Triplets =", three_sum_optimal(arr4))

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force")
print("Time  : O(N³)")
print("Space : O(Number of Triplets)")

print()

print("Hash Set")
print("Time  : O(N²)")
print("Space : O(N)")

print()

print("Sort + Two Pointers")
print("Time  : O(N²)")
print("Space : O(1)")

print()

print("================================================")
print("INTERVIEW NOTES")
print("================================================")

print("Brute Force")
print("-> Check every possible triplet.")

print()

print("Better")
print("-> Fix one element.")
print("-> Remaining problem becomes Two Sum using a Hash Set.")

print()

print("Optimal")
print("-> Sort the array.")
print("-> Fix one element.")
print("-> Solve the remaining part using Two Pointers.")
print("-> Skip duplicate values for i, left and right.")

print()

print("================================================")
print("MEMORY TRICK")
print("================================================")

print("Two Sum")
print("-> Solve directly.")

print()

print("Three Sum")
print("-> Fix ONE element.")
print("-> Remaining problem becomes Two Sum.")

print()

print("Four Sum")
print("-> Fix TWO elements.")
print("-> Remaining problem becomes Two Sum.")

print()

print("Pattern:")
print("More Sum Problems")
print("↓")
print("Reduce them")
print("↓")
print("Until they become Two Sum.")
