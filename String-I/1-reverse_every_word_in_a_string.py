# ============================================================
# REVERSE EVERY WORD IN A STRING
# ============================================================
#
# Problem:
#
# Given a string,
#
# reverse the order
# of the words.
#
#
# NOTE:
#
# Do NOT reverse
# individual characters.
#
#
# Reverse only
# the order
# of the words.
#
#
# Example:
#
# Input:
#
# "I love coding"
#
#
# Output:
#
# "coding love I"
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Think like a human.
#
#
# Step 1
#
# Separate the words.
#
#
# Example:
#
# "I love coding"
#
#
# becomes
#
# [
#   "I",
#   "love",
#   "coding"
# ]
#
#
# Step 2
#
# Reverse the order
# of the words.
#
#
# [
#   "coding",
#   "love",
#   "I"
# ]
#
#
# Step 3
#
# Join them back
# using one space.
#
#
# Result:
#
# "coding love I"
#
#
# This is exactly
# what Python's
#
# split()
#
# reverse()
#
# join()
#
# do.
#
# ============================================================


# ============================================================
# 1. PYTHONIC APPROACH
# ============================================================
#
# IDEA:
#
# Strip
#
# Split
#
# Reverse
#
# Join
#
#
# TIME  : O(N)
#
# SPACE : O(N)
#
# ============================================================

def reverse_words_pythonic(text):

    words = text.strip().split()

    words.reverse()

    return " ".join(words)


# ============================================================
# 2. MANUAL REVERSE
# (WITHOUT reverse())
# ============================================================
#
# IDEA:
#
# Extract all words.
#
#
# Reverse the list
# ourselves
# using
#
# Two Pointers.
#
#
# left ------>
#
# <------ right
#
#
# Swap
#
# until
#
# left >= right
#
#
# Finally,
#
# join the words.
#
#
# TIME  : O(N)
#
# SPACE : O(N)
#
# ============================================================

def reverse_words_manual(text):

    words = text.strip().split()

    left = 0

    right = len(words) - 1

    # Reverse the list
    # using Two Pointers.

    while left < right:

        words[left], words[right] = (

            words[right],

            words[left]

        )

        left += 1

        right -= 1

    return " ".join(words)


# ============================================================
# 3. INTERVIEW APPROACH
# ============================================================
#
# In C++ interviews,
#
# they may ask:
#
# "Can you do it
# without creating
# another array?"
#
#
# Idea:
#
# Reverse the
# entire string.
#
#
# Then
#
# reverse every
# individual word.
#
#
# Example:
#
# Original:
#
# I love coding
#
#
# Reverse Entire String:
#
# gnidoc evol I
#
#
# Reverse Every Word:
#
# coding love I
#
#
# This performs
# the reversal
# in-place.
#
#
# Python strings
# are immutable,
#
# therefore
#
# the previous
# two solutions
#
# are preferred.
#
# ============================================================


# ============================================================
# DRY RUN
# ============================================================
#
# text
#
# =
#
# "I love coding"
#
#
# split()
#
# ↓
#
# ["I","love","coding"]
#
#
# Reverse
#
# ↓
#
# ["coding","love","I"]
#
#
# Join
#
# ↓
#
# "coding love I"
#
#
# Answer:
#
# coding love I
#
# ============================================================
# DRIVER CODE
# ============================================================

text = "I love coding"

print("================================================")
print("INPUT STRING")
print("================================================")

print(text)

print()

print("================================================")
print("1. PYTHONIC APPROACH")
print("================================================")

print(

    reverse_words_pythonic(text)

)

print()

print("================================================")
print("2. MANUAL TWO POINTER APPROACH")
print("================================================")

print(

    reverse_words_manual(text)

)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

text2 = "the sky is blue"

print(text2)

print()

print(

    reverse_words_manual(text2)

)

print()

print("================================================")
print("MULTIPLE SPACES")
print("================================================")

text3 = "   hello     world    "

print("Original :")

print(repr(text3))

print()

print("Output :")

print(

    reverse_words_manual(text3)

)

print()

print("================================================")
print("SINGLE WORD")
print("================================================")

text4 = "Python"

print(text4)

print()

print(

    reverse_words_manual(text4)

)

print()

print("================================================")
print("EMPTY STRING")
print("================================================")

text5 = ""

print(repr(text5))

print()

print(

    reverse_words_manual(text5)

)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Pythonic Approach")
print("Time  : O(N)")
print("Space : O(N)")

print()

print("Manual Two Pointer")
print("Time  : O(N)")
print("Space : O(N)")

print()

print("Interview Approach")
print("Time  : O(N)")
print("Space : O(1)  (For mutable strings like C++)")

print()

print("================================================")
print("INTERVIEW NOTES")
print("================================================")

print("Step 1")
print("↓")
print("Extract all words.")

print()

print("Step 2")
print("↓")
print("Reverse the order")
print("of the words.")

print()

print("Step 3")
print("↓")
print("Join them back")
print("using a single space.")

print()

print("================================================")
print("WHY strip() ?")
print("================================================")

print("Removes leading")
print("and trailing spaces.")

print()

print("Example")

print()

print(repr("   hello world   "))

print()

print("becomes")

print()

print(repr("hello world"))

print()

print("================================================")
print("WHY split() ?")
print("================================================")

print("split() separates")
print("the sentence")
print("into individual words.")

print()

print("Example")

print()

print('"I love coding"')

print()

print("becomes")

print()

print(["I", "love", "coding"])

print()

print("================================================")
print("WHY join() ?")
print("================================================")

print("join() combines")
print("all the words")
print("back into")
print("one sentence.")

print()

print("Example")

print()

print(["coding", "love", "I"])

print()

print("becomes")

print()

print("coding love I")

print()

print("================================================")
print("TWO POINTER REVERSAL")
print("================================================")

print("Initially")

print()

print("[I, love, coding]")

print()

print("left = 0")
print("right = 2")

print()

print("Swap")

print()

print("[coding, love, I]")

print()

print("left = 1")
print("right = 1")

print()

print("Stop.")

print()

print("================================================")
print("MEMORY TRICK")
print("================================================")

print("Sentence")

print("↓")

print("Split")

print("↓")

print("Reverse")

print("↓")

print("Join")

print()

print("Think in terms")
print("of WORDS.")

print()

print("NOT")

print()

print("Characters.")

print()

print("================================================")
print("REAL INTERVIEW")
print("================================================")

print("Python")

print("↓")

print("split()")
print("reverse()")
print("join()")

print()

print("C++")

print("↓")

print("Reverse Entire String")
print("↓")
print("Reverse Every Word")
print("↓")
print("In-place Solution")

print()

print("================================================")
print("KEY TAKEAWAY")
print("================================================")

print("This problem")
print("introduces")
print("String Parsing.")

print()

print("Read Sentence")

print("↓")

print("Extract Words")

print("↓")

print("Process Words")

print("↓")

print("Build Answer")

print()

print("This same pattern")
print("appears again in:")

print()

print("• Roman to Integer")
print("• ATOI")
print("• Rabin-Karp")
print("• String Matching")