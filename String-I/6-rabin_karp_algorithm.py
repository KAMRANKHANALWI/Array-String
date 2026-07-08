# ============================================================
# RABIN-KARP ALGORITHM
# ============================================================
#
# Problem:
#
# Given a text and a pattern,
# find the starting index of the pattern in the text.
#
# If the pattern does not exist,
# return -1.
#
#
# Example:
#
# Text    : "ABABDABACDABABCABAB"
# Pattern : "ABABC"
#
# Output:
# 10
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Instead of comparing characters at every position,
# compare HASH values.
#
# If the hashes are different,
# the strings are definitely different.
#
# If the hashes are equal,
# verify by comparing the actual characters
# (to handle hash collisions).
#
# The hash is updated in O(1) using Rolling Hash.
#
# ============================================================


# ============================================================
# BRUTE FORCE
# ============================================================
#
# Compare the pattern with every possible substring.
#
# Time  : O(N × M)
# Space : O(1)
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# Use Polynomial Hashing + Rolling Hash.
#
# Compute:
# 1. Pattern Hash
# 2. First Window Hash
#
# Then slide the window.
#
# Instead of recomputing the hash,
# update it in O(1).
#
# Average Time : O(N + M)
# Worst Time   : O(N × M) (Many Hash Collisions)
# Space        : O(1)
#
# ============================================================


BASE = 31
MOD = 10**9 + 7


# ------------------------------------------------------------
# Convert:
#
# A -> 1
# B -> 2
# ...
# Z -> 26
# ------------------------------------------------------------
def character_value(character):
    return ord(character) - ord("A") + 1


# ------------------------------------------------------------
# Compute Polynomial Hash.
#
# hash = hash * BASE + value
# ------------------------------------------------------------
def compute_hash(string):

    hash_value = 0

    for character in string:
        hash_value = (hash_value * BASE + character_value(character)) % MOD

    return hash_value


# ------------------------------------------------------------
# Update the previous hash in O(1).
#
# Remove outgoing character
# Shift remaining characters
# Add incoming character
# ------------------------------------------------------------
def recalculate_hash(
    old_hash,
    outgoing_character,
    incoming_character,
    highest_power,
):

    old_hash = (old_hash - character_value(outgoing_character) * highest_power) % MOD

    old_hash = (old_hash * BASE) % MOD

    old_hash = (old_hash + character_value(incoming_character)) % MOD

    return old_hash


# ============================================================
# RABIN-KARP
# ============================================================
def rabin_karp(text, pattern):

    if len(pattern) > len(text):
        return -1

    pattern_length = len(pattern)

    highest_power = pow(BASE, pattern_length - 1, MOD)

    pattern_hash = compute_hash(pattern)

    window_hash = compute_hash(text[:pattern_length])

    for start_index in range(len(text) - pattern_length + 1):

        # Hashes match.
        # Verify actual characters.
        if (
            window_hash == pattern_hash
            and text[start_index : start_index + pattern_length] == pattern
        ):
            return start_index

        # Slide the window.
        if start_index < len(text) - pattern_length:

            window_hash = recalculate_hash(
                window_hash,
                text[start_index],
                text[start_index + pattern_length],
                highest_power,
            )

    return -1


# ============================================================
# DRY RUN
# ============================================================
#
# Text    : ABCDABC
# Pattern : ABC
#
# Pattern Hash
#        ↓
# First Window Hash
#        ↓
# Hash Match?
#        ↓
# Yes → Verify Characters
# No  → Slide Window
#        ↓
# Rolling Hash
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# Rolling Hash
#
# Related Concepts:
# • Sliding Window
# • Polynomial Hashing
# • String Matching
#
# Key Insight:
#
# Sliding Window
#        ↓
# Window Sum
#
# Rabin-Karp
#        ↓
# Window Hash
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

text = "ABABDABACDABABCABAB"
pattern = "ABABC"

print(rabin_karp(text, pattern))
