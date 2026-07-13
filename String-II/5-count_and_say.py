"""
============================================================
Category   : Strings
Difficulty : Medium
Pattern    : Simulation / Run-Length Encoding

LeetCode   : 38. Count and Say
Striver SDE Sheet : Yes
============================================================
"""

# ============================================================
# PROBLEM STATEMENT
# ============================================================
#
# The Count and Say sequence starts with "1".
#
# Each next term describes the consecutive groups
# present in the previous term.
#
# Sequence:
#
# "1" → "11" → "21" → "1211" → "111221" → ...
#
# Given n, return the nth term of this sequence.
#
#
# Example:
#
# n = 5
#
# Output:
# "111221"
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION / INTUITION
# ============================================================
#
# To build the NEXT term, describe the CURRENT term.
#
# Example:
#
# current = "111221"
#
# Groups:
#
# 111 | 22 | 1
#
# Three 1s → 31
# Two 2s   → 22
# One 1    → 11
#
# next = "312211"
#
#
# We count CONSECUTIVE groups, not total frequency.
#
# "111221"
#      ↓
# 111 | 22 | 1
#      ↓
# 31  | 22 | 11
#      ↓
#   "312211"
#
#
# One group scan creates ONE next term.
#
# Starting from "1", repeat this transformation N - 1 times
# to reach the Nth term.
#
# ============================================================


# ============================================================
# APPROACH - SIMULATION / RUN-LENGTH ENCODING
# ============================================================
#
# Start with the first term:
#
# current = "1"
#
# OUTER LOOP:
# Generate the next term N - 1 times.
#
# INNER LOOP:
# Scan the current term and count consecutive equal characters.
#
#
# Same character:
# → Continue the current group.
#
# Different character:
# → The previous group has ended.
# → Append count + previous character.
# → Start a new group.
#
#
# The final group is added manually because no different
# character appears after it to trigger the group-ending logic.
#
#
# Time  : O(L1 + L2 + ... + Ln)
# Space : O(L)
#
# Each term is scanned once to generate the next term.
#
# ============================================================


def count_and_say(n):

    # The sequence always starts with the first term "1".
    current = "1"

    # Outer loop: repeatedly generate the next term.
    for _ in range(n - 1):

        count = 1
        result = ""

        # Inner loop: describe the current term once.
        for i in range(1, len(current)):

            # Same group → keep counting.
            if current[i - 1] == current[i]:
                count += 1

            else:
                # Group ended → write count + character.
                result += str(count) + current[i - 1]

                # Current character starts a new group.
                count = 1

        # No different character comes after the final group,
        # so it must be added manually.
        result += str(count) + current[-1]

        # Move to the newly generated term.
        current = result

    return current


# ============================================================
# DRY RUN
# ============================================================
#
# n = 5
#
# Start:
#
# current = "1"          ← Term 1
#
# Outer Loop 1:
# "1"    → one 1         → "11"
#
# Outer Loop 2:
# "11"   → two 1s        → "21"
#
# Outer Loop 3:
# "21"   → one 2, one 1  → "1211"
#
# Outer Loop 4:
#
# "1211"
#    ↓
# 1 | 2 | 11
#    ↓
# 11 | 12 | 21
#    ↓
# "111221"
#
# Term 5 = "111221"
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# Simulation / Run-Length Encoding
#
# Run-Length Encoding groups consecutive equal values
# and represents each group using:
#
# count + value
#
#
# Example:
#
# aaabbccccd
#      ↓
# aaa | bb | cccc | d
#      ↓
# 3a  | 2b | 4c   | 1d
#      ↓
# "3a2b4c1d"
#
#
# Mental Signal:
#
# Count consecutive equal values
#              ↓
#      Run-Length Encoding
#
#
# For Count and Say:
#
# Inner Loop → Describe ONE term.
# Outer Loop → Generate terms until N.
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

n = 5

print(count_and_say(n))
