# Blind75: Valid Anagram

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `False`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**

-   **Input**: `s = "racecar"`, `t = "carrace"`
-   **Output**: `true`

**Example 2:**

-   **Input**: `s = "jar"`, `t = "jam"`
-   **Output**: `False`

### Constraints

-   `s` and `t` consist only of lowercase letters.

---

### Approach 1: Sorted Comparison

-   **Time Complexity**: `O(n log n)` where `n` is the length of the strings.
-   **Space Complexity**: `O(1)` if sorting in place, otherwise `O(n)` for the sorted strings.
-   **Description**: Sort both strings and compare them. If the sorted versions of `s` and `t` are the same, return `true`. Otherwise, return `False`.
-   **Algorithm**:

    1. If the lengths of `s` and `t` are different, return `False`.
    2. Create `list_s` and `list_t`.
    3. Compare the sorted string lists:
        - If they are the same, return `true`.
        - Otherwise, return `False`.

```python
def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    list_s = list(s)
    list_t = list(t)

    return sorted(list_s) == sorted(list_t)
```

---

### Approach 2: Count Frequency using Hash Maps

-   **Time Complexity**: `O(n)` where `n` is the length of the strings.
-   **Space Complexity**: `O(1)` since the hash maps require constant space for the 26 lowercase letters.
-   **Description**: This approach uses hash maps to count the frequency of each character in both strings. The hash maps `count_s` and `count_t` store the frequency of each character in `s` and `t`, respectively. After populating the hash maps, we compare the frequencies. If they match for all characters, the strings are anagrams; otherwise, they are not.
-   **Algorithm**:

    1. If the lengths of `s` and `t` are different, return `False`.
    2. Initialize two hash maps, `count_s` and `count_t`, to store the frequency of each character in `s` and `t`.
    3. Iterate through each character in `s` and `t`:
        - For each character in `s`, increment its count in `count_s`.
        - For each character in `t`, increment its count in `count_t`.
    4. Iterate through the keys in `count_s`:
        - If the frequency of a character in `count_s` does not match its frequency in `count_t`, return `False`.
    5. If all character frequencies match, return `true`.

```python
def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s, count_t = defaultdict(int), defaultdict(int)

    for i in range(len(s)):
        count_s[s[i]] += 1
        count_t[t[i]] += 1

    for c in count_s:
        if count_s[c] != count_t[c]:
            return False

    return count_s == count_t
```

---

### Pro Solution

While this does work, it likely won't be accepted in an interview. 😅 But feel free to use it elsewhere and to impress others. 😎

It is essentially the equivalent of Approach 2, but it utilizes Python's built-in `collections.Counter` class to remove the boilerplate code.

```python
def valid_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```
