# ============================================================
# GRID UNIQUE PATHS
# ============================================================
#
# Problem:
#
# You are standing at the
# Top-Left corner of an m x n grid.
#
# You want to reach the
# Bottom-Right corner.
#
#
# Allowed Moves:
#
# → Right
#
# ↓ Down
#
#
# Find the total number of
# unique paths.
#
#
# Example:
#
# Grid = 3 x 3
#
# S . .
#
# . . .
#
# . . E
#
#
# Answer:
#
# 6
#
# ============================================================


# ============================================================
# WHY THIS IS A DP PROBLEM?
# ============================================================
#
# Imagine standing on a cell.
#
# Example:
#
# S . .
#
# . X .
#
# . . E
#
#
# From X,
# we don't care HOW we reached X.
#
#
# We only care:
#
# "How many ways can I reach
# the destination from here?"
#
#
# No matter how many times
# we arrive at X,
#
# the answer is always the same.
#
#
# Therefore,
#
# we should calculate it once
# and reuse it.
#
#
# This is exactly the idea behind:
#
# Dynamic Programming.
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Think in reverse.
#
# Instead of asking:
#
# "How do I go to destination?"
#
#
# Ask:
#
# "How can I reach THIS cell?"
#
#
# Example:
#
# . ↑ .
#
# ← X .
#
#
# X can only be reached:
#
# From Top
#
# or
#
# From Left
#
#
# Therefore:
#
# Ways(Current Cell)
#
# =
#
# Ways(Top)
#
# +
#
# Ways(Left)
#
#
# This recurrence is the heart
# of the entire problem.
#
#
# Every approach below
# (Recursion, Memoization,
# Tabulation, Space Optimization)
#
# simply implements
# this same relation differently.
#
# ============================================================


# ============================================================
# 1. RECURSION (BRUTE FORCE)
# ============================================================
#
# IDEA:
#
# From every cell,
# we have only two choices:
#
# Go Up
#
# or
#
# Go Left
#
#
# (Equivalent to starting from
# Top-Left and moving Right/Down.)
#
#
# Base Case:
#
# Reach (0,0)
#
# -> Found one valid path.
#
#
# Outside Grid
#
# -> Invalid path.
#
#
# TIME  :
#
# O(2^(m+n))
#
# SPACE :
#
# O(m+n)
#
# ============================================================

def unique_paths_recursive(i, j):

    # Reached starting cell

    if i == 0 and j == 0:

        return 1

    # Outside grid

    if i < 0 or j < 0:

        return 0

    up = unique_paths_recursive(
        i - 1,
        j
    )

    left = unique_paths_recursive(
        i,
        j - 1
    )

    return up + left


# ============================================================
# 2. MEMOIZATION
# (TOP-DOWN DP)
# ============================================================
#
# PROBLEM WITH RECURSION:
#
# Same cells are solved
# again and again.
#
#
# Example:
#
# paths(1,1)
#
# may be calculated
# multiple times.
#
#
# SOLUTION:
#
# Store every answer
# inside a DP table.
#
#
# Before solving:
#
# Check:
#
# dp[i][j]
#
#
# If already computed,
#
# return it immediately.
#
#
# TIME  :
#
# O(m*n)
#
# SPACE :
#
# O(m*n)
#
# ============================================================

def helper(i, j, dp):

    if i == 0 and j == 0:

        return 1

    if i < 0 or j < 0:

        return 0

    if dp[i][j] != -1:

        return dp[i][j]

    up = helper(
        i - 1,
        j,
        dp
    )

    left = helper(
        i,
        j - 1,
        dp
    )

    dp[i][j] = up + left

    return dp[i][j]


def unique_paths_memoization(m, n):

    dp = [

        [-1] * n

        for _ in range(m)

    ]

    return helper(
        m - 1,
        n - 1,
        dp
    )


# ============================================================
# 3. TABULATION
# (BOTTOM-UP DP)
# ============================================================
#
# IDEA:
#
# Instead of solving recursively,
#
# build the answer
# from the beginning.
#
#
# Fill DP table row by row.
#
#
# Base Cell:
#
# dp[0][0] = 1
#
#
# Every other cell:
#
# dp[i][j]
#
# =
#
# dp[i-1][j]
#
# +
#
# dp[i][j-1]
#
#
# Example:
#
# 1 1 1
#
# 1 2 3
#
# 1 3 6
#
#
# Last cell
#
# contains the answer.
#
#
# TIME  :
#
# O(m*n)
#
# SPACE :
#
# O(m*n)
#
# ============================================================

