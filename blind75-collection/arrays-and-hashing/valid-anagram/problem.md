# Blind75: Valid Anagram

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**

-   **Input**: `s = "racecar"`, `t = "carrace"`
-   **Output**: `true`

**Example 2:**

-   **Input**: `s = "jar"`, `t = "jam"`
-   **Output**: `false`

### Constraints

-   `s` and `t` consist of lowercase English letters.

---

### Approach 1: Sorting

-   **Time Complexity**: `O(n log n)` where `n` is the length of the strings.
-   **Space Complexity**: `O(1)` if sorting in place, otherwise `O(n)` for the sorted strings.
-   **Description**: Sort both strings and compare them. If the sorted versions of `s` and `t` are the same, return `true`. Otherwise, return `false`.
-   **Algorithm**:

    1. If the lengths of `s` and `t` are different, return `false`.
    2. Sort both strings.
    3. Compare the sorted strings:
        - If they are the same, return `true`.
        - Otherwise, return `false`.

```pseudo
function validAnagram(s, t):
    if len(s) != len(t):
        return false
    return sort(s) == sort(t)
```

---

### Approach 2: Frequency Count

-   **Time Complexity**: `O(n)` where `n` is the length of the strings.
-   **Space Complexity**: `O(1)` since the frequency count array size is constant.
-   **Description**: Use a frequency count array to compare the occurrences of each character in both strings. If the counts match for all characters, return `true`. Otherwise, return `false`.
-   **Algorithm**:

    1. If the lengths of `s` and `t` are different, return `false`.
    2. Initialize an array `count` of size `26` to `0`.
    3. Iterate through each character in `s` and `t`:
        - Increment the count for the character in `s`.
        - Decrement the count for the character in `t`.
    4. If all counts are `0`, return `true`.
    5. Otherwise, return `false`.

```pseudo
function validAnagram(s, t):
    if len(s) != len(t):
        return false
    count = [0] * 26
    for i from 0 to len(s) - 1:
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    return all(count[i] == 0 for i in range(26))
```
