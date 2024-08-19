# Blind75: Valid Palindrome

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Example 1:**

-   **Input:** `s = "Was it a car or a cat I saw?"`
-   **Output:** `true`
-   **Explanation:** After considering only alphanumerical characters, we have `"wasitacaroracatisaw"`, which is a palindrome.

**Example 2:**

-   **Input:** `s = "tab a cat"`
-   **Output:** `false`
-   **Explanation:** `"tabacat"` is not a palindrome.

### Constraints

-   `1 <= len(s) <= 1000`
-   `s` is made up of only printable ASCII characters.`

---

### Approach 1: Two Pointers

-   **Time Complexity:** `O(n)`, where `n` is the length of `s`.
-   **Space Complexity:** `O(1)`.
-   **Description:** The two-pointer technique is employed to check whether the given string is a palindrome. The string is traversed using two pointers: one starting from the beginning and the other from the end. The goal is to compare the characters at both ends while skipping any non-alphanumeric characters and ignoring case. If all character pairs match, the string is a palindrome.
-   **Algorithm:**

    1. Initialize `left` to `0` and `right` to `len(s) - 1`.
    2. While `left` is less than `right`:
        1. If `s[left]` is not alphanumeric, increment `left`.
        2. If `s[right]` is not alphanumeric, decrement `right`.
        3. Compare the lowercase characters at `left` and `right`:
            - If they are not equal, return `false`.
            - If they are equal, increment `left` and decrement `right`.
    3. If the loop finishes, return `true` (the string is a palindrome).

```pseudo
function isAlphanumeric(c):
    return (
        ('a' <= c <= 'z')
        or ('A' <= c <= 'Z')
        or ('0' <= c <= '9')
    )

function isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if not isAlphanumeric(s[left]):
            left += 1
            continue

        if not isAlphanumeric(s[right]):
            right -= 1
            continue

        if s[left].lowercase() != s[right].lowercase():
            return false

        left += 1
        right -= 1

    return true
```
