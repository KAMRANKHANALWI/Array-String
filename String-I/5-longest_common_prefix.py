# ============================================================
# LONGEST COMMON PREFIX
# ============================================================
#
# Problem:
#
# Given an array of strings,
# find the longest common prefix.
#
# If no common prefix exists,
# return an empty string "".
#
# Example:
#
# Input:
# ["flower", "flow", "flight"]
#
# Output:
# "fl"
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# A prefix always starts from index 0.
#
# Instead of generating every possible prefix,
# compare one character position across all strings.
#
# The first mismatch immediately ends the common prefix.
#
# This technique is called Vertical Scanning.
#
# ============================================================


# ============================================================
# BRUTE FORCE
# ============================================================
#
# Idea:
# Generate every prefix of the first string and check whether
# every other string starts with it.
#
# Time  : O(N × M²)
# Space : O(1)
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# Idea:
# Use the first string as a reference.
#
# Compare each character with the corresponding character
# in every other string.
#
# Stop immediately when:
# 1. A string becomes shorter.
# 2. Characters don't match.
#
# Time  : O(N × M)
# Space : O(1)
#
# ============================================================


def longest_common_prefix(strings):

    # Empty array
    if not strings:
        return ""

    # Reference string
    first_string = strings[0]

    # Compare every character of the reference string
    for index in range(len(first_string)):

        # Character that every string should match
        current_character = first_string[index]

        for word in strings[1:]:

            # Stop if the string ends or characters differ
            if index >= len(word) or word[index] != current_character:
                return first_string[:index]

    # Every character matched
    return first_string


# ============================================================
# DRY RUN
# ============================================================
#
# strings = ["flower", "flow", "flight"]
#
# Index 0 -> 'f' ✔
# Index 1 -> 'l' ✔
# Index 2 -> 'o' != 'i' ✘
#
# Return:
# "fl"
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# Vertical Scanning
#
# Steps:
#
# Pick First String
#        ↓
# Compare One Character Position Across All Strings
#        ↓
# Mismatch?
#        ↓
# Yes → Return Prefix
# No  → Continue
#
# Used In:
# • Longest Common Prefix
# • Character-by-Character Validation
# • Trie-related Problems
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

strings = ["flower", "flow", "flight"]

print(longest_common_prefix(strings))