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

-   `s` and `t` consist only of lowercase letters.

---

### Approach 1: Sorted Comparison

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

### Approach 2: Count Frequency using Hash Maps

-   **Time Complexity**: `O(n)` where `n` is the length of the strings.
-   **Space Complexity**: `O(1)` since the hash maps require constant space for the 26 lowercase letters.
-   **Description**: This approach uses hash maps to count the frequency of each character in both strings. The hash maps `countS` and `countT` store the frequency of each character in `s` and `t`, respectively. After populating the hash maps, we compare the frequencies. If they match for all characters, the strings are anagrams; otherwise, they are not.
-   **Algorithm**:

    1. If the lengths of `s` and `t` are different, return `false`.
    2. Initialize two hash maps, `countS` and `countT`, to store the frequency of each character in `s` and `t`.
    3. Iterate through each character in `s` and `t`:
        - For each character in `s`, increment its count in `countS`.
        - For each character in `t`, increment its count in `countT`.
    4. Iterate through the keys in `countS`:
        - If the frequency of a character in `countS` does not match its frequency in `countT`, return `false`.
    5. If all character frequencies match, return `true`.

```pseudo
function validAnagram(s, t):
    if len(s) != len(t):
        return false

    countS, countT = {}, {}
    for i from 0 to len(s) - 1:
        countS[s[i]] = (countS[s[i]] if s[i] in countS else 0) + 1
        countT[t[i]] = (countT[t[i]] if t[i] in countT else 0) + 1

    for c in countS:
        if countS[c] != (countT[c] if t[i] in countT else 0):
            return false

    return countS == countT
```
