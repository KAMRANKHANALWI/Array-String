# ============================================================
# FIND THE MISSING AND REPEATING NUMBER
# ============================================================
#
# Problem:
#
# Given an array of size:
#
# N
#
# containing numbers from:
#
# 1 to N
#
# Exactly:
#
# One number is missing
# One number is repeating
#
#
# Return:
#
# (repeating, missing)
#
#
# Example:
#
# arr = [4,3,6,2,1,1]
#
#
# Numbers should be:
#
# 1 2 3 4 5 6
#
#
# Actual:
#
# 1 1 2 3 4 6
#
#
# Repeating = 1
# Missing   = 5
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Array should contain:
#
# 1 to N
#
# exactly once.
#
#
# But:
#
# One number appears twice
#
# One number never appears
#
#
# Therefore:
#
# Frequency distribution
# gets disturbed.
#
#
# Let:
#
# x = Repeating Number
# y = Missing Number
#
#
# We need to find:
#
# x and y
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# For every number:
#
# 1 to N
#
# Count its occurrences.
#
#
# count == 2
#
# -> Repeating Number
#
#
# count == 0
#
# -> Missing Number
#
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================


def find_missing_repeating_brute(arr):

    n = len(arr)

    repeating = -1
    missing = -1

    for num in range(1, n + 1):

        count = 0

        for value in arr:

            if value == num:

                count += 1

        if count == 2:

            repeating = num

        elif count == 0:

            missing = num

    return repeating, missing


# ============================================================
# 2. BETTER APPROACH (HASHING)
# ============================================================
#
# IDEA:
#
# Create frequency array.
#
#
# freq[i]
#
# stores frequency of i.
#
#
# Example:
#
# freq[1] = 2
#
# -> Repeating
#
#
# freq[5] = 0
#
# -> Missing
#
#
# TIME  : O(N)
# SPACE : O(N)
#
# ============================================================


def find_missing_repeating_better(arr):

    n = len(arr)

    freq = [0] * (n + 1)

    for num in arr:

        freq[num] += 1

    repeating = -1
    missing = -1

    for num in range(1, n + 1):

        if freq[num] == 2:

            repeating = num

        elif freq[num] == 0:

            missing = num

    return repeating, missing


# ============================================================
# 3. OPTIMAL APPROACH (MATH)
# ============================================================
#
# Let:
#
# x = Repeating Number
# y = Missing Number
#
#
# Expected Sum:
#
# SN = n(n+1)/2
#
#
# Expected Square Sum:
#
# S2N = n(n+1)(2n+1)/6
#
#
# Actual Sum:
#
# S
#
#
# Actual Square Sum:
#
# S2
#
#
# Then:
#
# S - SN
#
# = x - y
#
#
# Let:
#
# val1 = x - y
#
#
# Also:
#
# S2 - S2N
#
# = x² - y²
#
#
# = (x-y)(x+y)
#
#
# Therefore:
#
# val2
#
# =
#
# (x²-y²)/(x-y)
#
# =
#
# x+y
#
#
# Now:
#
# x-y = val1
# x+y = val2
#
#
# Solve:
#
# x = (val1 + val2)/2
#
# y = x - val1
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================


def find_missing_repeating_math(arr):

    n = len(arr)

    expected_sum = (n * (n + 1)) // 2

    expected_square_sum = (n * (n + 1) * (2 * n + 1)) // 6

    actual_sum = 0
    actual_square_sum = 0

    for num in arr:

        actual_sum += num

        actual_square_sum += num * num

    # x - y
    val1 = actual_sum - expected_sum

    # x² - y²
    val2 = actual_square_sum - expected_square_sum

    # x + y
    val2 = val2 // val1

    repeating = (val1 + val2) // 2

    missing = repeating - val1

    return repeating, missing


# ============================================================
# 4. OPTIMAL APPROACH (XOR)
# ============================================================
#
# IDEA:
#
# XOR:
#
# Array Elements
#
# and
#
# Numbers 1 to N
#
#
# Everything cancels except:
#
# Missing XOR Repeating
#
#
# Let:
#
# xr = Missing ^ Repeating
#
#
# Missing and Repeating
# differ in at least one bit.
#
#
# Find:
#
# Rightmost Set Bit
#
#
# Divide all numbers into:
#
# Group 1
# Group 2
#
#
# XOR separately.
#
#
# Eventually:
#
# One bucket gives:
#
# Missing
#
# Other bucket gives:
#
# Repeating
#
#
# Need one extra pass
# to determine which is which.
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================


def find_missing_repeating_xor(arr):

    n = len(arr)

    xr = 0

    for num in arr:

        xr ^= num

    for num in range(1, n + 1):

        xr ^= num

    # Rightmost set bit

    bit_no = xr & -xr

    bucket1 = 0
    bucket2 = 0

    for num in arr:

        if num & bit_no:

            bucket1 ^= num

        else:

            bucket2 ^= num

    for num in range(1, n + 1):

        if num & bit_no:

            bucket1 ^= num

        else:

            bucket2 ^= num

    count = 0

    for num in arr:

        if num == bucket1:

            count += 1

    if count == 2:

        repeating = bucket1
        missing = bucket2

    else:

        repeating = bucket2
        missing = bucket1

    return repeating, missing


# ============================================================
# DRIVER CODE
# ============================================================

arr = [4, 3, 6, 2, 1, 1]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

repeating, missing = find_missing_repeating_brute(arr)

print("Repeating =", repeating)
print("Missing   =", missing)

print()

print("================================================")
print("2. BETTER APPROACH (HASHING)")
print("================================================")

repeating, missing = find_missing_repeating_better(arr)

print("Repeating =", repeating)
print("Missing   =", missing)

print()

print("================================================")
print("3. OPTIMAL APPROACH (MATH)")
print("================================================")

repeating, missing = find_missing_repeating_math(arr)

print("Repeating =", repeating)
print("Missing   =", missing)

print()

print("================================================")
print("4. OPTIMAL APPROACH (XOR)")
print("================================================")

repeating, missing = find_missing_repeating_xor(arr)

print("Repeating =", repeating)
print("Missing   =", missing)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [3, 1, 2, 5, 3]

print("Input =", arr2)

repeating, missing = find_missing_repeating_math(arr2)

print("Repeating =", repeating)
print("Missing   =", missing)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute   -> O(N²), O(1)")
print("Hashing -> O(N),  O(N)")
print("Math    -> O(N),  O(1)")
print("XOR     -> O(N),  O(1)")
