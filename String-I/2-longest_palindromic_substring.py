# ============================================================
# LONGEST PALINDROMIC SUBSTRING
# ============================================================
#
# Problem:
#
# Given a string,
#
# find the longest
# palindromic substring.
#
#
# A palindrome
# reads the same
# from left to right
# and right to left.
#
#
# Example:
#
# Input:
#
# "babad"
#
#
# Output:
#
# "bab"
#
# or
#
# "aba"
#
#
# Both answers
# are correct.
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Every palindrome
# has a CENTER.
#
#
# Odd Length:
#
# racecar
#
#       ↑
#
#
# Even Length:
#
# abba
#
#    ↑ ↑
#
#
# Therefore,
#
# instead of generating
# every substring,
#
# simply try every
# possible center
#
# and expand outward.
#
#
# This reduces
#
# O(N³)
#
# to
#
# O(N²).
#
# ============================================================


# ============================================================
# HELPER FUNCTION
# ============================================================
#
# Expand from
# the given center.
#
#
# Continue expanding
# while:
#
# 1. We are inside
#    the string.
#
# 2. Both characters
#    are equal.
#
#
# Return the
# palindrome found.
#
#
# TIME :
#
# O(N)
#
# ============================================================


def expand_from_center(s, left, right):

    while left >= 0 and right < len(s) and s[left] == s[right]:

        left -= 1

        right += 1

    # Loop stops
    # AFTER crossing
    # the palindrome.
    #
    # Therefore,
    #
    # actual palindrome
    # lies between:
    #
    # left + 1
    #
    # and
    #
    # right - 1

    return s[left + 1 : right]


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Generate every
# substring.
#
#
# Check whether
# it is a palindrome.
#
#
# Keep the longest.
#
#
# TIME  : O(N³)
#
# SPACE : O(1)
#
# ============================================================


def longest_palindrome_brute(s):

    longest = ""

    n = len(s)

    for start in range(n):

        for end in range(start, n):

            substring = s[start : end + 1]

            if substring == substring[::-1]:

                if len(substring) > len(longest):

                    longest = substring

    return longest


# ============================================================
# 2. OPTIMAL
# (EXPAND AROUND CENTER)
# ============================================================
#
# IDEA:
#
# Every palindrome
# has either
#
# One Center
#
# or
#
# Two Centers.
#
#
# For every index,
#
# perform
#
# Odd Expansion
#
# and
#
# Even Expansion.
#
#
# Keep whichever
# palindrome
# is longer.
#
#
# TIME  : O(N²)
#
# SPACE : O(1)
#
# ============================================================


def longest_palindrome_optimal(s):

    longest = ""

    for i in range(len(s)):

        # --------------------------------------------
        # Odd Length Palindrome
        #
        # Example:
        #
        # racecar
        #    ↑
        # --------------------------------------------

        odd = expand_from_center(s, i, i)

        if len(odd) > len(longest):

            longest = odd

        # --------------------------------------------
        # Even Length Palindrome
        #
        # Example:
        #
        # abba
        #   ↑↑
        # --------------------------------------------

        even = expand_from_center(s, i, i + 1)

        if len(even) > len(longest):

            longest = even

    return longest


# ============================================================
# DRY RUN
# ============================================================
#
# s =
#
# "babad"
#
#
# Center = 0
#
# b
#
# Longest = "b"
#
#
# Center = 1
#
# a
#
# Expand:
#
# b == b
#
#
# Palindrome:
#
# "bab"
#
#
# Longest:
#
# "bab"
#
#
# Center = 2
#
# b
#
# Expand:
#
# a == a
#
#
# Palindrome:
#
# "aba"
#
#
# Length is same.
#
#
# Longest
# remains:
#
# "bab"
#
#
# Final Answer:
#
# "bab"
#
# ============================================================
# DRIVER CODE
# ============================================================

s = "babad"

print("Input String :", s)

print()

print("Brute Force")

print(longest_palindrome_brute(s))

print()

print("Optimal")

print(longest_palindrome_optimal(s))
