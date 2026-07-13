"""
============================================================
Category   : Strings
Difficulty : Medium
Pattern    : String Parsing / Two Pointers

LeetCode   : 165. Compare Version Numbers
Striver SDE Sheet : Yes
============================================================
"""

# ============================================================
# PROBLEM STATEMENT
# ============================================================
#
# Given two version strings, compare their revisions from
# left to right.
#
# Return:
#
# -1 → version1 < version2
#  1 → version1 > version2
#  0 → version1 == version2
#
#
# Example:
#
# version1 = "1.2"
# version2 = "1.10"
#
# Compare:
#
# 1 == 1
# 2 < 10
#
# Output:
# -1
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION / INTUITION
# ============================================================
#
# A version is a sequence of integer revisions separated
# by dots.
#
# Example:
#
# "1.10.3"
#     ↓
# 1 | 10 | 3
#
# We compare corresponding revisions from left to right.
#
# The FIRST unequal revision decides the answer.
#
#
# Important:
#
# Revisions must be compared as INTEGERS, not strings.
#
# "10" and "2" as strings may compare character by character,
# but numerically:
#
# 10 > 2
#
#
# Integer conversion also ignores leading zeros:
#
# "01"  → 1
# "001" → 1
#
#
# If one version has fewer revisions, missing revisions
# are treated as 0.
#
# "1.0"   → 1 | 0 | 0
# "1.0.0" → 1 | 0 | 0
#
# Therefore, both versions are equal.
#
# ============================================================


# ============================================================
# BETTER APPROACH - SPLIT AND COMPARE
# ============================================================
#
# Split both versions using ".".
#
# "1.10.3"
#     ↓
# ["1", "10", "3"]
#
# Compare corresponding revisions as integers.
#
# Loop until the longer list ends.
#
# If a revision is missing from the shorter version,
# treat it as 0.
#
#
# Time  : O(N + M)
# Space : O(N + M)
#
# The split lists require extra space.
#
# ============================================================


def compare_versions_split(version1, version2):

    parts1 = version1.split(".")
    parts2 = version2.split(".")

    max_length = max(len(parts1), len(parts2))

    for i in range(max_length):

        # Missing revisions are treated as 0.
        revision1 = int(parts1[i]) if i < len(parts1) else 0
        revision2 = int(parts2[i]) if i < len(parts2) else 0

        # The first unequal revision decides the answer.
        if revision1 < revision2:
            return -1

        if revision1 > revision2:
            return 1

    return 0


# ============================================================
# OPTIMAL APPROACH - TWO POINTERS / MANUAL PARSING
# ============================================================
#
# Instead of creating split lists, read one revision at
# a time directly from both version strings.
#
# i → reads version1
# j → reads version2
#
#
# To manually build a revision:
#
# revision = revision * 10 + digit
#
# Example: "123"
#
# 0 * 10 + 1 = 1
# 1 * 10 + 2 = 12
# 12 * 10 + 3 = 123
#
#
# Keep reading digits until "." or the end of the string.
#
# Then:
#
# Compare revision1 and revision2.
#
# Equal?
# → Move past "." and parse the next revisions.
#
# Unequal?
# → Return immediately.
#
#
# The outer loop uses OR:
#
# while version1 remains OR version2 remains
#
# because one version may contain extra revisions.
#
# Missing revisions naturally remain 0.
#
#
# Time  : O(N + M)
# Space : O(1)
#
# ============================================================


def compare_versions(version1, version2):

    i = 0
    j = 0

    n = len(version1)
    m = len(version2)

    # Keep comparing while either version still has
    # revisions left to process.
    while i < n or j < m:

        revision1 = 0
        revision2 = 0

        # Build one revision from version1 digit by digit.
        while i < n and version1[i] != ".":

            revision1 = revision1 * 10 + int(version1[i])

            i += 1

        # Build one revision from version2 digit by digit.
        while j < m and version2[j] != ".":

            revision2 = revision2 * 10 + int(version2[j])

            j += 1

        # The first unequal revision decides the answer.
        if revision1 < revision2:
            return -1

        if revision1 > revision2:
            return 1

        # The parsing loops stop at ".".
        # Move past the separators to the next revisions.
        i += 1
        j += 1

    return 0


# ============================================================
# DRY RUN
# ============================================================
#
# version1 = "1.01"
# version2 = "1.001.0"
#
#
# Round 1:
#
# revision1 = 1
# revision2 = 1
#
# Equal → continue.
#
#
# Round 2:
#
# "01"  → 1
# "001" → 1
#
# Equal → continue.
#
#
# Round 3:
#
# version1 has ended.
#
# revision1 = 0
#
# version2:
#
# revision2 = 0
#
# Equal → continue.
#
#
# No unequal revision was found.
#
# Answer = 0
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# String Parsing / Two Pointers
#
#
# A structured string may contain meaningful components
# separated by delimiters.
#
# Here:
#
# Version String
#       ↓
# Dot-Separated Revisions
#       ↓
# Parse One Revision
#       ↓
# Compare
#       ↓
# Move to Next Revision
#
#
# Manual Number Parsing:
#
# number = number * 10 + digit
#
#
# Connection:
#
# ATOI
# → Build one integer digit by digit.
#
# Compare Version Numbers
# → Build one revision digit by digit.
# → Stop at ".".
# → Compare.
# → Repeat.
#
#
# Mental Signal:
#
# Delimiter-separated numeric components
#                 ↓
#      Manual Parsing / Two Pointers
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

version1 = "1.01"
version2 = "1.001.0"

print(compare_versions(version1, version2))
