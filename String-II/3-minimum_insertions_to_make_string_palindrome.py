"""
============================================================
Category   : Strings / Dynamic Programming
Difficulty : Hard
Pattern    : LCS Family / Longest Palindromic Subsequence

Problem:
Minimum Insertions to Make a String Palindrome

LeetCode 1312:
Minimum Insertion Steps to Make a String Palindrome
============================================================
"""

# ============================================================
# PROBLEM STATEMENT
# ============================================================
#
# Given a string s, return the minimum number of characters
# we need to INSERT to make s a palindrome.
#
# We can insert a character at any position.
#
#
# Example:
#
# s = "mbadm"
#
# One possible palindrome:
#
# "mbdadbm"
#
# We inserted:
#
# 'd' and 'b'
#
# Answer = 2
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION / INTUITION
# ============================================================
#
# Instead of asking:
#
# "Which characters should I insert?"
#
# ask:
#
# "What is the largest part of the string that is already
#  palindrome-safe?"
#
#
# Example:
#
# s = "mbadm"
#
# A palindromic subsequence is:
#
# m   a   m
# ↑   ↑   ↑
#
# "mam"
#
# These characters already form a palindrome.
# We do NOT need to fix them.
#
#
# The remaining characters are:
#
# b and d
#
# Each remaining character needs a mirror partner.
#
# Therefore:
#
# Minimum Insertions
# =
# Total Characters - Longest Palindromic Subsequence
#
#
#              MINIMUM INSERTIONS = N - LPS
#
#
# So the problem becomes:
#
# Minimum Insertions
#         ↓
# Find Longest Palindromic Subsequence
#
# ============================================================


# ============================================================
# WHY SUBSEQUENCE AND NOT SUBSTRING?
# ============================================================
#
# A substring must be continuous.
#
# A subsequence may skip characters while preserving order.
#
#
# Example:
#
# s = "mbadm"
#
# "mam" is NOT a substring.
#
# But it is a subsequence:
#
# m b a d m
# ↑   ↑   ↑
#
#
# Insertions do not change the relative order of the
# characters already present in the string.
#
# Therefore, subsequence thinking fits this problem naturally.
#
#
# DP SIGNAL:
#
# If order must remain but characters may be skipped,
# think about a SUBSEQUENCE.
#
# ============================================================


# ============================================================
# HOW DO WE FIND THE LONGEST PALINDROMIC SUBSEQUENCE?
# ============================================================
#
# A palindrome reads the same:
#
# Forward  → abcba
# Backward → abcba
#
#
# Therefore, reverse the original string.
#
# Then find the Longest Common Subsequence between:
#
# Original String
# and
# Reversed String
#
#
# Example:
#
# s   = "abcaa"
# rev = "aacba"
#
# One common subsequence is:
#
# "aca"
#
# It is also a palindrome.
#
#
# Therefore:
#
# LPS(s) = LCS(s, reverse(s))
#
#
# Full reduction:
#
# Minimum Insertions
#         ↓
# N - LPS
#         ↓
# N - LCS(s, reverse(s))
#
# ============================================================


# ============================================================
# BRUTE FORCE
# ============================================================
#
# We could generate subsequences and check which ones
# are palindromes.
#
# A string of length N has roughly 2^N subsequences.
#
# Therefore, this approach becomes extremely expensive.
#
# Time  : Exponential
# Space : Depends on recursion / generated subsequences
#
#
# Improvement:
#
# The same smaller subsequence problems repeat many times.
#
# This repeated structure suggests Dynamic Programming.
#
# ============================================================


# ============================================================
# BETTER APPROACH - LCS TABULATION
# ============================================================
#
# Reverse the string and find:
#
# LCS(s, reverse(s))
#
# This gives the Longest Palindromic Subsequence length.
#
#
# DP STATE:
#
# dp[i][j]
#
# means:
#
# "Length of the Longest Common Subsequence between
#  the first i characters of s and
#  the first j characters of rev."
#
#
# We use shifted indexing.
#
# dp[0][j] = 0
# dp[i][0] = 0
#
# Why?
#
# If either string is empty, no common subsequence exists.
#
#
# ------------------------------------------------------------
# CASE 1: CHARACTERS MATCH
# ------------------------------------------------------------
#
# if s[i - 1] == rev[j - 1]:
#
#     dp[i][j] = 1 + dp[i - 1][j - 1]
#
#
# English:
#
# "The characters match.
#  Keep this character and extend the previous
#  common subsequence."
#
#
# We add 1 because the matching character contributes
# to our common subsequence.
#
# Then we move diagonally because both characters
# have now been used.
#
#
# ------------------------------------------------------------
# CASE 2: CHARACTERS DO NOT MATCH
# ------------------------------------------------------------
#
# else:
#
#     dp[i][j] = max(
#         dp[i - 1][j],
#         dp[i][j - 1]
#     )
#
#
# English:
#
# "The characters do not match.
#  Skip one character from either side and
#  preserve the better answer."
#
#
# dp[i - 1][j]
# → Ignore the current character from s.
#
# dp[i][j - 1]
# → Ignore the current character from rev.
#
# We keep the maximum because we want the LONGEST
# common subsequence.
#
#
# Time  : O(N²)
# Space : O(N²)
#
# ============================================================


