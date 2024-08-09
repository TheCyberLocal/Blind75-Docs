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

- `1 <= len(s) <= 1000`
- `s` consists of lowercase letters.

---

### Approach 1: Expand Around Center

- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(1)`
- **Description**:
- **Algorithm**:

  ```pseudo
  function countSubstrings(s):
    function countPali(l, r):
      count = 0
      while l >= 0 and r < len(s) and s[l] == s[r]:
          count += 1
          l, r = l - 1, r + 1
      return count

    res = 0
    for i from 0 to len(s) - 1:
        res += countPali(i, i)
        res += countPali(i, i + 1)

    return res
  ```
