# ============================================================
# STRING TO INTEGER (ATOI)
# ============================================================
#
# Problem:
#
# Implement the
# atoi() function.
#
#
# The function should:
#
# 1. Ignore leading spaces.
#
# 2. Read an optional
#    '+' or '-'.
#
# 3. Read digits.
#
# 4. Stop at the first
#    non-digit character.
#
# 5. Return the integer.
#
#
# If the value exceeds
# the 32-bit signed
# integer range,
#
# clamp it.
#
#
# Range:
#
# [-2147483648,
#   2147483647]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Think exactly like
# a human reading
# a number.
#
#
# Example:
#
# "   -123abc"
#
#
# Step 1
#
# Ignore spaces.
#
#
# Step 2
#
# Detect '-'.
#
#
# Step 3
#
# Read:
#
# 1
#
# 2
#
# 3
#
#
# Step 4
#
# Encounter:
#
# a
#
# Stop reading.
#
#
# Step 5
#
# Apply the sign.
#
#
# Step 6
#
# If the answer
# exceeds the
# 32-bit range,
#
# clamp it.
#
#
# This problem
# introduces
#
# String Parsing.
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# IDEA:
#
# Traverse the string
# from left to right.
#
#
# Skip leading spaces.
#
#
# Detect the sign.
#
#
# Read digits
# one by one.
#
#
# Build the number
# using:
#
# number
#
# =
#
# number × 10
#
# +
#
# current_digit
#
#
# Stop when a
# non-digit appears.
#
#
# Finally,
#
# apply the sign
#
# and clamp
# the answer.
#
#
# TIME  : O(N)
#
# SPACE : O(1)
#
# ============================================================


def my_atoi(s):

    index = 0

    n = len(s)

    sign = 1

    number = 0

    INT_MAX = 2147483647

    INT_MIN = -2147483648

    # --------------------------------------------------------
    # Skip all leading spaces.
    # --------------------------------------------------------

    while index < n and s[index] == " ":

        index += 1

    # --------------------------------------------------------
    # Read the sign.
    # --------------------------------------------------------

    if index < n and (s[index] == "+" or s[index] == "-"):

        if s[index] == "-":

            sign = -1

        index += 1

    # --------------------------------------------------------
    # Read digits.
    # --------------------------------------------------------

    while index < n and s[index].isdigit():

        # Convert the
        # character into
        # an integer.
        #
        # Example:
        #
        # "7"
        #
        # becomes
        #
        # 7

        digit = int(s[index])

        # Another way
        # (commonly used
        # in C/C++):
        #
        # digit =
        #
        # ord(s[index])
        #
        # -
        #
        # ord("0")
        #
        # ord()
        # returns the
        # ASCII value.
        #
        # Example:
        #
        # ord("7") = 55
        #
        # ord("0") = 48
        #
        # 55 - 48 = 7

        # digit = ord(s[index]) - ord("0")

        number = number * 10 + digit

        index += 1

    # --------------------------------------------------------
    # Apply the sign.
    # --------------------------------------------------------

    number *= sign

    # --------------------------------------------------------
    # Clamp the answer
    # inside the
    # 32-bit range.
    # --------------------------------------------------------

    if number > INT_MAX:

        return INT_MAX

    if number < INT_MIN:

        return INT_MIN

    return number


# ============================================================
# DRY RUN
# ============================================================
#
# s =
#
# "   -123abc"
#
#
# Skip Spaces
#
# ↓
#
# index -> '-'
#
#
# sign = -1
#
#
# Read:
#
# '1'
#
# number = 1
#
#
# Read:
#
# '2'
#
# number = 12
#
#
# Read:
#
# '3'
#
# number = 123
#
#
# Read:
#
# 'a'
#
# Not a digit.
#
# Stop.
#
#
# Apply Sign
#
# number = -123
#
#
# Return:
#
# -123
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
#
# String Parsing
#
#
# Steps:
#
# Skip Spaces
#
# ↓
#
# Read Sign
#
# ↓
#
# Read Digits
#
# ↓
#
# Stop on
# Invalid Character
#
# ↓
#
# Apply Sign
#
# ↓
#
# Clamp Answer
#
#
# Used In:
#
# • ATOI
# • Expression Parsing
# • JSON Parsing
# • CSV Parsing
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

s = "   -123abc"

print("Input :", repr(s))

print()

print(my_atoi(s))
