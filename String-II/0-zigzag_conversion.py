"""
============================================================
Category   : Strings
Difficulty : Medium
Pattern    : Simulation / State Machine

LeetCode   : 6. Zigzag Conversion
GFG        : -
Striver SDE Sheet : Extra
============================================================
"""

# ============================================================
# ZIGZAG CONVERSION
# ============================================================
#
# Problem:
#
# Arrange the given string in a zigzag pattern using the given
# number of rows, then read the rows one by one.
#
# Example:
#
# Input:
# s = "PAYPALISHIRING"
# numRows = 3
#
# Zigzag:
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# Output:
# "PAHNAPLSIIGYIR"
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Instead of building the zigzag matrix,
# simulate the movement of a pen.
#
# Keep track of:
#
# • Current Row
# • Current Direction
#
# Append each character to its row.
# Finally, join all rows together.
#
# ============================================================


# ============================================================
# BRUTE FORCE
# ============================================================
#
# Idea:
#
# Build the complete zigzag matrix,
# then read it row by row.
#
# Time  : O(N)
# Space : O(N × numRows)
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# Idea:
#
# Simulate writing characters.
#
# Maintain:
#
# • Current Row
# • Current Direction
#
# Reverse the direction whenever
# the first or last row is reached.
#
# Time  : O(N)
# Space : O(N)
#
# ============================================================


def zigzag_conversion(s, numRows):

    # Zigzag doesn't exist with only one row.
    if numRows == 1:
        return s

    # --------------------------------------------------------
    # i -> Current Row
    # d -> Current Direction
    #
    # d =  1 → Moving Down
    # d = -1 → Moving Up
    # --------------------------------------------------------
    i = 0
    d = 1

    # Store characters of every row separately.
    rows = [[] for _ in range(numRows)]

    for character in s:

        rows[i].append(character)

        # Change direction at the top row.
        if i == 0:
            d = 1

        # Change direction at the bottom row.
        elif i == numRows - 1:
            d = -1

        # Move to the next row.
        i += d

    # Join all rows to build the final answer.
    answer = ""

    for row in rows:
        answer += "".join(row)

    return answer


# ============================================================
# DRY RUN
# ============================================================
#
# s = "PAYPALISHIRING"
# numRows = 3
#
# Step-by-step:
#
# Row 0 : P A H N
# Row 1 : A P L S I I G
# Row 2 : Y I R
#
# Final Answer:
#
# PAHNAPLSIIGYIR
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# Simulation
#
# Core Idea:
#
# Simulate the movement instead of
# constructing the complete structure.
#
# Related Problems:
#
# • Spiral Matrix
# • Robot Return to Origin
# • Game Simulation Problems
#
# ============================================================


# ============================================================
# CONNECTIONS
# ============================================================
#
# Spiral Matrix
# → Simulate movement.
#
# Robot Movement
# → Maintain current direction.
#
# Sliding Window
# → Maintain current window.
#
# Zigzag Conversion
# → Maintain current row and direction.
#
# ============================================================


# ============================================================
# INTERVIEW CHEAT SHEET
# ============================================================
#
# ✓ Maintain current row.
#
# ✓ Maintain direction.
#
# ✓ Top Row
#   → Move Down.
#
# ✓ Bottom Row
#   → Move Up.
#
# ✓ Append every character to its row.
#
# ✓ Join all rows at the end.
#
# Time  : O(N)
# Space : O(N)
#
# Mental Model:
#
# Imagine a pen moving up and down
# while writing characters.
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

s = "PAYPALISHIRING"
numRows = 3

print(zigzag_conversion(s, numRows))