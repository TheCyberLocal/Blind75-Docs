# Blind75: Palindromic Substrings

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s`, return the number of substrings within `s` that are palindromes.

A palindrome is a string that reads the same forward and backward.

**Example 1:**

- **Input**: `s = "abc"`
- **Output**: `3`
- **Explanation**: `"a"`, `"b"`, `"c"`.

**Example 2:**

- **Input**: `s = "aaa"`
- **Output**: `6`
- **Explanation**: `"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, `"aaa"`. Note that different substrings are counted as different palindromes even if the string contents are the same.

### Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

---

### Approach 1: Expand Around Center

- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)`
- **Description**: This approach counts all palindromic substrings by expanding around each possible center of the palindrome. Since a palindrome can have either an odd or even length, we check for both cases by considering each character (and the space between characters) as the center of a potential palindrome.
- **Algorithm**:

  1. Initialize a variable `count` to store the number of palindromic substrings.
  2. Iterate through each character in the string, treating it as the center of potential odd-length and even-length palindromes.
  3. For each center, expand outward while the characters on both sides match, and increment `count` for each valid palindrome found.
  4. Return `count` as the total number of palindromic substrings.

  ```pseudo
  function countSubstrings(s):
    count = 0

    for i from 0 to len(s) - 1:
        count += expandAroundCenter(s, i, i)      // Odd-length palindromes
        count += expandAroundCenter(s, i, i + 1)  // Even-length palindromes

    return count

  function expandAroundCenter(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count
  ```
