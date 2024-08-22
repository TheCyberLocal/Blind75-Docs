# Blind75: Palindromic Substrings

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s`, return the number of substrings within `s` that are palindromes.

A palindrome is a string that reads the same forward and backward.

**Example 1:**

-   **Input**: `s = "abc"`
-   **Output**: `3`
-   **Explanation**: `"a"`, `"b"`, `"c"`.

**Example 2:**

-   **Input**: `s = "aaa"`
-   **Output**: `6`
-   **Explanation**: `"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, `"aaa"`. Note that different substrings are counted as different palindromes even if the string contents are the same.

### Constraints

-   `1 <= len(s) <= 1000`
-   `s` consists only of lowercase letters.

---

### Approach 1: Expand Around Center

-   **Time Complexity**: `O(n^2)`
-   **Space Complexity**: `O(1)`
-   **Description**: This approach counts palindromic substrings by expanding around each character (and between each pair of characters) as the center. A palindrome can have either a single character as its center (odd-length palindromes) or two consecutive characters as its center (even-length palindromes). For each possible center, we expand outward as long as the characters on both sides are equal, counting the number of valid palindromic substrings. This method ensures that all possible palindromic substrings are considered.
-   **Algorithm**:

    1. Define a helper function `count_pali(left, right)` that takes two indices, `left` and `right`, and counts the number of palindromic substrings with the center between `s[left]` and `s[right]`.
        - Initialize a counter `count` to `0`.
        - Use a while loop to expand outward as long as `left` is non-negative, `right` is within bounds, and `s[left] == s[right]`.
        - Increment the `count` each time a valid palindrome is found.
        - Move `left` one step left and `right` one step right.
        - Return the `count`.
    2. Initialize a variable `res` to store the total number of palindromic substrings.
    3. Iterate over each index `i` in the string `s`:
        - Call `count_pali(i, i)` to count odd-length palindromes centered at `i`.
        - Call `count_pali(i, i + 1)` to count even-length palindromes centered between `i` and `i + 1`.
        - Add the results from these function calls to `res`.
    4. Return `res` as the total number of palindromic substrings.

```python
def countSubstrings(s: str) -> int:
	def count_pali(left: int, right: int) -> int:
		count = 0

		while left >= 0 and right < len(s) and s[left] == s[right]:
			count += 1
			left, right = left - 1, right + 1

		return count

	res = 0

	for i in range(len(s)):
		res += count_pali(i, i)
		res += count_pali(i, i + 1)

	return res
```
