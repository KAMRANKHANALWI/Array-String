# ============================================================
# ROMAN TO INTEGER
# ============================================================
#
# Problem:
#
# Given a Roman numeral,
#
# convert it into
# an integer.
#
#
# Example:
#
# Input:
#
# "III"
#
# Output:
#
# 3
#
#
# Example:
#
# Input:
#
# "IV"
#
# Output:
#
# 4
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Most Roman numerals
# are simply added.
#
#
# Example:
#
# VIII
#
# =
#
# 5 + 1 + 1 + 1
#
# =
#
# 8
#
#
# BUT...
#
# Whenever a smaller
# numeral appears
# before a larger numeral,
#
# subtract instead
# of add.
#
#
# Example:
#
# IV
#
# =
#
# 5 - 1
#
# =
#
# 4
#
#
# Therefore,
#
# while traversing
# the string,
#
# compare the
# current value
# with the next value.
#
#
# Current < Next
#
# ->
#
# Subtract
#
#
# Otherwise
#
# ->
#
# Add
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# IDEA:
#
# Store the value
# of every Roman
# numeral inside
# a Hash Map.
#
#
# Traverse the string
# from left to right.
#
#
# If the current value
# is smaller than
# the next value,
#
# subtract it.
#
#
# Otherwise,
#
# add it.
#
#
# TIME  : O(N)
#
# SPACE : O(1)
#
# ============================================================


def roman_to_integer(s):

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    answer = 0

    for i in range(len(s)):

        current = roman[s[i]]

        # If a smaller value
        # comes before a
        # larger value,
        #
        # subtract it.

        if i < len(s) - 1 and current < roman[s[i + 1]]:

            answer -= current

        # Otherwise,
        #
        # simply add it.

        else:

            answer += current

    return answer


# ============================================================
# DRY RUN
# ============================================================
#
# s =
#
# "MCMIV"
#
#
# M
#
# 1000 > 100
#
# Add
#
# Answer = 1000
#
#
# C
#
# 100 < 1000
#
# Subtract
#
# Answer = 900
#
#
# M
#
# 1000 > 1
#
# Add
#
# Answer = 1900
#
#
# I
#
# 1 < 5
#
# Subtract
#
# Answer = 1899
#
#
# V
#
# Last character.
#
# No larger value
# after it.
#
# Add.
#
# Answer = 1904
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
#
# Character Mapping
#
#
# Steps:
#
# Read Character
#
# ↓
#
# Look Ahead
#
# ↓
#
# Current < Next ?
#
# ↓
#
# Yes
#
# ->
#
# Subtract
#
#
# No
#
# ->
#
# Add
#
#
# Used In:
#
# • Roman to Integer
# • Parsing Problems
# • Character Mapping Problems
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

roman = "MCMIV"

print("Roman Numeral :", roman)

print()

print(roman_to_integer(roman))