def minimum_insertions_tabulation(s):

    n = len(s)

    # A palindrome reads the same forward and backward.
    # Comparing the string with its reverse using LCS
    # reveals the longest palindromic subsequence.
    rev = s[::-1]

    # dp[i][j] = LCS length between:
    # first i characters of s
    # first j characters of rev
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):

        for j in range(1, n + 1):

            if s[i - 1] == rev[j - 1]:

                # The characters match.
                # Keep this character and extend the
                # previous common subsequence.
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                # The characters do not match.
                # Skip one character from either side
                # and preserve the better answer.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS(s, reverse(s)) gives the length of the
    # Longest Palindromic Subsequence.
    longest_palindromic_subsequence = dp[n][n]

    # Characters outside the palindromic subsequence
    # need mirror partners to be inserted.
    return n - longest_palindromic_subsequence


# ============================================================
# OPTIMAL APPROACH - SPACE OPTIMIZED LCS
# ============================================================
#
# Look carefully at the LCS recurrence.
#
# To calculate the current row, we only need:
#
# 1. Previous row
# 2. Current row
#
# We do NOT need the complete N × N DP table.
#
#
# previous[j]
# → Value from the previous DP row.
#
# current[j]
# → Value being calculated in the current DP row.
#
#
# Therefore:
#
# O(N²) DP table
#         ↓
# Two arrays of size N + 1
#
#
# Time  : O(N²)
# Space : O(N)
#
# ============================================================


def minimum_insertions(s):

    n = len(s)
    rev = s[::-1]

    # Represents the completed previous DP row.
    previous = [0] * (n + 1)

    for i in range(1, n + 1):

        # A fresh row is created for the current character.
        current = [0] * (n + 1)

        for j in range(1, n + 1):

            if s[i - 1] == rev[j - 1]:

                # The characters match.
                # Keep this character and extend the
                # previous common subsequence.
                current[j] = 1 + previous[j - 1]

            else:

                # The characters do not match.
                # Skip one character from either side
                # and preserve the better answer.
                current[j] = max(previous[j], current[j - 1])

        # The current row is complete.
        # It becomes the previous row for the next iteration.
        previous = current

    longest_palindromic_subsequence = previous[n]

    return n - longest_palindromic_subsequence


# ============================================================
# DRY RUN
# ============================================================
#
# s = "abcaa"
#
# Step 1:
#
# Reverse the string.
#
# s   = "abcaa"
# rev = "aacba"
#
#
# Step 2:
#
# Find LCS(s, rev).
#
# One Longest Common Subsequence:
#
# "aca"
#
# Length = 3
#
#
# Therefore:
#
# Longest Palindromic Subsequence = 3
#
#
# Step 3:
#
# Minimum Insertions
# =
# N - LPS
#
# =
# 5 - 3
#
# =
# 2
#
#
# Mental picture:
#
# Total characters              = 5
# Already palindrome-safe       = 3
# Characters needing partners   = 2
#
# Answer = 2
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# LCS Family / Longest Palindromic Subsequence
#
#
# MAIN REDUCTION:
#
# Minimum Insertions
#         ↓
# Maximize the palindrome-safe part
#         ↓
# Longest Palindromic Subsequence
#         ↓
# LCS(s, reverse(s))
#
#
# Formula:
#
# Minimum Insertions = N - LPS
#
#
# GENERAL DP PATTERN:
#
# Minimize the changes
#         ↓
# Maximize the useful part we can preserve
#
#
# For this problem:
#
# Minimize Insertions
#         ↓
# Maximize Palindromic Subsequence
#
# ============================================================


# ============================================================
# INTERVIEW CHEAT SHEET
# ============================================================
#
# 1. We want to make the string a palindrome.
#
# 2. Preserve the largest part already forming a palindrome.
#
# 3. That part is the Longest Palindromic Subsequence.
#
# 4. Find LPS using:
#
#       LCS(s, reverse(s))
#
# 5. Every remaining character needs a mirror partner.
#
#       Answer = N - LPS
#
#
# LCS RECURRENCE IN ENGLISH:
#
# Characters match?
#
# → Keep the character.
# → Extend the previous common subsequence.
# → 1 + diagonal.
#
#
# Characters do not match?
#
# → Skip one character from either side.
# → Preserve the better answer.
# → max(top, left).
#
#
# Time  : O(N²)
# Space : O(N)   [Space Optimized]
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

s = "abcaa"

print(minimum_insertions(s))
