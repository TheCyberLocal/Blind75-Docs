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
-   `s` consists only of digits.

---

### Approach 1: Simple Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(n)`
-   **Description**: This approach leverages dynamic programming to track the number of ways the string can be decoded up to each character. The fundamental idea is that each character in the string can potentially be decoded as a single digit or, when combined with the previous character, as a two-digit number, provided they form valid mappings to letters. By maintaining an array where each element represents the number of decoding ways up to that index, we can systematically explore all valid decoding possibilities. The solution involves examining each character, considering it individually and as part of a pair, and updating the array based on these possibilities.
-   **Algorithm**:

    1. **Define the Problem Size**: Determine the length of the string `s` and store it in `n`.

    2. **Initialize the Array**: Create an array `dp` of size `n + 1`, where each element will store the number of ways to decode the substring up to that point. Set the first element `dp[0]` to `1`, representing the single valid way to decode an empty string. For the first character, set `dp[1]` to `1` if it is a valid digit (i.e., not '0') since a single character can be decoded on its own.

    3. **Iterate Through the String**: Starting from the second character (index 2), iterate through each character in the string. For each character:

        - **Check Single Digit Validity**: If the current character can be decoded as a single digit (i.e., it is not '0'), add the number of ways to decode the string up to the previous character (`dp[i - 1]`) to the current value `dp[i]`.

        - **Check Two-Digit Validity**: If the combination of the current character and the previous character forms a valid two-digit number (between 10 and 26 inclusive), add the number of ways to decode the string up to two characters before (`dp[i - 2]`) to the current value `dp[i]`.

    4. **Return the Result**: After processing all characters, the last element of the `dp` array (`dp[n]`) contains the total number of ways to decode the entire string. Return this value as the result. If the string starts with '0', return `0` immediately as it is not decodable.

```pseudo
function numDecodings(s):
    n = len(s)
    if s[0] == '0':
        return 0
    dp = array of size n + 1 initialized to 0
    dp[0] = dp[1] = 1
    for i from 2 to n:
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[n]
```

---

### Approach 2: Optimized Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(1)`
-   **Description**: This is an optimized version of the dynamic programming approach where only two variables are used to store the last two states instead of using a full array.
-   **Algorithm**:

    1. Initialize two variables, `p1` (for `dp[i - 1]`) and `p2` (for `dp[i - 2]`), both starting as 1.
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
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            current += p2
        p2 = p1
        p1 = current
    return p1
```
