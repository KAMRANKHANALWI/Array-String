"""
============================================================
Category   : Strings
Difficulty : Hard
Pattern    : Prefix-Suffix Reuse

LeetCode   : 28. Find the Index of the First Occurrence in a String
GFG        : KMP Algorithm
Striver SDE Sheet : Yes
============================================================
"""

# ============================================================
# KMP (KNUTH-MORRIS-PRATT) ALGORITHM
# ============================================================
#
# Problem:
#
# Given a text and a pattern,
# return the starting index of the first occurrence
# of the pattern in the text.
#
# Return -1 if the pattern does not exist.
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
# Naive matching repeats comparisons after every mismatch.
#
# KMP avoids this by remembering how much of the
# pattern is still useful.
#
# This information is stored inside the LPS array.
#
# LPS[i] = Length of the Longest Proper Prefix
#          which is also a Suffix.
#
# ============================================================


# ============================================================
# BRUTE FORCE
# ============================================================
#
# Compare the pattern from every possible position.
#
# Time  : O(N × M)
# Space : O(1)
#
# ============================================================


# ============================================================
# OPTIMAL APPROACH
# ============================================================
#
# Step 1:
# Build the LPS array.
#
# Step 2:
# Use the LPS array while searching.
#
# Whenever a mismatch occurs,
# jump to the next reusable prefix
# instead of starting again.
#
# Time  : O(N + M)
# Space : O(M)
#
# ============================================================


# ------------------------------------------------------------
# BUILD LPS ARRAY
# ------------------------------------------------------------
#
# lps[i] stores the length of the longest proper prefix
# which is also a suffix for pattern[0...i].
#
# ------------------------------------------------------------
def build_lps(pattern):

    length = len(pattern)

    lps = [0] * length

    # Length of current reusable prefix.
    prefix_length = 0

    # Start from second character.
    index = 1

    while index < length:

        # Characters match.
        # Current reusable prefix becomes longer.
        if pattern[index] == pattern[prefix_length]:

            prefix_length += 1

            lps[index] = prefix_length

            index += 1

        else:

            # Try the next smaller reusable prefix.
            if prefix_length != 0:

                prefix_length = lps[prefix_length - 1]

            # No reusable prefix exists.
            else:

                lps[index] = 0

                index += 1

    return lps


# ------------------------------------------------------------
# KMP SEARCH
# ------------------------------------------------------------
def kmp_search(text, pattern):

    if len(pattern) == 0:
        return 0

    lps = build_lps(pattern)

    text_index = 0
    pattern_index = 0

    while text_index < len(text):

        # Characters match.
        if text[text_index] == pattern[pattern_index]:

            text_index += 1
            pattern_index += 1

            # Entire pattern matched.
            if pattern_index == len(pattern):
                return text_index - pattern_index

        else:

            # Reuse previous prefix.
            if pattern_index != 0:

                pattern_index = lps[pattern_index - 1]

            # Move to next character in text.
            else:

                text_index += 1

    return -1


# ============================================================
# DRY RUN
# ============================================================
#
# Pattern:
#
# ABABCABAB
#
# LPS:
#
# 0 0 1 2 0 1 2 3 4
#
# Whenever a mismatch occurs,
# the pattern jumps using the LPS array
# instead of restarting from the beginning.
#
# ============================================================


# ============================================================
# PATTERN LEARNED
# ============================================================
#
# Pattern:
# Prefix-Suffix Reuse
#
# Core Idea:
#
# Reuse previously matched characters
# after every mismatch.
#
# Related Problems:
#
# • Z Algorithm
# • Longest Common Prefix
# • String Matching
#
# ============================================================


# ============================================================
# CONNECTIONS
# ============================================================
#
# Longest Common Prefix
# → Prefix comparison.
#
# Rabin-Karp
# → Reuses previous work using Rolling Hash.
#
# Z Algorithm
# → Reuses previous work using the Z-Box.
#
# KMP
# → Reuses previous work using the LPS array.
#
# ============================================================


# ============================================================
# INTERVIEW CHEAT SHEET
# ============================================================
#
# ✓ LPS stores reusable prefix lengths.
#
# ✓ Match
#   → Increase prefix length.
#
# ✓ Mismatch
#
#   prefix_length > 0
#   → Jump using the LPS array.
#
#   prefix_length == 0
#   → Store 0 and move ahead.
#
# ✓ Search uses the same fallback logic.
#
# Time  : O(N + M)
# Space : O(M)
#
# Mental Model:
#
# Think of the LPS array as a bookmark.
# Whenever a mismatch occurs,
# jump to the previous bookmark
# instead of starting from the beginning.
#
# ============================================================


# ============================================================
# HOW TO RECOGNIZE THIS PATTERN
# ============================================================
#
# Think about KMP when:
#
# ✓ You repeatedly match one pattern
#   inside a larger text.
#
# ✓ Naive matching causes repeated work.
#
# ✓ The pattern contains repeating prefixes.
#
# Ask yourself:
#
# "Can I reuse the already matched part
# instead of comparing it again?"
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

text = "ABABDABACDABABCABAB"
pattern = "ABABC"

print(kmp_search(text, pattern))
