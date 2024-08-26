# Blind75: Group Anagrams

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**

-   **Input**: `strs = ["act","pots","tops","cat","stop","hat"]`
-   **Output**: `[["hat"],["act", "cat"],["stop", "pots", "tops"]]`

**Example 2:**

-   **Input**: `strs = ["x"]`
-   **Output**: `[["x"]]`

**Example 3:**

-   **Input**: `strs = [""]`
-   **Output**: `[[""]]`

### Constraints

-   `1 <= len(strs) <= 1000`
-   `0 <= len(strs[i]) <= 100`
-   `strs[i]` is made up of lowercase letters.

---

### Approach 1: Categorize by Sorted String

-   **Time Complexity**: `O(n * k log k)` where `n` is the number of strings and `k` is the average string length.
-   **Space Complexity**: `O(n * k)` for storing the grouped anagrams.
-   **Description**: We sort each string in the list, and use the sorted string as a key in a hash map to group anagrams together. Strings that are anagrams of each other will have the same sorted string and thus be placed in the same group.
-   **Algorithm**:

    1. Initialize an empty hash map `anagram_map` to store groups of anagrams.
    2. Iterate over each string `s` in `strs`:
        - Sort the characters of `s` to create a key.
        - If the key is not in `anagram_map`, add it with an empty list.
        - Append `s` to the list corresponding to the sorted key in `anagram_map`.
    3. Return the values of `anagram_map` as the grouped anagrams.

```python
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)

    for s in strs:
        key = sorted(s)
        anagram_map[tuple(key)].append(s)

    return list(anagram_map.values())
```

---

### Approach 2: Categorize by Character Count

-   **Time Complexity**: `O(n * k)` where `n` is the number of strings and `k` is the average string length.
-   **Space Complexity**: `O(n * k)` for storing the grouped anagrams.
-   **Description**: Instead of sorting the string, we can use the character count as a key. Each string can be represented by the count of each character, and this count array can serve as the key to group anagrams together.
-   **Algorithm**:

    1. Initialize an empty hash map `anagram_map` to store groups of anagrams.
    2. Iterate over each string `s` in `strs`:
        - Create a character count array `count` of size 26 (for each letter).
        - For each character in `s`, increment its corresponding position in the `count` array.
        - Convert the `count` array into a tuple and use it as a key in `anagram_map`.
        - Append `s` to the list corresponding to the tuple key in `anagram_map`.
    3. Return the values of `anagram_map` as the grouped anagrams.

```python
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)
        anagram_map[key].append(s)

    return list(anagram_map.values())
```
