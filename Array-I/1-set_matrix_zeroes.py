# ============================================================
# SET MATRIX ZEROES
# ============================================================
#
# Problem:
# If any cell contains 0,
# make its entire row and column zero.
#
# We will learn:
#
# 1. Brute Force
# 2. Better Approach
# 3. Optimal Approach
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE APPROACH
# ============================================================
#
# IDEA:
# -----
# When we find a 0:
#
# - mark its row with -1
# - mark its column with -1
#
# Later:
# convert all -1 -> 0
#
# WHY?
# ----
# Because directly placing 0 causes chain reaction.
#
# TIME  : O((N*M)*(N+M))
# SPACE : O(1)
#
# ============================================================

def mark_row(matrix, row):

    cols = len(matrix[0])

    for c in range(cols):

        if matrix[row][c] != 0:
            matrix[row][c] = -1


def mark_col(matrix, col):

    rows = len(matrix)

    for r in range(rows):

        if matrix[r][col] != 0:
            matrix[r][col] = -1


def set_zeroes_brute(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Mark rows and cols
    for r in range(rows):

        for c in range(cols):

            if matrix[r][c] == 0:

                mark_row(matrix, r)
                mark_col(matrix, c)

    # Step 2: Convert -1 -> 0
    for r in range(rows):

        for c in range(cols):

            if matrix[r][c] == -1:
                matrix[r][c] = 0

    return matrix


# ============================================================
# 2. BETTER APPROACH
# ============================================================
#
# IDEA:
# -----
# Instead of modifying matrix immediately,
# store info separately.
#
# row[i] = 1
# means row i should become zero
#
# col[j] = 1
# means col j should become zero
#
# TIME  : O(N*M)
# SPACE : O(N + M)
#
# ============================================================

def set_zeroes_better(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    # Extra arrays
    row = [0] * rows
    col = [0] * cols

    # Step 1: Store which rows/cols should become zero
    for r in range(rows):

        for c in range(cols):

            if matrix[r][c] == 0:

                row[r] = 1
                col[c] = 1

    # Step 2: Fill zeros
    for r in range(rows):

        for c in range(cols):

            if row[r] == 1 or col[c] == 1:

                matrix[r][c] = 0

    return matrix


# ============================================================
# 3. OPTIMAL APPROACH
# ============================================================
#
# IDEA:
# -----
# Instead of row[] and col[],
# use:
#
# matrix[i][0]  -> row marker
# matrix[0][j]  -> col marker
#
# IMPORTANT:
# ----------
# matrix[0][0] belongs to BOTH:
#
# - first row
# - first column
#
# So we use:
#
# col0 = 1
#
# to separately track first column.
#
# TIME  : O(N*M)
# SPACE : O(1)
#
# ============================================================

def set_zeroes_optimal(matrix):

    n = len(matrix)
    m = len(matrix[0])

    # Tracks whether first column should become zero
    col0 = 1

    # ========================================================
    # STEP 1: STORE MARKERS
    # ========================================================

    for i in range(n):

        for j in range(m):

            if matrix[i][j] == 0:

                # Mark row
                matrix[i][0] = 0

                # Mark column
                if j != 0:
                    matrix[0][j] = 0

                else:
                    col0 = 0

    # ========================================================
    # STEP 2: FILL INNER MATRIX
    # ========================================================

    for i in range(1, n):

        for j in range(1, m):

            # If row or col is marked
            if matrix[i][0] == 0 or matrix[0][j] == 0:

                matrix[i][j] = 0

    # ========================================================
    # STEP 3: HANDLE FIRST ROW
    # ========================================================

    if matrix[0][0] == 0:

        for j in range(m):

            matrix[0][j] = 0

    # ========================================================
    # STEP 4: HANDLE FIRST COLUMN
    # ========================================================

    if col0 == 0:

        for i in range(n):

            matrix[i][0] = 0

    return matrix


# ============================================================
# DRIVER CODE
# ============================================================

matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

matrix2 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

matrix3 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print("================================================")
print("BRUTE FORCE APPROACH")
print("================================================")

result1 = set_zeroes_brute(matrix1)

for row in result1:
    print(row)

print()

print("================================================")
print("BETTER APPROACH")
print("================================================")

result2 = set_zeroes_better(matrix2)

for row in result2:
    print(row)

print()

print("================================================")
print("OPTIMAL APPROACH")
print("================================================")

result3 = set_zeroes_optimal(matrix3)

for row in result3:
    print(row)