def unique_paths_tabulation(m, n):

    dp = [

        [0] * n

        for _ in range(m)

    ]

    for i in range(m):

        for j in range(n):

            if i == 0 and j == 0:

                dp[i][j] = 1

            else:

                up = 0
                left = 0

                if i > 0:

                    up = dp[i - 1][j]

                if j > 0:

                    left = dp[i][j - 1]

                dp[i][j] = up + left

    return dp[m - 1][n - 1]

# ============================================================
# 4. SPACE OPTIMIZATION
# ============================================================
#
# OBSERVATION:
#
# To calculate the current row,
#
# we only need:
#
# 1. Previous Row
# 2. Current Row
#
#
# We do NOT need the entire
# DP table.
#
#
# Therefore,
#
# Store only one previous row.
#
#
# Example:
#
# Previous Row
#
# 1 2 3
#
#
# Current Row
#
# 1 3 6
#
#
# After finishing current row,
#
# make it the previous row.
#
#
# SPACE reduces from:
#
# O(m*n)
#
# to
#
# O(n)
#
#
# TIME  :
#
# O(m*n)
#
# SPACE :
#
# O(n)
#
# ============================================================

def unique_paths_space_optimized(m, n):

    previous = [0] * n

    for i in range(m):

        current = [0] * n

        for j in range(n):

            if i == 0 and j == 0:

                current[j] = 1

            else:

                up = 0
                left = 0

                if i > 0:

                    up = previous[j]

                if j > 0:

                    left = current[j - 1]

                current[j] = up + left

        previous = current

    return previous[n - 1]


# ============================================================
# 5. MATHEMATICAL SOLUTION
# ============================================================
#
# GOLDEN OBSERVATION:
#
# To reach the destination,
#
# Total Moves =
#
# (m-1) Down
#
# +
#
# (n-1) Right
#
#
# Example:
#
# Grid = 3 x 7
#
#
# Down Moves:
#
# 2
#
#
# Right Moves:
#
# 6
#
#
# Total Moves:
#
# 8
#
#
# Now the problem becomes:
#
# Out of 8 positions,
#
# choose 2 positions
# for Down moves.
#
#
# Remaining positions
# automatically become
# Right moves.
#
#
# Therefore:
#
# Answer =
#
# 8C2
#
#
# We compute nCr using
# the optimized multiplicative
# formula learned earlier
# in Pascal Triangle.
#
#
# TIME  :
#
# O(min(m,n))
#
# SPACE :
#
# O(1)
#
# ============================================================

def unique_paths_math(m, n):

    total_moves = (m - 1) + (n - 1)

    down_moves = m - 1

    r = min(
        down_moves,
        total_moves - down_moves
    )

    answer = 1

    for i in range(r):

        answer *= (
            total_moves - i
        )

        answer //= (
            i + 1
        )

    return answer


# ============================================================
# DRIVER CODE
# ============================================================

m = 3
n = 7

print("================================================")
print("GRID SIZE")
print("================================================")

print(f"Rows    = {m}")
print(f"Columns = {n}")

print()

print("================================================")
print("1. RECURSION")
print("================================================")

print(
    "Unique Paths =",
    unique_paths_recursive(
        m - 1,
        n - 1
    )
)

print()

print("================================================")
print("2. MEMOIZATION")
print("================================================")

print(
    "Unique Paths =",
    unique_paths_memoization(
        m,
        n
    )
)

print()

print("================================================")
print("3. TABULATION")
print("================================================")

print(
    "Unique Paths =",
    unique_paths_tabulation(
        m,
        n
    )
)

print()

print("================================================")
print("4. SPACE OPTIMIZATION")
print("================================================")

print(
    "Unique Paths =",
    unique_paths_space_optimized(
        m,
        n
    )
)

print()

print("================================================")
print("5. MATHEMATICAL SOLUTION")
print("================================================")

print(
    "Unique Paths =",
    unique_paths_math(
        m,
        n
    )
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

m = 3
n = 3

print(f"Rows    = {m}")
print(f"Columns = {n}")

print(
    "Unique Paths =",
    unique_paths_math(
        m,
        n
    )
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Recursion          -> O(2^(m+n)), O(m+n)")
print("Memoization        -> O(m*n),     O(m*n)")
print("Tabulation         -> O(m*n),     O(m*n)")
print("Space Optimized    -> O(m*n),     O(n)")
print("Mathematical (nCr) -> O(min(m,n)), O(1)")