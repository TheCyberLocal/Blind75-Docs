# Blind75: Longest Palindromic Substring

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s`, return the longest substring of `s` that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

**Example 1:**

-   **Input**: `s = "ababd"`
-   **Output**: `"bab"`
-   **Explanation**: Both `"aba"` and `"bab"` are valid answers.

**Example 2:**

-   **Input**: `s = "abbc"`
-   **Output**: `"bb"`

### Constraints

-   `1 <= len(s) <= 1000`
-   `s` is alphanumeric.

---

### Approach 1: Expand Around Center and Store Result

-   **Time Complexity**: `O(n^2)`
-   **Space Complexity**: `O(1)`
-   **Description**: This approach identifies the longest palindrome by treating each character (and each pair of consecutive characters) as the potential center of a palindrome. It directly updates a result string with the current longest palindrome as it iterates through the centers.
-   **Algorithm**:

    1. Initialize two variables `result` and `res_len` to track the longest palindromic substring and its length.
    2. Define a helper function `pali_len(left, right)` that expands around the center indices `left` and `right` while the characters on both sides are equal.
    3. For each center index `i` in the string `s`, call `pali_len` twice: once for odd-length palindromes (centered at `i`) and once for even-length palindromes (centered between `i` and `i + 1`).
    4. Update `res` and `res_len` if a longer palindrome is found during the expansion.
    5. Return the longest palindromic substring stored in `res`.

```python
def longest_palindrome(s: str) -> str:
	def pali_len(left: int, right: int) -> None:
			nonlocal res, res_len

			while left >= 0 and right < n and s[left] == s[right]:
				if (right - left + 1) > res_len:
					res = s[left:right + 1]
					res_len = right - left + 1

				left, right = left - 1, right + 1

	n = len(s)
	res = ""
	res_len = 0

	for i in range(n):
		pali_len(i, i)
		pali_len(i, i + 1)

	return res
```

---

### Approach 2: Expand Around Center and Track Indices

-   **Time Complexity**: `O(n^2)`
-   **Space Complexity**: `O(1)`
-   **Description**: This approach identifies the longest palindrome by treating each character (and each pair of consecutive characters) as the potential center of a palindrome. It tracks the longest palindrome indicies as it iterates through the centers.
-   **Algorithm**:

    1. Initialize two variables `start` and `end` to track the beginning and ending indices of the longest palindrome found.
    2. Define a helper function `pali_len(left, right)` that expands around the center indices `left` and `right` while the characters on both sides are equal.
    3. Iterate over the string `s`, considering each character as the center of the palindrome.
    4. For each center, expand around it while the characters on both sides are equal.
    5. Update the `start` and `end` indices if a longer palindrome is found.
    6. Return the substring of `s` from `start` to `end + 1`.

```python
def longest_palindrome(s: str) -> str:
	def pali_len(left: int, right: int) -> int:
		while left >= 0 and right < len(s) and s[left] == s[right]:
			left, right = left - 1, right + 1

		return right - left - 1

	start = end = 0

	for i in range(len(s)):
		len1 = pali_len(i, i)
		len2 = pali_len(i, i + 1)
		max_len = max(len1, len2)

		if max_len > end - start:
			start = i - (max_len - 1) // 2
			end = i + max_len // 2

	return s[start:end + 1]
```
