"""
============================================================
Category   : Strings
Difficulty : Easy
Pattern    : Frequency Counting / Character Mapping

LeetCode   : 242. Valid Anagram
Striver SDE Sheet : Yes
============================================================
"""

# ============================================================
# PROBLEM STATEMENT
# ============================================================
#
# Given two strings s and t, return True if t is an
# anagram of s. Otherwise, return False.
#
# An anagram contains exactly the same characters with
# exactly the same frequencies, but the order may differ.
#
#
# Example:
#
# s = "anagram"
# t = "nagaram"
#
# Output:
# True
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION / INTUITION
# ============================================================
#
# The order of characters does NOT matter.
#
# What matters is:
#
# "Does every character appear the same number of times
#  in both strings?"
#
#
# Therefore:
#
# Order does not matter
#         ↓
# Exact occurrences matter
#         ↓
# Frequency Counting
#
#
# We can think of it like a balance:
#
# Characters from s → Increase frequency
# Characters from t → Decrease frequency
#
# If every frequency becomes 0, both strings contain
# exactly the same characters in exactly the same counts.
#
# ============================================================


# ============================================================
# BRUTE FORCE - SORTING
# ============================================================
#
# Sort both strings and compare them.
#
# Sorting removes the effect of character order.
#
# Example:
#
# "listen" → "eilnst"
# "silent" → "eilnst"
#
# Both sorted strings are equal, so they are anagrams.
#
#
# Time  : O(N log N)
# Space : O(N)
#
#
# Improvement:
#
# We do not actually need the characters in sorted order.
# We only need to know how many times each character occurs.
#
# Therefore, frequency counting avoids sorting.
#
# ============================================================


def is_anagram_sorting(s, t):

    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


# ============================================================
# OPTIMAL APPROACH - FREQUENCY COUNTING
# ============================================================
#
# The problem guarantees lowercase English letters.
#
# Therefore, only 26 possible characters exist:
#
# a, b, c, ... z
#
# We use an array of size 26 and map:
#
# a → 0
# b → 1
# c → 2
# ...
# z → 25
#
#
# Mapping Formula:
#
# ord(character) - ord('a')
#
#
# Example:
#
# ord('c') - ord('a')
#
# = 99 - 97
# = 2
#
# Therefore, 'c' maps to index 2.
#
#
# Time  : O(N)
# Space : O(1)
#
# Why O(1) space?
#
# The frequency array always contains exactly 26 positions.
# Its size does not grow with the input.
#
# ============================================================


def is_anagram(s, t):

    # An anagram only rearranges existing characters.
    # Different lengths can never form anagrams.
    if len(s) != len(t):
        return False

    frequency = [0] * 26

    # Characters from s increase the balance.
    for ch in s:

        index = ord(ch) - ord("a")

        frequency[index] += 1

    # Characters from t cancel the balance.
    for ch in t:

        index = ord(ch) - ord("a")

        frequency[index] -= 1

    # Every character must be perfectly balanced.
    for count in frequency:

        if count != 0:
            return False

    return True


# ============================================================
# DRY RUN
# ============================================================
#
# s = "anagram"
# t = "nagaram"
#
#
# After processing s:
#
# a → 3
# n → 1
# g → 1
# r → 1
# m → 1
#
#
# Now process t and decrease frequencies:
#
# n → 0
# a → 2
# g → 0
# a → 1
# r → 0
# a → 0
# m → 0
#
#
# Final frequency balance:
#
# a → 0
# n → 0
# g → 0
# r → 0
# m → 0
#
# Every character is balanced.
#
# Answer = True
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# Frequency Counting / Character Mapping
#
#
# Think about frequency counting when:
#
# ✓ Character order does not matter.
#
# ✓ The number of occurrences matters.
#
# ✓ Two collections need to contain the same elements
#   with the same counts.
#
#
# Mental Signal:
#
# "Order irrelevant + exact occurrences matter"
#
#                 ↓
#
#          FREQUENCY COUNTING
#
#
# Common Problems:
#
# • Valid Anagram
# • Ransom Note
# • Find All Anagrams in a String
# • Group Anagrams
#
# ============================================================


# ============================================================
# INTERVIEW CHEAT SHEET
# ============================================================
#
# 1. Different lengths?
#    → Immediately return False.
#
# 2. Create a frequency array of size 26.
#
# 3. First string:
#    → Increase frequencies.
#
# 4. Second string:
#    → Decrease frequencies.
#
# 5. Any non-zero frequency?
#    → Not an anagram.
#
#
# Mental Model:
#
# s deposits characters.
#
# t withdraws characters.
#
# Final balance must be 0 everywhere.
#
#
# Time  : O(N)
# Space : O(1)
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

s = "anagram"
t = "nagaram"

print(is_anagram(s, t))
