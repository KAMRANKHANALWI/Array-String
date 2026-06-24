# ============================================================
# SEARCH IN A 2D MATRIX
# ============================================================
#
# Problem:
#
# Given an m x n matrix where:
#
# 1. Each row is sorted.
#
# 2. First element of every row
#    is greater than the last
#    element of the previous row.
#
#
# Return:
#
# True  -> if target exists
# False -> otherwise
#
#
# Example:
#
# matrix =
#
# [
#   [1, 3, 5, 7],
#   [10,11,16,20],
#   [23,30,34,60]
# ]
#
# target = 16
#
# Answer = True
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# This matrix behaves like
# a single sorted array.
#
#
# Example:
#
# [
#   [1,3,5,7],
#   [10,11,16,20],
#   [23,30,34,60]
# ]
#
#
# can be viewed as:
#
# [1,3,5,7,10,11,16,20,23,30,34,60]
#
#
# Why?
#
# Because:
#
# Last element of previous row
# <
# First element of next row
#
#
# Therefore:
#
# Entire matrix is globally sorted.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Visit every cell.
#
# If target is found:
#
# return True
#
#
# Otherwise:
#
# return False
#
#
# TIME  : O(N × M)
# SPACE : O(1)
#
# ============================================================

def search_matrix_brute(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):

        for c in range(cols):

            if matrix[r][c] == target:

                return True

    return False


# ============================================================
# 2. BETTER APPROACH
# ============================================================
#
# IDEA:
#
# Every row is sorted.
#
# Perform Binary Search
# on every row.
#
#
# TIME  :
#
# O(N × log M)
#
# SPACE :
#
# O(1)
#
# ============================================================

def binary_search_row(row, target):

    low = 0
    high = len(row) - 1

    while low <= high:

        mid = (low + high) // 2

        if row[mid] == target:

            return True

        elif row[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    return False


def search_matrix_better(matrix, target):

    for row in matrix:

        if binary_search_row(row, target):

            return True

    return False


# ============================================================
# 3. BETTER BETTER APPROACH
# ============================================================
#
# IDEA:
#
# First identify the row
# that could contain target.
#
#
# Condition:
#
# row[0] <= target <= row[last]
#
#
# Once row is found:
#
# Perform Binary Search
# only in that row.
#
#
# TIME:
#
# O(N + log M)
#
# SPACE:
#
# O(1)
#
# ============================================================

def search_matrix_better_better(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):

        if (
            matrix[r][0]
            <= target
            <= matrix[r][cols - 1]
        ):

            return binary_search_row(
                matrix[r],
                target
            )

    return False


# ============================================================
# 4. OPTIMAL APPROACH
# ============================================================
#
# GOLDEN IDEA:
#
# Treat matrix as a
# single sorted array.
#
#
# Example:
#
# [
#   [1,3,5,7],
#   [10,11,16,20],
#   [23,30,34,60]
# ]
#
#
# behaves like:
#
# [1,3,5,7,10,11,16,20,23,30,34,60]
#
#
# Total Elements:
#
# rows * cols
#
#
# Binary Search on:
#
# 0 to rows*cols - 1
#
#
# ------------------------------------------------------------
# MAGIC MAPPING
# ------------------------------------------------------------
#
# Convert 1D index
#
# into
#
# matrix coordinates.
#
#
# row = index // cols
#
# col = index % cols
#
#
# Example:
#
# cols = 4
#
# index = 8
#
#
# row = 8 // 4 = 2
#
# col = 8 % 4 = 0
#
#
# matrix[2][0]
#
# = 23
#
#
# This mapping is the heart
# of the optimal solution.
#
#
# TIME:
#
# O(log(N*M))
#
# SPACE:
#
# O(1)
#
# ============================================================

def search_matrix_optimal(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = rows * cols - 1

    while low <= high:

        mid = (low + high) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:

            return True

        elif value < target:

            low = mid + 1

        else:

            high = mid - 1

    return False


# ============================================================
# DRIVER CODE
# ============================================================

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 16

print("================================================")
print("INPUT MATRIX")
print("================================================")

for row in matrix:
    print(row)

print()

print("Target =", target)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    search_matrix_brute(
        matrix,
        target
    )
)

print()

print("================================================")
print("2. BETTER")
print("================================================")

print(
    search_matrix_better(
        matrix,
        target
    )
)

print()

print("================================================")
print("3. BETTER BETTER")
print("================================================")

print(
    search_matrix_better_better(
        matrix,
        target
    )
)

print()

print("================================================")
print("4. OPTIMAL")
print("================================================")

print(
    search_matrix_optimal(
        matrix,
        target
    )
)

print()

print("================================================")
print("TARGET NOT PRESENT")
print("================================================")

target2 = 13

print("Target =", target2)

print(
    search_matrix_optimal(
        matrix,
        target2
    )
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute         -> O(N*M)")
print("Better        -> O(N log M)")
print("Better Better -> O(N + log M)")
print("Optimal       -> O(log(N*M))")