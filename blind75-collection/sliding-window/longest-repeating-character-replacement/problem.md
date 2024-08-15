# Blind75: Longest Repeating Character Replacement

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

You are given a string `s` consisting of only uppercase letters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase letter.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

**Example 1:**

-   **Input:**
    ```
    s = "XYYX", k = 2
    ```
-   **Output:**
    ```
    4
    ```
    Explanation: Either replace the `'X'`s with `'Y'`s, or replace the `'Y'`s with `'X'`s.

**Example 2:**

-   **Input:**
    ```
    s = "AAABABB", k = 1
    ```
-   **Output:**
    ```
    5
    ```
    Explanation: Replace the `'B'` at index 4 with `'A'` to form the substring `"AAAAA"`.

### Constraints

-   `1 <= len(s) <= 1000`
-   `0 <= k <= len(s)`

---

### Approach 1: Sliding Window

-   **Time Complexity:** `O(n)`, where `n` is the length of the string.
-   **Space Complexity:** `O(1)` since the space usage does not depend on the input size.
-   **Description:** The sliding window approach keeps track of the frequency of characters within the window. The window is expanded by moving the right pointer, and when the number of characters that need to be replaced exceeds `k`, the left pointer is moved to shrink the window. The goal is to maximize the length of the window where the number of replacements does not exceed `k`.
-   **Algorithm:**

    1. Initialize variables `left` to 0, `maxCount` to 0, and `maxLength` to 0. Use a frequency array to keep track of character counts in the current window.
    2. Iterate through the string with `right` pointer:
        - Update the frequency of the current character and find the maximum frequency (`maxCount`) of any character in the current window.
        - If the length of the window minus `maxCount` is greater than `k`, increment the `left` pointer to shrink the window.
        - Update `maxLength` as the maximum of its current value and the window size.
    3. Return `maxLength`.

```pseudo
function characterReplacement(s, k):
	left = 0
	maxCount = 0
	maxLength = 0
	freq = array of size 26 initialized to 0

	for right from 0 to len(s) - 1:
		charIndex = ascii(s[right]) - ascii('A')
		freq[charIndex] += 1
		maxCount = max(maxCount, freq[charIndex])

		while (right - left + 1) - maxCount > k:
			freq[ascii(s[left]) - ascii('A')] -= 1
			left += 1

		maxLength = max(maxLength, right - left + 1)

	return maxLength
```
