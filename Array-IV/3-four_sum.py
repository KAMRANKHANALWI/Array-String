# ============================================================
# FOUR SUM
# ============================================================
#
# Problem:
#
# Given an integer array
# and a target value,
#
# find all UNIQUE quadruplets
# whose sum equals the target.
#
#
# Example:
#
# arr = [1,0,-1,0,-2,2]
#
# target = 0
#
#
# Answer:
#
# [
#   [-2,-1,1,2],
#   [-2,0,0,2],
#   [-1,0,0,1]
# ]
#
# ============================================================


# ============================================================
# GOLDEN OBSERVATION
# ============================================================
#
# Four Sum is simply
#
# Three Sum
#
# +
#
# One Extra Loop.
#
#
# Think about the progression:
#
# Two Sum
#
# ↓
#
# Need two numbers.
#
#
# Three Sum
#
# ↓
#
# Fix ONE element.
#
# Remaining problem becomes
# Two Sum.
#
#
# Four Sum
#
# ↓
#
# Fix TWO elements.
#
# Remaining problem becomes
# Two Sum.
#
#
# Therefore,
#
# once we know Two Sum,
#
# Three Sum and Four Sum
# become natural extensions.
#
# ============================================================


# ============================================================
# 1. BRUTE FORCE
# ============================================================
#
# IDEA:
#
# Try every possible
# quadruplet.
#
#
# Four nested loops.
#
#
# If:
#
# arr[i] + arr[j] + arr[k] + arr[l]
#
# equals target,
#
# store the quadruplet.
#
#
# Since duplicates are possible,
#
# sort every quadruplet
# before storing.
#
#
# Use a set to remove duplicates.
#
#
# TIME  : O(N⁴)
#
# SPACE : O(Number of Quadruplets)
#
# ============================================================

def four_sum_brute(arr, target):

    n = len(arr)

    unique_quadruplets = set()

    for i in range(n):

        for j in range(i + 1, n):

            for k in range(j + 1, n):

                for l in range(k + 1, n):

                    if (

                        arr[i]

                        + arr[j]

                        + arr[k]

                        + arr[l]

                        == target

                    ):

                        quadruplet = sorted(

                            [

                                arr[i],
                                arr[j],
                                arr[k],
                                arr[l]

                            ]

                        )

                        unique_quadruplets.add(

                            tuple(quadruplet)

                        )

    return [

        list(quadruplet)

        for quadruplet in unique_quadruplets

    ]


# ============================================================
# 2. BETTER APPROACH (HASH SET)
# ============================================================
#
# IDEA:
#
# Fix:
#
# i
#
# j
#
#
# Remaining problem
# becomes:
#
# Two Sum.
#
#
# Maintain a Hash Set.
#
#
# third =
#
# target
#
# -
#
# (arr[i] + arr[j] + arr[k])
#
#
# If third already exists,
#
# we found one quadruplet.
#
#
# Again,
#
# use a set
# to avoid duplicates.
#
#
# TIME  : O(N³)
#
# SPACE : O(N)
#
# ============================================================

def four_sum_better(arr, target):

    n = len(arr)

    unique_quadruplets = set()

    for i in range(n):

        for j in range(i + 1, n):

            seen = set()

            for k in range(j + 1, n):

                fourth = (

                    target

                    - (

                        arr[i]

                        + arr[j]

                        + arr[k]

                    )

                )

                if fourth in seen:

                    quadruplet = sorted(

                        [

                            arr[i],
                            arr[j],
                            arr[k],
                            fourth

                        ]

                    )

                    unique_quadruplets.add(

                        tuple(quadruplet)

                    )

                seen.add(

                    arr[k]

                )

    return [

        list(quadruplet)

        for quadruplet in unique_quadruplets

    ]


# ============================================================
# 3. OPTIMAL
# (SORT + TWO POINTERS)
# ============================================================
#
# IDEA:
#
# Step 1:
#
# Sort the array.
#
#
# Step 2:
#
# Fix first element.
#
#
# Step 3:
#
# Fix second element.
#
#
# Remaining problem
# becomes Two Sum.
#
#
# Maintain:
#
# left
#
# right
#
#
# If:
#
# current_sum < target
#
# move left++
#
#
# If:
#
# current_sum > target
#
# move right--
#
#
# Else:
#
# Store answer.
#
#
# IMPORTANT:
#
# Skip duplicate values
# for:
#
# i
#
# j
#
# left
#
# right
#
#
# TIME  : O(N³)
#
# SPACE : O(1)
#
# ============================================================

