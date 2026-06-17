# ============================================================
# PASCAL TRIANGLE
# ============================================================
#
# Pascal Triangle Problems:
#
# 1. Find Element at (Row, Col)
# 2. Print Nth Row
# 3. Print Entire Pascal Triangle
#
# Core Formula:
#
# element = (row - 1) C (col - 1)
#
# Example:
#
# Row 1            1
#
# Row 2          1   1
#
# Row 3        1   2   1
#
# Row 4      1   3   3   1
#
# Row 5    1   4   6   4   1
#
# Row 6  1   5  10  10   5   1
#
# Every value in Pascal Triangle can be represented as:
#
# (row - 1) C (col - 1)
#
# ============================================================


# ============================================================
# HELPER FUNCTION : nCr
# ============================================================

# GOLDEN OBSERVATION
# ==================
#
# Every element in Pascal Triangle is nothing but:
#
# nCr
#
# Example:
#
# Row 6:
#
# 1   5   10   10   5   1
#
# can be written as:
#
# 5C0  5C1  5C2  5C3  5C4  5C5
#
# Therefore:
#
# If we know how to calculate nCr efficiently,
# we can solve all Pascal Triangle problems.
#
#
# ------------------------------------------------------------
# STANDARD FORMULA
# ------------------------------------------------------------
#
# nCr = n! / (r! * (n-r)!)
#
# Example:
#
# 5C2
#
# = 5! / (2! * 3!)
#
# = (5×4×3×2×1) / [(2×1)(3×2×1)]
#
# Many terms cancel:
#
# = (5×4) / (2×1)
#
# = 10
#
#
# ------------------------------------------------------------
# PROBLEM WITH FACTORIALS
# ------------------------------------------------------------
#
# Using factorials:
#
# 1. Extra computation
# 2. Large numbers very quickly
# 3. Unnecessary work because most terms
#    eventually get cancelled
#
#
# ------------------------------------------------------------
# INTUITION FOR OPTIMIZATION
# ------------------------------------------------------------
#
# Instead of calculating:
#
# n!
#
# we directly build only the terms
# that survive after cancellation.
#
# Example:
#
# 5C3
#
# = (5×4×3) / (1×2×3)
#
# Notice:
#
# We never calculated:
#
# 5!
# 3!
# 2!
#
# We directly built the final expression.
#
#
# ------------------------------------------------------------
# MATHEMATICAL FORM
# ------------------------------------------------------------
#
# nCr
#
# = n(n-1)(n-2)...(n-r+1)
# ------------------------
#      1×2×3×...×r
#
#
# Example:
#
# 5C3
#
# = (5×4×3)
# ----------
# (1×2×3)
#
#
# ------------------------------------------------------------
# HOW THE LOOP BUILDS THIS
# ------------------------------------------------------------
#
# Example:
#
# n = 5
# r = 3
#
# result = 1
#
# i = 0
#
# result = result × 5
# result = result / 1
#
# result = 5
#
#
# i = 1
#
# result = result × 4
# result = result / 2
#
# result = 10
#
#
# i = 2
#
# result = result × 3
# result = result / 3
#
# result = 10
#
#
# Final Answer:
#
# 5C3 = 10
#
#
# ------------------------------------------------------------
# STRIVER'S GOLDEN IDEA
# ------------------------------------------------------------
#
# Don't calculate factorials.
#
# Build nCr incrementally:
#
# result *= (n - i)
# result /= (i + 1)
#
# At every step:
#
# Multiply one numerator term
# Divide one denominator term
#
#
# FORMULA:
#
# nCr = n! / (r! * (n-r)!)
#
# Instead of calculating factorials,
# we use the optimized multiplicative formula:
#
# nCr =
#
# n * (n-1) * (n-2) * ...
# -------------------------
# r * (r-1) * (r-2) * ...
#
# This gives:
#
# TIME  : O(r)
# SPACE : O(1)
#
#
# ============================================================


def nCr(n, r):

    result = 1

    for i in range(r):

        result = result * (n - i)
        result = result // (i + 1)

    return result


# ============================================================
# 1. FIND ELEMENT AT (ROW, COL)
# ============================================================
#
# IDEA:
# -----
#
# Element at:
#
# row = R
# col = C
#
# is:
#
# (R-1) C (C-1)
#
# Example:
#
# row = 5
# col = 3
#
# = 4C2
# = 6
#
# TIME  : O(col)
# SPACE : O(1)
#
# ============================================================


def find_element(row, col):

    return nCr(row - 1, col - 1)


# ============================================================
# 2. PRINT NTH ROW OF PASCAL TRIANGLE
# ============================================================
#
# Example:
#
# row = 5
#
# Output:
#
# [1, 4, 6, 4, 1]
#
# STRIVER'S OPTIMIZATION:
# -----------------------
#
# Instead of calculating:
#
# 4C0
# 4C1
# 4C2
# 4C3
# 4C4
#
# separately,
#
# generate the next element from
# the previous element.
#
# Formula:
#
# next_element =
#
# current_element * (row - col)
# --------------------------------
#             col
#
# TIME  : O(N)
# SPACE : O(N)
#
# ============================================================


def generate_row(row):

    ans = 1

    row_values = [1]

    for col in range(1, row):

        ans = ans * (row - col)
        ans = ans // col

        row_values.append(ans)

    return row_values


# ============================================================
# 3. BRUTE FORCE APPROACH
# ============================================================
#
# IDEA:
# -----
#
# For every position:
#
# (row-1)C(col-1)
#
# calculate using nCr()
#
# Example:
#
# Row 5:
#
# 4C0 4C1 4C2 4C3 4C4
#
# TIME  : O(N^3)
# SPACE : O(N^2)
#
# ============================================================


def pascal_triangle_brute(n):

    triangle = []

    for row in range(1, n + 1):

        current_row = []

        for col in range(1, row + 1):

            current_row.append(nCr(row - 1, col - 1))

        triangle.append(current_row)

    return triangle


# ============================================================
# 4. OPTIMAL APPROACH
# ============================================================
#
# IDEA:
# -----
#
# Generate every row in O(row)
#
# using the optimized relation:
#
# next_element =
#
# current_element * (row - col)
# --------------------------------
#             col
#
# Then generate all rows.
#
# TIME  : O(N^2)
# SPACE : O(N^2)
#
# ============================================================


def pascal_triangle_optimal(n):

    triangle = []

    for row in range(1, n + 1):

        triangle.append(generate_row(row))

    return triangle


# ============================================================
# DRIVER CODE
# ============================================================

print("================================================")
print("1. FIND ELEMENT AT (ROW, COL)")
print("================================================")

row = 5
col = 3

print(f"Row = {row}, Col = {col}")
print("Answer =", find_element(row, col))

print()

print("================================================")
print("2. PRINT NTH ROW")
print("================================================")

row_number = 5

print(f"Row = {row_number}")
print(generate_row(row_number))

print()

print("================================================")
print("3. PRINT ENTIRE PASCAL TRIANGLE (BRUTE)")
print("================================================")

triangle_brute = pascal_triangle_brute(6)

for row in triangle_brute:
    print(row)

print()

print("================================================")
print("4. PRINT ENTIRE PASCAL TRIANGLE (OPTIMAL)")
print("================================================")

triangle_optimal = pascal_triangle_optimal(6)

for row in triangle_optimal:
    print(row)
