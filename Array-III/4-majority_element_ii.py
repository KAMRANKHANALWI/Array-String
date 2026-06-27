# ============================================================
# MAJORITY ELEMENT II
# (Extended Moore's Voting Algorithm)
# ============================================================
#
# Problem:
#
# Given an array,
# find all elements whose frequency
# is greater than n/3.
#
#
# Return all such elements.
#
#
# Example:
#
# arr = [3,2,3]
#
# Answer:
#
# [3]
#
#
# Example:
#
# arr = [1,1,1,3,3,2,2,2]
#
# Answer:
#
# [1,2]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Majority Element I:
#
# Frequency > n/2
#
# Maximum possible answers:
#
# 1
#
#
# Majority Element II:
#
# Frequency > n/3
#
# Maximum possible answers:
#
# 2
#
#
# Why?
#
# Suppose:
#
# n = 9
#
# Three elements each appear
# more than 3 times.
#
# Total would exceed 9.
#
# Impossible.
#
#
# Therefore:
#
# At most TWO majority elements
# can exist.
#
#
# This leads to:
#
# Two Candidates
#
# Two Counters
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# For every unique element,
# count its frequency.
#
# If frequency > n/3,
#
# add it to answer.
#
#
# TIME  : O(N²)
# SPACE : O(1)
#
# ============================================================

def majority_element_brute(arr):

    n = len(arr)

    answer = []

    for i in range(n):

        if arr[i] in answer:

            continue

        count = 0

        for j in range(n):

            if arr[j] == arr[i]:

                count += 1

        if count > n // 3:

            answer.append(arr[i])

    return answer


# ============================================================
# 2. BETTER APPROACH (HASH MAP)
# ============================================================
#
# IDEA:
#
# Store frequencies of
# every element.
#
# Traverse the map.
#
# Add elements whose
# frequency > n/3.
#
#
# TIME  : O(N)
# SPACE : O(N)
#
# ============================================================

def majority_element_better(arr):

    frequency = {}

    for num in arr:

        frequency[num] = (
            frequency.get(num, 0) + 1
        )

    answer = []

    limit = len(arr) // 3

    for key in frequency:

        if frequency[key] > limit:

            answer.append(key)

    return answer


# ============================================================
# 3. OPTIMAL
# (EXTENDED MOORE'S VOTING)
# ============================================================
#
# Since there can be
# at most TWO majority elements,
#
# maintain:
#
# candidate1
# count1
#
# candidate2
# count2
#
#
# RULES:
#
# Same as candidate1
#
# -> count1++
#
#
# Same as candidate2
#
# -> count2++
#
#
# count1 == 0
#
# -> new candidate1
#
#
# count2 == 0
#
# -> new candidate2
#
#
# Different from both
#
# -> count1--
# -> count2--
#
#
# Finally,
#
# verify both candidates
# because they are only
# POSSIBLE majority elements.
#
#
# TIME  : O(N)
# SPACE : O(1)
#
# ============================================================

def majority_element_optimal(arr):

    candidate1 = None
    candidate2 = None

    count1 = 0
    count2 = 0

    # ========================================================
    # PASS 1
    #
    # Find possible candidates
    # ========================================================

    for num in arr:

        if candidate1 == num:

            count1 += 1

        elif candidate2 == num:

            count2 += 1

        elif count1 == 0:

            candidate1 = num
            count1 = 1

        elif count2 == 0:

            candidate2 = num
            count2 = 1

        else:

            count1 -= 1
            count2 -= 1

    # ========================================================
    # PASS 2
    #
    # Verify candidates
    # ========================================================

    count1 = 0
    count2 = 0

    for num in arr:

        if num == candidate1:

            count1 += 1

        elif num == candidate2:

            count2 += 1

    answer = []

    limit = len(arr) // 3

    if count1 > limit:

        answer.append(candidate1)

    if count2 > limit:

        answer.append(candidate2)

    return answer


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [1,1,1,3,3,2,2,2]
#
#
# candidate1 = None
# count1 = 0
#
# candidate2 = None
# count2 = 0
#
#
# 1
#
# candidate1 = 1
#
# count1 = 1
#
#
# 1
#
# count1 = 2
#
#
# 1
#
# count1 = 3
#
#
# 3
#
# candidate2 = 3
#
# count2 = 1
#
#
# 3
#
# count2 = 2
#
#
# 2
#
# Different from both
#
# count1--
#
# count2--
#
#
# count1 = 2
#
# count2 = 1
#
#
# 2
#
# Again different
#
# count1 = 1
#
# count2 = 0
#
#
# 2
#
# count2 == 0
#
# candidate2 = 2
#
# count2 = 1
#
#
# Candidates:
#
# 1
#
# 2
#
#
# Verification:
#
# 1 -> 3 times
#
# 2 -> 3 times
#
#
# Both >
#
# n/3
#
#
# Answer:
#
# [1,2]
#
# ============================================================


# ============================================================
# DRIVER CODE
# ============================================================

arr = [1, 1, 1, 3, 3, 2, 2, 2]

print("================================================")
print("INPUT ARRAY")
print("================================================")

print(arr)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Majority Elements =",
    majority_element_brute(arr)
)

print()

print("================================================")
print("2. BETTER APPROACH (HASH MAP)")
print("================================================")

print(
    "Majority Elements =",
    majority_element_better(arr)
)

print()

print("================================================")
print("3. OPTIMAL (EXTENDED MOORE'S VOTING)")
print("================================================")

print(
    "Majority Elements =",
    majority_element_optimal(arr)
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [3, 2, 3]

print("Array =", arr2)

print(
    "Majority Elements =",
    majority_element_optimal(arr2)
)

print()

print("================================================")
print("NO MAJORITY ELEMENT")
print("================================================")

arr3 = [1, 2, 3, 4]

print("Array =", arr3)

print(
    "Majority Elements =",
    majority_element_optimal(arr3)
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force -> O(N²), O(1)")
print("Hash Map    -> O(N),  O(N)")
print("Moore Vote  -> O(N),  O(1)")