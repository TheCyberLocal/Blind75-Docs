# Blind75: Decode Ways

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

A string consisting of uppercase letters can be encoded to a number using the following mapping:

-   `'A'` -> `"1"`
-   `'B'` -> `"2"`
-   ...
-   `'Z'` -> `"26"`

To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, `"1012"` can be mapped into:

-   `"JAB"` with the grouping `(10 1 2)`
-   `"JL"` with the grouping `(10 12)`

The grouping `(1 01 2)` is invalid because `01` cannot be mapped into a letter since it contains a leading zero.

Given a string `s` containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

**Example 1:**

-   **Input**: `s = "12"`
-   **Output**: `2`
-   **Explanation**: "12" could be decoded as "AB" (1 2) or "L" (12).

**Example 2:**

-   **Input**: `s = "01"`
-   **Output**: `0`
-   **Explanation**: "01" cannot be decoded because "01" cannot be mapped into a letter.

### Constraints

-   `1 <= len(s) <= 100`
-   `s` consists of digits.

---

### Approach 1: Simple Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(n)`
-   **Description**: This approach uses dynamic programming to keep track of the number of ways to decode the string up to each character. The key observation is that a valid decoding can be formed by considering either the last single digit or the last two digits as a letter if they form a valid character mapping.
-   **Algorithm**:

    1. Define `n` as `len(s)`.
    2. Initialize a `dp` array of size `n + 1`, where `dp[i]` represents the number of ways to decode the substring `s[0:i]`.
    3. Set `dp[0] = 1` (empty string has one way to decode) and `dp[1] = 1` if `s[0]` is not '0'.
    4. For each index `i` from 2 to `n`, update `dp[i]`:
        - If `s[i-1]` is a valid single digit, add `dp[i-1]` to `dp[i]`.
        - If `s[i-2:i]` is a valid two-digit number, add `dp[i-2]` to `dp[i]`.
    5. Return `dp[n]`.

```pseudo
function numDecodings(s):
    n = len(s)
    if s[0] == '0':
        return 0
    dp = array of size n + 1 initialized to 0
    dp[0] = dp[1] = 1
    for i from 2 to n:
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[n]
```

---

### Approach 2: Optimized Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(1)`
-   **Description**: This is an optimized version of the dynamic programming approach where only two variables are used to store the last two states instead of using a full array.
-   **Algorithm**:

    1. Initialize two variables, `p1` (for `dp[i-1]`) and `p2` (for `dp[i-2]`), both starting as 1.
    2. Iterate through the string from the second character to the end:
        - Calculate the current state based on the last single digit and the last two digits.
        - Update `p2` and `p1` accordingly.
    3. Return `p1` after the loop.

```pseudo
function numDecodings(s):
    n = len(s)
    if s[0] == '0':
        return 0
    p1 = p2 = 1
    for i from 1 to (n - 1):
        current = 0
        if s[i] != '0':
            current = p1
        if 10 <= int(s[i-1:i+1]) <= 26:
            current += p2
        p2 = p1
        p1 = current
    return p1
```

---

### Approach 3: Recursive Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(n)` (due to recursion stack and memoization)
-   **Description**: This approach uses recursion with memoization to calculate the number of ways to decode the string. The idea is to explore each possible decoding by trying to decode either one or two digits at a time and using memoization to store results of subproblems to avoid redundant calculations. This recursive method ensures that each subproblem is solved only once.
-   **Algorithm**:

    1. Initialize a dictionary `dp` to store the number of ways to decode the string starting from each index `i`. Set `dp[len(s)] = 1` as the base case (an empty string has one way to be decoded).
    2. Define a helper function `dfs(i)` that returns the number of ways to decode the substring starting at index `i`.
    3. In the `dfs` function:
        - If `i` is already in `dp`, return `dp[i]` (memoized result).
        - If the character at `s[i]` is `'0'`, return `0` because no valid letter can be mapped from `'0'`.
        - Recursively call `dfs(i + 1)` to consider the possibility of decoding the single digit at `s[i]`.
        - If the next two digits form a valid number between `10` and `26`, also recursively call `dfs(i + 2)` to consider this as a valid two-digit decoding.
        - Sum the results of the two recursive calls and store the result in `dp[i]`.
    4. Return the result of `dfs(0)`, which represents the number of ways to decode the entire string `s`.

```pseudo
function numDecodings(s):
    dp = dictionary a default value 1 at index len(s)

    function dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == '0':
            return 0

        res = dfs(i + 1)
        if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
            res += dfs(i + 2)

        dp[i] = res
        return res

    return dfs(0)
```
