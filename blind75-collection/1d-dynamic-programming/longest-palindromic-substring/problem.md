# Blind75: Longest Palindromic Substring

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s`, return the longest substring of `s` that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

**Example 1:**

- **Input**: `s = "ababd"`
- **Output**: `"bab"`
- **Explanation**: Both `"aba"` and `"bab"` are valid answers.

**Example 2:**

- **Input**: `s = "abbc"`
- **Output**: `"bb"`

### Constraints

- `1 <= len(s) <= 1000`
- `s` is alphanumeric.

---

### Approach 1: Expand Around Center and Store Result

- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)`
- **Description**: This approach identifies the longest palindrome by treating each character (and each pair of consecutive characters) as the potential center of a palindrome. It directly updates a result string with the current longest palindrome as it iterates through the centers.
- **Algorithm**:

  1. Initialize two variables `result` and `resLen` to track the longest palindromic substring and its length.
  2. Define a helper function `countPali(l, r)` that expands around the center indices `l` and `r` while the characters on both sides are equal.
  3. For each center index `i` in the string `s`, call `countPali` twice: once for odd-length palindromes (centered at `i`) and once for even-length palindromes (centered between `i` and `i+1`).
  4. Update `res` and `resLen` if a longer palindrome is found during the expansion.
  5. Return the longest palindromic substring stored in `res`.

  ```pseudo
  function LongestPalindrome(s):
    res = ""
    resLen = 0

    function countPali(l, r):
      while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r - l + 1) > resLen:
          res = s[l : r + 1]
          resLen = r - l + 1
        l, r = l - 1, r + 1

    for i from 0 to (len(s) - 1):
      # odd length
      countPali(i, i)

      # even length
      countPali(i, i + 1)

    return res
  ```

---

### Approach 2: Expand Around Center and Track Indices

- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)`
- **Description**: This approach identifies the longest palindrome by treating each character (and each pair of consecutive characters) as the potential center of a palindrome. It tracks the longest palindrome indicies as it iterates through the centers.
- **Algorithm**:

  1. Initialize two variables `start` and `end` to track the beginning and ending indices of the longest palindrome found.
  2. Iterate over the string `s`, considering each character as the center of the palindrome.
  3. For each center, expand around it while the characters on both sides are equal.
  4. Update the `start` and `end` indices if a longer palindrome is found.
  5. Return the substring of `s` from `start` to `end + 1`.

  ```pseudo
  function longestPalindrome(s):
    function countPali(left, right):
      while left >= 0 and right < len(s) and s[left] == s[right]:
          left -= 1
          right += 1
      return right - left - 1

    start, end = 0, 0
    for i from 0 to len(s):
        len1 = countPali(i, i)
        len2 = countPali(i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start = floor(i - (length - 1) / 2)
            end = floor(i + length / 2)
    return s[start:end + 1]
  ```

---

### Approach 3: Dynamic Programming

- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`
- **Description**: This approach uses dynamic programming to check whether a substring is a palindrome. The idea is to use a 2D table `dp` where `dp[i][j]` is `True` if the substring `s[i:j+1]` is a palindrome. The result is then the longest palindromic substring found in the table.
- **Algorithm**:

  1. Initialize a 2D array `dp` of size `n x n` where `n` is the length of the string `s`.
  2. Set `dp[i][i]` to `True` since every single character is a palindrome.
  3. Check for two consecutive characters and update `dp[i][i+1]` if they are the same.
  4. Iterate over substrings of length greater than 2, updating `dp[i][j]` if `dp[i+1][j-1]` is `True` and `s[i] == s[j]`.
  5. Track the start and end indices of the longest palindrome found during the iterations.
  6. Return the substring of `s` from `start` to `end + 1`.

  ```pseudo
  function longestPalindrome(s):
    n = len(s)
    dp = 2D array of size n x n filled initialized to False
    start, end = 0, 0
    for i from 0 to n:
        dp[i][i] = True
    for length from 2 to n:
        for i from 0 to n - length + 1:
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > end - start + 1:
                        start = i
                        end = j
    return s[start:end + 1]
  ```
