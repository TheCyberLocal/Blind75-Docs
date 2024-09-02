# Blind75: Jump Game

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer array `nums` where each element `nums[i]` indicates your maximum jump length at that position.

Return `True` if you can reach the last index starting from index `0`, or `False` otherwise.

**Example 1:**

-   **Input:** `nums = [1, 2, 0, 1, 0]`
-   **Output:** `True`
-   **Explanation:** First jump from index `0` to `1`, then from index `1` to `3`, and lastly from index `3` to `4`.

**Example 2:**

-   **Input:** `nums = [1, 2, 1, 0, 1]`
-   **Output:** `False`

### Constraints

-   `1 <= len(nums) <= 1000`
-   `0 <= nums[i] <= 1000`

---

### Approach 1: Greedy

-   **Time Complexity:** `O(n)` where `n` is the length of the array.
-   **Space Complexity:** `O(1)`
-   **Description:** The idea is to keep track of the farthest index that can be reached. Starting from the first index, iterate through the array and update the farthest reachable index. If at any point, the current index is beyond the farthest reachable index, return `False`. If the last index is within or equal to the farthest reachable index, return `True`.
-   **Algorithm:**

    1. Initialize a variable `farthest` to keep track of the farthest index that can be reached, starting with `0`.
    2. Iterate through the array:
        - If the current index is greater than `farthest`, return `False`.
        - Update `farthest` to be the maximum of `farthest` and `i + nums[i]`.
    3. After the loop, return `True` if `farthest` is greater than or equal to the last index.

```python
def can_jump(nums: List[int]) -> bool:
	n = len(nums)
	farthest = 0

	for i in range(n):
		if i > farthest:
			return False

		farthest = max(farthest, i + nums[i])

	return farthest >= n - 1
```
