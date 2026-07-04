# ============================================================
# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ============================================================
#
# Problem:
#
# Given a string,
#
# find the length of the
# longest substring
# without repeating characters.
#
#
# Example:
#
# s = "abcabcbb"
#
#
# Answer:
#
# 3
#
# Because:
#
# "abc"
#
# is the longest substring
# with all unique characters.
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# We need a window
# that always contains
# UNIQUE characters.
#
#
# Whenever a duplicate
# character appears,
#
# shrink the window
# from the left
# until it becomes
# valid again.
#
#
# This is the classic
# Sliding Window pattern.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Generate every
# possible substring.
#
#
# Check whether
# all characters
# are unique.
#
#
# If yes,
#
# update answer.
#
#
# TIME  : O(N³)
#
# SPACE : O(N)
#
# ============================================================

def longest_substring_brute(s):

    n = len(s)

    longest = 0

    for start in range(n):

        for end in range(start, n):

            seen = set()

            valid = True

            for index in range(start, end + 1):

                if s[index] in seen:

                    valid = False

                    break

                seen.add(s[index])

            if valid:

                longest = max(

                    longest,

                    end - start + 1

                )

    return longest


# ============================================================
# 2. BETTER APPROACH
# (SLIDING WINDOW + HASH SET)
# ============================================================
#
# IDEA:
#
# Maintain:
#
# left
#
# right
#
#
# Expand:
#
# right
#
#
# If duplicate appears,
#
# remove characters
# from the left
# until duplicate
# disappears.
#
#
# Window always
# contains unique
# characters.
#
#
# TIME  : O(2N)
#
# SPACE : O(N)
#
# ============================================================

def longest_substring_better(s):

    left = 0

    longest = 0

    seen = set()

    for right in range(len(s)):

        while s[right] in seen:

            seen.remove(

                s[left]

            )

            left += 1

        seen.add(

            s[right]

        )

        longest = max(

            longest,

            right - left + 1

        )

    return longest


# ============================================================
# 3. OPTIMAL
# (SLIDING WINDOW + HASH MAP)
# ============================================================
#
# IDEA:
#
# Instead of removing
# characters one by one,
#
# remember the LAST
# index of every
# character.
#
#
# Whenever duplicate
# appears,
#
# jump left pointer
# directly.
#
#
# left =
#
# max(
#
# left,
#
# last_index + 1
#
# )
#
#
# TIME  : O(N)
#
# SPACE : O(N)
#
# ============================================================

def longest_substring_optimal(s):

    last_seen = {}

    left = 0

    longest = 0

    for right in range(len(s)):

        current = s[right]

        # Duplicate found
        # inside current window.

        if current in last_seen:
            # Never move the left pointer backwards.
            #
            # If the previous occurrence lies
            # outside the current window,
            # we should ignore it.
            #
            # Therefore,
            # move left only forward.

            left = max(

                left,

                last_seen[current] + 1

            )

        last_seen[current] = right

        longest = max(

            longest,

            right - left + 1

        )

    return longest


# ============================================================
# DRY RUN
# ============================================================
#
# s =
#
# "abcabcbb"
#
#
# left = 0
#
#
# right -> a
#
# Window:
#
# a
#
# Length = 1
#
#
# right -> b
#
# Window:
#
# ab
#
# Length = 2
#
#
# right -> c
#
# Window:
#
# abc
#
# Length = 3
#
#
# right -> a
#
# Duplicate.
#
#
# Jump:
#
# left = 1
#
#
# Window:
#
# bca
#
#
# Length = 3
#
#
# Continue...
#
#
# Final Answer:
#
# 3
#
# ============================================================
# DRIVER CODE
# ============================================================

s = "abcabcbb"

print("================================================")
print("INPUT STRING")
print("================================================")

print("String =", s)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Longest Length =",
    longest_substring_brute(s)
)

print()

print("================================================")
print("2. BETTER APPROACH (SLIDING WINDOW + HASH SET)")
print("================================================")

print(
    "Longest Length =",
    longest_substring_better(s)
)

print()

print("================================================")
print("3. OPTIMAL (SLIDING WINDOW + HASH MAP)")
print("================================================")

print(
    "Longest Length =",
    longest_substring_optimal(s)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

s2 = "bbbbb"

print("String =", s2)

print(
    "Longest Length =",
    longest_substring_optimal(s2)
)

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

s3 = "pwwkew"

print("String =", s3)

print(
    "Longest Length =",
    longest_substring_optimal(s3)
)

print()

print("================================================")
print("FOURTH TEST CASE")
print("================================================")

s4 = "abcdef"

print("String =", s4)

print(
    "Longest Length =",
    longest_substring_optimal(s4)
)

print()

print("================================================")
print("EMPTY STRING")
print("================================================")

s5 = ""

print("String =", s5)

print(
    "Longest Length =",
    longest_substring_optimal(s5)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force")
print("Time  : O(N³)")
print("Space : O(N)")

print()

print("Sliding Window + Hash Set")
print("Time  : O(2N)")
print("Space : O(N)")

print()

print("Sliding Window + Hash Map")
print("Time  : O(N)")
print("Space : O(N)")

print()

print("================================================")
print("INTERVIEW NOTES")
print("================================================")

print("Brute Force")
print("-> Generate every substring.")
print("-> Check whether all characters")
print("   are unique.")

print()

print("Better")
print("-> Expand the window.")
print("-> If duplicate appears,")
print("   shrink the window")
print("   one character at a time.")

print()

print("Optimal")
print("-> Store the last index")
print("   of every character.")
print("-> Jump the left pointer")
print("   directly instead of")
print("   removing characters")
print("   one by one.")

print()

print("================================================")
print("WHY max(left, last_seen + 1)?")
print("================================================")

print("Suppose:")

print()

print("String = abcbdeaf")

print()

print("When we see a duplicate,")

print("we must NEVER move")

print("the left pointer")

print("backwards.")

print()

print("Therefore:")

print()

print("left = max(")
print("    left,")
print("    last_seen[character] + 1")
print(")")

print()

print("This guarantees")

print("left only moves")

print("forward.")

print()

print("================================================")
print("SLIDING WINDOW PATTERN")
print("================================================")

print("Expand Window")
print("↓")

print("Window becomes Invalid?")
print("↓")

print("Shrink Window")
print("↓")

print("Window becomes Valid")
print("↓")

print("Update Answer")
print("↓")

print("Continue")

print()

print("================================================")
print("MEMORY TRICK")
print("================================================")

print("Brute Force")
print("↓")
print("Generate Every Substring")
print("↓")
print("Check Duplicates")
print("↓")
print("O(N³)")

print()

print("Better")
print("↓")
print("Sliding Window")
print("↓")
print("Hash Set")
print("↓")
print("Shrink One by One")
print("↓")
print("O(2N)")

print()

print("Optimal")
print("↓")
print("Sliding Window")
print("↓")
print("Hash Map")
print("↓")
print("Jump Left Pointer")
print("↓")
print("O(N)")

print()

print("================================================")
print("GOLDEN RULE")
print("================================================")

print("Grow the window")
print("while it is valid.")

print()

print("If it becomes invalid,")

print("shrink the window")

print("until it becomes")

print("valid again.")

print()

print("This is the foundation")

print("of almost every")

print("Sliding Window problem.")