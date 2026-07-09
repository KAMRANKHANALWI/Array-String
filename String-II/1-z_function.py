"""
============================================================
Category   : Strings
Difficulty : Hard
Pattern    : Z-Box / Prefix Matching

LeetCode   : -
GFG        : Z Algorithm
Striver SDE Sheet : Yes
============================================================
"""

# ============================================================
# Z FUNCTION (Z ALGORITHM)
# ============================================================
#
# Problem:
#
# For every index i in the string,
# compute the length of the longest substring starting at i
# that matches the prefix of the string.
#
# Example:
#
# String : "aabcaabxaaaz"
#
# Z Array:
# [0,1,0,0,3,1,0,0,2,2,1,0]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# • Z[i] stores the length of the longest prefix match
#   starting from index i.
#
# • Maintain a Z-Box [L, R].
# 
# • Every character inside this box is already known
#   to match the prefix.
#
# • If the current index lies inside the box,
#   reuse previous work instead of comparing again.
#
# • Current Z-Box
#   0 1 2 3 4 5 6 7 8 9
#   a a b c a a b x a a
#           <------->
#           L       R
# ============================================================


# ============================================================
# BRUTE FORCE
# ============================================================
#
# Idea:
# For every index,
# compare characters with the prefix one by one.
#
# Time  : O(N²)
# Space : O(N)
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# Idea:
#
# Maintain the current Z-Box [L, R].
#
# Case 1:
# Outside the box
# → Compare characters manually.
#
# Case 2:
# Inside the box
# → Copy previously computed information.
#
# If the copied answer reaches the boundary,
# continue matching beyond the box.
#
# Time  : O(N)
# Space : O(N)
#
# ============================================================


def z_function(string):

    length = len(string)

    # Result array
    z = [0] * length

    # Current Z-Box
    left = 0
    right = 0

    # Start from index 1 because Z[0] = 0 by convention
    for index in range(1, length):

        # ----------------------------------------------------
        # CASE 1
        # Current index is inside the Z-Box.
        # Reuse previously computed information.
        # ----------------------------------------------------
        if index <= right:

            mirror = index - left

            z[index] = min(
                z[mirror],
                right - index + 1,
            )

        # ----------------------------------------------------
        # Expand beyond the current Z-Box if possible.
        # ----------------------------------------------------
        while (
            index + z[index] < length and string[z[index]] == string[index + z[index]]
        ):
            z[index] += 1

        # ----------------------------------------------------
        # If expansion created a larger Z-Box,
        # update its boundaries.
        # ----------------------------------------------------
        if index + z[index] - 1 > right:

            left = index
            right = index + z[index] - 1

    return z


# ============================================================
# DRY RUN
# ============================================================
#
# String:
# aabcaabxaaaz
#
# i = 4
#
# Match:
#
# Prefix : aab
# Current: aab
#
# Z[4] = 3
#
# New Z-Box:
#
# L = 4
# R = 6
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# Prefix Matching
#
# Core Idea:
# Maintain a window where the prefix is already known
# to match, and reuse that information.
#
# Related Problems:
# • KMP Algorithm
# • Longest Common Prefix
#
# ============================================================


# ============================================================
# CONNECTIONS
# ============================================================
#
# Longest Common Prefix
# → Compare prefixes.
#
# Rabin-Karp
# → Reuses previous work using Rolling Hash.
#
# KMP
# → Reuses previous work using LPS Array.
#
# Z Algorithm
# → Reuses previous work using the Z-Box.
#
# ============================================================


# ============================================================
# INTERVIEW CHEAT SHEET
# ============================================================
#
# ✓ Z[i] = Longest Prefix Match starting at i.
#
# ✓ Maintain Z-Box [L, R].
#
# ✓ Outside Box
#   → Brute Force Matching.
#
# ✓ Inside Box
#   → Copy min(Z[mirror], Remaining Box Length).
#
# ✓ Expand only if necessary.
#
# ✓ Time  : O(N)
# ✓ Space : O(N)
#
# Mental Model:
#
# Think of the Z-Box as a cache that stores
# an interval where prefix matches are already known.
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

string = "aabcaabxaaaz"

print(z_function(string))