def four_sum_optimal(arr, target):

    arr.sort()

    answer = []

    n = len(arr)

    # We need at least
    # three more elements
    # after i.

    for i in range(n - 3):

        # Skip duplicate first element.
        #
        # Otherwise,
        # the same quadruplet
        # would be generated
        # multiple times.

        if i > 0 and arr[i] == arr[i - 1]:

            continue

        # We need at least
        # two more elements
        # after j.

        for j in range(i + 1, n - 2):

            # Skip duplicate second element.
            #
            # This prevents duplicate
            # quadruplets with the
            # same second element.

            if (

                j > i + 1

                and

                arr[j] == arr[j - 1]

            ):

                continue

            left = j + 1

            right = n - 1

            while left < right:

                current_sum = (

                    arr[i]

                    + arr[j]

                    + arr[left]

                    + arr[right]

                )

                if current_sum < target:

                    left += 1

                elif current_sum > target:

                    right -= 1

                else:

                    answer.append(

                        [

                            arr[i],
                            arr[j],
                            arr[left],
                            arr[right]

                        ]

                    )

                    left += 1
                    right -= 1

                    # Move past duplicate values.
                    #
                    # We have already used
                    # this value in the
                    # current quadruplet.
                    #
                    # Using it again would
                    # generate the same
                    # answer.

                    while (

                        left < right

                        and

                        arr[left] == arr[left - 1]

                    ):

                        left += 1

                    # Move past duplicate values.
                    #
                    # This prevents generating
                    # the same quadruplet
                    # from the right side.

                    while (

                        left < right

                        and

                        arr[right] == arr[right + 1]

                    ):

                        right -= 1

    return answer


# ============================================================
# DRY RUN
# ============================================================
#
# arr =
#
# [1,0,-1,0,-2,2]
#
#
# Sort:
#
# [-2,-1,0,0,1,2]
#
#
# Fix:
#
# i = -2
#
#
# Fix:
#
# j = -1
#
#
# Need:
#
# remaining sum = 3
#
#
# left = 0
#
# right = 2
#
#
# Current Sum:
#
# -2 + -1 + 0 + 2
#
# = -1
#
#
# Too Small.
#
# Move left.
#
#
# Current Sum:
#
# -2 + -1 + 1 + 2
#
# = 0
#
#
# Found:
#
# [-2,-1,1,2]
#
#
# Continue.
#
#
# Skip duplicate values.
#
#
# Final Answer:
#
# [
#   [-2,-1,1,2],
#   [-2,0,0,2],
#   [-1,0,0,1]
# ]
#
# ============================================================
# DRIVER CODE
# ============================================================

arr = [1, 0, -1, 0, -2, 2]

target = 0

print("================================================")
print("INPUT ARRAY")
print("================================================")

print("Array  =", arr)
print("Target =", target)

print()

print("================================================")
print("1. BRUTE FORCE")
print("================================================")

print(
    "Quadruplets =",
    four_sum_brute(
        arr,
        target
    )
)

print()

print("================================================")
print("2. BETTER APPROACH (HASH SET)")
print("================================================")

print(
    "Quadruplets =",
    four_sum_better(
        arr,
        target
    )
)

print()

print("================================================")
print("3. OPTIMAL (SORT + TWO POINTERS)")
print("================================================")

print(
    "Quadruplets =",
    four_sum_optimal(
        arr,
        target
    )
)

print()

print("================================================")
print("SECOND TEST CASE")
print("================================================")

arr2 = [2, 2, 2, 2, 2]

target2 = 8

print("Array  =", arr2)
print("Target =", target2)

print()

print(
    "Quadruplets =",
    four_sum_optimal(
        arr2,
        target2
    )
)

print()

print("================================================")
print("THIRD TEST CASE")
print("================================================")

arr3 = [-3, -1, 0, 2, 4, 5]

target3 = 2

print("Array  =", arr3)
print("Target =", target3)

print()

print(
    "Quadruplets =",
    four_sum_optimal(
        arr3,
        target3
    )
)

print()

print("================================================")
print("NO VALID QUADRUPLETS")
print("================================================")

arr4 = [1, 2, 3, 4]

target4 = 100

print("Array  =", arr4)
print("Target =", target4)

print()

print(
    "Quadruplets =",
    four_sum_optimal(
        arr4,
        target4
    )
)

print()

print("================================================")
print("COMPLEXITY SUMMARY")
print("================================================")

print("Brute Force")
print("Time  : O(N⁴)")
print("Space : O(Number of Quadruplets)")

print()

print("Hash Set")
print("Time  : O(N³)")
print("Space : O(N)")

print()

print("Sort + Two Pointers")
print("Time  : O(N³)")
print("Space : O(1)")

print()

print("================================================")
print("INTERVIEW NOTES")
print("================================================")

print("Brute Force")
print("-> Try every possible quadruplet.")

print()

print("Better")
print("-> Fix two elements.")
print("-> Remaining problem becomes Two Sum using a Hash Set.")

print()

print("Optimal")
print("-> Sort the array.")
print("-> Fix the first element.")
print("-> Fix the second element.")
print("-> Solve the remaining part using Two Pointers.")
print("-> Skip duplicate values for i, j, left and right.")

print()

print("================================================")
print("K-SUM PATTERN")
print("================================================")

print("Two Sum")
print("-> Solve directly using Hash Map or Two Pointers.")

print()

print("Three Sum")
print("-> Fix ONE element.")
print("-> Remaining problem becomes Two Sum.")

print()

print("Four Sum")
print("-> Fix TWO elements.")
print("-> Remaining problem becomes Two Sum.")

print()

print("General Rule")

print()

print("K Sum")
print("-> Fix (K - 2) elements.")
print("-> Remaining problem becomes Two Sum.")

print()

print("================================================")
print("MEMORY TRICK")
print("================================================")

print("4 Sum")
print("↓")

print("Fix First Element")
print("↓")

print("Fix Second Element")
print("↓")

print("Two Pointer")
print("↓")

print("Skip Duplicates")
print("↓")

print("Repeat")

print()

print("Every K-Sum problem")
print("eventually reduces")
print("to Two Sum.")