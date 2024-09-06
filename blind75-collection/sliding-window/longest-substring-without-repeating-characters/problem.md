# Blind75: Longest Substring Without Repeating Characters

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s`, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

**Example 1:**

-   **Input:** `s = "zxyzxyz"`
-   **Output:** `3`
    Explanation: The string `"xyz"` is the longest without duplicate characters.

**Example 2:**

-   **Input:** `s = "xxxx"`
-   **Output:** `1`

### Constraints

-   `0 <= len(s) <= 1000`
-   `s` may consist of printable ASCII characters.

---

### Approach 1: Sliding Window with Hash Map

-   **Time Complexity:** `O(n)`, where `n` is the length of the string.
-   **Space Complexity:** `O(min(n, m))`, where `m` is the size of the character set, because we use a hash map to store the last indices of the characters.
-   **Description:** The sliding window approach uses two pointers (`left` and `right`) to represent the current substring. A hash map is used to store the last occurrence of each character. As the `right` pointer expands the window, if a duplicate character is found, the `left` pointer is moved to ensure the substring remains free of duplicates. The maximum length of the substring is updated throughout the process.
-   **Algorithm:**

    1. Initialize a hash map `last_indicies` to store the last seen index of each character and set `left` to 0 and `max_length` to 0.
    2. Iterate through the string with the `right` pointer:
        - If the current character is already in the hash map and its last occurrence index is greater than or equal to `left`, update `left` to the index right after the last occurrence.
        - Update the hash map with the current character's index.
        - Update `max_length` as the maximum of its current value and the window size.
    3. Return `max_length`.

```python
def length_of_longest_substring(s: str) -> int:
	left = 0
	max_length = 0
	last_indicies = {}

	for right in range(len(s)):
		if s[right] in last_indicies and last_indicies[s[right]] >= left:
			left = last_indicies[s[right]] + 1

		last_indicies[s[right]] = right
		max_length = max(max_length, right - left + 1)

	return max_length
```
