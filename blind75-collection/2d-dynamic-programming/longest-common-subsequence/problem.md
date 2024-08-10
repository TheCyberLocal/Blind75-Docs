# Blind75: Longest Common Subsequence

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given two strings `text1` and `text2`, return the length of the longest common subsequence between the two strings if one exists, otherwise return `0`.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

A common subsequence of two strings is a subsequence that exists in both strings.

**Example 1:**

-   **Input**: `text1 = "cat"`, `text2 = "crabt"`
-   **Output**: `3`
-   **Explanation**: The longest common subsequence is `"cat"` which has a length of 3.

**Example 2:**

-   **Input**: `text1 = "abcd"`, `text2 = "abcd"`
-   **Output**: `4`

**Example 3:**

-   **Input**: `text1 = "abcd"`, `text2 = "efgh"`
-   **Output**: `0`

### Constraints

-   `1 <= len(text1), len(text2) <= 1000`
-   `text1` and `text2` consist of only lowercase letters.

---

### Approach 1: Dynamic Programming

-   **Time Complexity**: `O(m * n)`
-   **Space Complexity**: `O(m * n)`
-   **Description**: This approach uses dynamic programming to find the length of the longest common subsequence. We create a 2D array `dp` where `dp[i][j]` represents the length of the longest common subsequence of `text1[0..i - 1]` and `text2[0..j - 1]`. If the characters `text1[i - 1]` and `text2[j - 1]` are the same, then `dp[i][j]` will be `dp[i - 1][j - 1] + 1`. Otherwise, it will be the maximum of `dp[i - 1][j]` and `dp[i][j - 1]`.
-   **Algorithm**:

    1. Initialize a 2D array `dp` of size `(m + 1) x (n + 1)` with all values set to `0`, where `m` and `n` are the lengths of `text1` and `text2`, respectively.
    2. Iterate through the strings `text1` and `text2` using two nested loops.
    3. For each pair of characters `text1[i - 1]` and `text2[j - 1]`, if they are equal, set `dp[i][j] = dp[i - 1][j - 1] + 1`. Otherwise, set `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`.
    4. The value at `dp[m][n]` will contain the length of the longest common subsequence.

```pseudo
function longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = 2D array of size (m + 1) x (n + 1) initialized to 0

    for i from 1 to m:
        for j from 1 to n:
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
```

### Approach 2: Dynamic Programming (Reversed Iteration)

-   **Time Complexity**: `O(m * n)`
-   **Space Complexity**: `O(m * n)`
-   **Description**: This approach is similar to the first dynamic programming method but iterates through the strings in reverse order. Instead of starting from the beginning of the strings and building up the solution, we start from the end of the strings and work backward. The idea is to fill out the `dp` table from the bottom right to the top left, where each `dp[i][j]` represents the length of the longest common subsequence between the suffixes `text1[i:]` and `text2[j:]`. The final answer will be stored in `dp[0][0]`, representing the longest common subsequence between the entire strings `text1` and `text2`.
-   **Algorithm**:

    1. Initialize a 2D array `dp` of size `(m + 1) x (n + 1)` with all values set to `0`, where `m` and `n` are the lengths of `text1` and `text2`, respectively.
    2. Iterate through the strings `text1` and `text2` in reverse order using two nested loops.
    3. For each pair of characters `text1[i]` and `text2[j]`, if they are equal, set `dp[i][j] = 1 + dp[i + 1][j + 1]`. Otherwise, set `dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])`.
    4. The value at `dp[0][0]` will contain the length of the longest common subsequence.

```pseudo
function longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = 2D array of size (m + 1) x (n + 1) initialized to 0

    for i from m - 1 to 0:
            for j from n - 1 to 0:
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
```
