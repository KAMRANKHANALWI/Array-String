# DSA — Arrays & Strings

Structured Python solutions for Array and String interview problems, following Striver's A2Z Sheet. Each file includes approach and complexity analysis.

---

## Array-I

| #   | Problem                         | Key Idea                             |
| --- | ------------------------------- | ------------------------------------ |
| 1   | Set Matrix Zeroes               | Use first row/column as markers      |
| 2   | Pascal's Triangle               | Combinatorics / row-by-row build     |
| 3   | Next Permutation                | Find pivot, swap, reverse suffix     |
| 4   | Kadane's Algorithm              | Running sum, reset when negative     |
| 5   | Sort 0s, 1s, 2s                 | Dutch National Flag (three pointers) |
| 6   | Best Time to Buy and Sell Stock | Track minimum price seen so far      |

## Array-II

| #   | Problem                                 | Key Idea                           |
| --- | --------------------------------------- | ---------------------------------- |
| 1   | Rotate Matrix by 90 Degrees             | Transpose + reverse rows           |
| 2   | Merge Overlapping Intervals             | Sort by start, merge on overlap    |
| 3   | Merge Sorted Arrays Without Extra Space | Gap method / two-pointer swap      |
| 4   | Find the Duplicate Number               | Floyd's Cycle Detection on indices |
| 5   | Find Missing and Repeating Number       | Math / XOR technique               |
| 6   | Count Inversions in Array               | Merge Sort                         |

## Array-III

| #   | Problem                           | Key Idea                                       |
| --- | --------------------------------- | ---------------------------------------------- |
| 1   | Search in a 2D Matrix             | Treat as flattened sorted array, Binary Search |
| 2   | Pow(x, n) — Binary Exponentiation | Divide exponent by 2 each step                 |
| 3   | Majority Element                  | Boyer-Moore Voting Algorithm                   |
| 4   | Majority Element II               | Extended Boyer-Moore (two candidates)          |
| 5   | Grid Unique Paths                 | Combinatorics / DP                             |
| 6   | Reverse Pairs                     | Merge Sort with count                          |

## Array-IV

| #   | Problem                                        | Key Idea                                    |
| --- | ---------------------------------------------- | ------------------------------------------- |
| 1   | Two Sum                                        | HashMap for complement lookup               |
| 2   | Three Sum                                      | Sort + Two Pointer                          |
| 3   | Four Sum                                       | Sort + Two Pointer (nested)                 |
| 4   | Longest Consecutive Sequence                   | HashSet, start counting from sequence heads |
| 5   | Longest Subarray with Sum K                    | Prefix Sum + HashMap                        |
| 6   | Number of Subarrays with XOR K                 | Prefix XOR + HashMap                        |
| 7   | Longest Substring Without Repeating Characters | Sliding Window + HashMap                    |

## String-I

| #   | Problem                        | Key Idea                                                |
| --- | ------------------------------ | ------------------------------------------------------- |
| 1   | Reverse Every Word in a String | Split, reverse order, rejoin                            |
| 2   | Longest Palindromic Substring  | Expand Around Center                                    |
| 3   | Roman to Integer               | Left-to-right scan, subtract if smaller precedes larger |
| 4   | String to Integer (atoi)       | Manual parsing with overflow checks                     |
| 5   | Longest Common Prefix          | Vertical scanning across strings                        |
| 6   | Rabin-Karp Algorithm           | Rolling Hash for pattern matching                       |

## String-II

| #   | Problem                                      | Key Idea                                  |
| --- | -------------------------------------------- | ----------------------------------------- |
| 0   | Zigzag Conversion                            | Simulate row traversal direction          |
| 1   | Z Function                                   | Z-array for pattern matching              |
| 2   | KMP Algorithm                                | LPS (prefix) array to skip re-comparisons |
| 3   | Minimum Insertions to Make String Palindrome | LCS with reversed string                  |
| 4   | Valid Anagram                                | Frequency count comparison                |
| 5   | Count and Say                                | Iterative run-length encoding             |
| 6   | Compare Version Numbers                      | Split by '.', compare numeric segments    |

---

## Structure

Each file contains the problem statement, approach, and time/space complexity inline as comments.
