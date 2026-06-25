# ============================================================
# POW(x, n)
# (Binary Exponentiation / Fast Exponentiation)
# ============================================================
#
# Problem:
#
# Given:
#
# x (base)
# n (exponent)
#
# Compute:
#
# xⁿ
#
#
# Example:
#
# x = 2
# n = 10
#
# Answer:
#
# 1024
#
#
# LeetCode also allows:
#
# Negative exponent.
#
# Example:
#
# 2⁻³
#
# = 1 / 2³
#
# = 1 / 8
#
# = 0.125
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Brute Force:
#
# x × x × x × ...
#
# repeated n times.
#
#
# But notice:
#
# x⁸
#
# =
#
# (x⁴)²
#
#
# x⁴
#
# =
#
# (x²)²
#
#
# Every iteration:
#
# 1. Exponent becomes half.
#
# 2. Base becomes square.
#
#
# Therefore:
#
# n
#
# becomes:
#
# n
#
# ↓
#
# n/2
#
# ↓
#
# n/4
#
# ↓
#
# n/8
#
#
# giving:
#
# O(log n)
#
#
# IMPORTANT:
#
# If exponent is odd,
#
# one copy of x
#
# cannot be paired.
#
#
# Therefore:
#
# multiply it into answer.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Multiply x exactly n times.
#
#
# Example:
#
# 2⁵
#
# =
#
# 2×2×2×2×2
#
#
# TIME  : O(n)
# SPACE : O(1)
#
# ============================================================

def power_brute(x, n):

    if n < 0:

        x = 1 / x
        n = -n

    answer = 1

    for _ in range(n):

        answer *= x

    return answer


# ============================================================
# 2. OPTIMAL
# (BINARY EXPONENTIATION)
# ============================================================
#
# IDEA:
#
# Maintain:
#
# answer
# base
# exponent
#
#
# While exponent > 0:
#
#
# If exponent is odd:
#
# answer *= base
#
#
# Square the base:
#
# base *= base
#
#
# Halve the exponent:
#
# exponent //= 2
#
#
# Example:
#
# x = 2
#
# n = 13
#
#
# answer = 1
#
#
# n = 13 (odd)
#
# answer = 2
#
# base = 4
#
# n = 6
#
#
# n = 6 (even)
#
# answer = 2
#
# base = 16
#
# n = 3
#
#
# n = 3 (odd)
#
# answer = 32
#
# base = 256
#
# n = 1
#
#
# n = 1 (odd)
#
# answer = 8192
#
# n = 0
#
#
# Stop.
#
#
# TIME  : O(log n)
# SPACE : O(1)
#
# ============================================================

def power_optimal(x, n):

    # Handle negative exponent

    if n < 0:

        x = 1 / x
        n = -n

    answer = 1

    while n > 0:

        # Odd exponent
        if n % 2 == 1:

            answer *= x

        # Square the base
        x *= x

        # Halve the exponent
        n //= 2

    return answer


# ============================================================
# DRY RUN SUMMARY
# ============================================================
#
# Example:
#
# x = 2
#
# n = 13
#
#
# ------------------------------------------------------------
# Step
# ------------------------------------------------------------
#
# answer = 1
#
# x = 2
#
# n = 13
#
#
# n is odd
#
# answer = 2
#
# x = 4
#
# n = 6
#
#
# n is even
#
# answer = 2
#
# x = 16
#
# n = 3
#
#
# n is odd
#
# answer = 32
#
# x = 256
#
# n = 1
#
#
# n is odd
#
# answer = 8192
#
# x = 65536
#
# n = 0
#
#
# Final Answer:
#
# 8192
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

x = 2
n = 13

print("================================================")
print("INPUT")
print("================================================")

print("Base     =", x)
print("Exponent =", n)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Answer =",
    power_brute(x, n)
)

print()

print("================================================")
print("2. OPTIMAL (BINARY EXPONENTIATION)")
print("================================================")

print(
    "Answer =",
    power_optimal(x, n)
)

print()

print("================================================")
print("NEGATIVE EXPONENT")
print("================================================")

x = 2
n = -3

print("Base     =", x)
print("Exponent =", n)

print(
    "Answer =",
    power_optimal(x, n)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute   -> O(N),      O(1)")
print("Optimal -> O(log N),  O(1)")