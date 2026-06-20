# ============================================================
# ROTATE MATRIX BY 90 DEGREES
# ============================================================
#
# Problem:
#
# Given an N x N matrix,
# rotate it 90 degrees clockwise.
#
# Example:
#
# Input:
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# Output:
#
# 7 4 1
# 8 5 2
# 9 6 3
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# 90° Clockwise Rotation
#
# =
#
# Transpose Matrix
# +
# Reverse Every Row
#
#
# Example:
#
# Original:
#
# 1 2 3
# 4 5 6
# 7 8 9
#
#
# Step 1: Transpose
#
# 1 4 7
# 2 5 8
# 3 6 9
#
#
# Step 2: Reverse Every Row
#
# 7 4 1
# 8 5 2
# 9 6 3
#
#
# Final Answer Achieved.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# Create a new matrix.
#
# Every element:
#
# matrix[i][j]
#
# goes to:
#
# rotated[j][n - 1 - i]
#
# TIME  : O(N²)
# SPACE : O(N²)
#
# ============================================================

def rotate_matrix_brute(matrix):

    n = len(matrix)

    rotated = [[0] * n for _ in range(n)]

    for i in range(n):

        for j in range(n):

            rotated[j][n - 1 - i] = matrix[i][j]

    return rotated


# ============================================================
# 2. OPTIMAL APPROACH
# ============================================================
#
# Step 1:
# Transpose Matrix
#
# Step 2:
# Reverse Every Row
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def rotate_matrix_optimal(matrix):

    n = len(matrix)

    # ========================================================
    # STEP 1: TRANSPOSE
    # ========================================================

    for i in range(n):

        for j in range(i + 1, n):

            matrix[i][j], matrix[j][i] = (
                matrix[j][i],
                matrix[i][j]
            )

    # ========================================================
    # STEP 2: REVERSE EVERY ROW
    # ========================================================

    for row in matrix:

        row.reverse()

    return matrix


# ============================================================
# WHY j STARTS FROM i + 1 ?
# ============================================================
#
# During transpose:
#
# (i,j) <-> (j,i)
#
# Example:
#
# (0,1) <-> (1,0)
#
# If we later visit:
#
# (1,0)
#
# we would swap again and undo the work.
#
# Therefore we only process the
# UPPER TRIANGLE of the matrix.
#
# Example:
#
# (0,1) (0,2) (0,3)
# (1,2) (1,3)
# (2,3)
#
# Hence:
#
# for i in range(n):
#     for j in range(i + 1, n):
#
# Diagonal elements:
#
# (0,0)
# (1,1)
# (2,2)
#
# remain unchanged.
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("================================================")
print("INPUT MATRIX")
print("================================================")

for row in matrix1:
    print(row)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

rotated_brute = rotate_matrix_brute(matrix1)

for row in rotated_brute:
    print(row)

print()

print("================================================")
print("2. OPTIMAL APPROACH")
print("================================================")

rotated_optimal = rotate_matrix_optimal(matrix2)

for row in rotated_optimal:
    print(row)