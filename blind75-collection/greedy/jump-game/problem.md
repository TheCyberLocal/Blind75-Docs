# Blind75: Jump Game

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer array `nums` where each element `nums[i]` indicates your maximum jump length at that position.

Return `true` if you can reach the last index starting from index `0`, or `false` otherwise.

**Example 1:**

-   **Input:** `nums = [1, 2, 0, 1, 0]`
-   **Output:** `true`
-   **Explanation:** First jump from index `0` to `1`, then from index `1` to `3`, and lastly from index `3` to `4`.

**Example 2:**

-   **Input:** `nums = [1, 2, 1, 0, 1]`
-   **Output:** `false`

### Constraints

-   `1 <= len(nums) <= 1000`
-   `0 <= nums[i] <= 1000`

---

### Approach 1: Greedy

-   **Time Complexity:** `O(n)` where `n` is the length of the array.
-   **Space Complexity:** `O(1)`
-   **Description:** The idea is to keep track of the farthest index that can be reached. Starting from the first index, iterate through the array and update the farthest reachable index. If at any point, the current index is beyond the farthest reachable index, return `false`. If the last index is within or equal to the farthest reachable index, return `true`.
-   **Algorithm:**

    1. Initialize a variable `farthest` to keep track of the farthest index that can be reached, starting with `0`.
    2. Iterate through the array:
        - If the current index is greater than `farthest`, return `false`.
        - Update `farthest` to be the maximum of `farthest` and `i + nums[i]`.
    3. After the loop, return `true` if `farthest` is greater than or equal to the last index.

```pseudo
function canJump(nums):
	farthest = 0
	for i in initialize range of len(nums):
		if i > farthest:
			return false
		farthest = max(farthest, i + nums[i])
	return farthest >= len(nums) - 1
```

---

### Approach 2: Dynamic Programming

-   **Time Complexity:** `O(n^2)` where `n` is the length of the array.
-   **Space Complexity:** `O(n)`
-   **Description:** This approach uses a DP array where `dp[i]` indicates whether it is possible to reach the `i`th index. Start from the first index and try to update the DP array for all reachable indices.
-   **Algorithm:**

    1. Initialize a DP array `dp` with `false`, except `dp[0] = true`.
    2. Iterate through each index `i`:
        - If `dp[i]` is `true`, update all positions from `i + 1` to `i + nums[i]` to `true`.
    3. Return the value at `dp[-1]`.

```pseudo
function canJump(nums):
	n = len(nums)
	dp = initialize array of false with length n
	dp[0] = true
	for i in initialize range of n:
		if dp[i]:
			for j in range(i + 1, min(i + nums[i] + 1, n)):
				dp[j] = true
	return dp[-1]
```

---

### Approach 3: Backtracking

-   **Time Complexity:** `O(2^n)` where `n` is the length of the array.
-   **Space Complexity:** `O(n)` for the recursion stack.
-   **Description:** This approach tries to jump to every possible position using backtracking. Starting from the first index, recursively check whether we can reach the last index by trying every possible jump.
-   **Algorithm:**

    1. Define a recursive function `canJumpFromPosition(i)`:
        - If `i` is the last index, return `true`.
        - Iterate over all possible jumps from the current index `i`.
        - Recursively check if it is possible to reach the last index from each of these jumps.
        - If any of these returns `true`, return `true`.
    2. Start the recursion from index `0`.

```pseudo
function canJump(nums):
	function canJumpFromPosition(i):
		if i >= len(nums) - 1:
			return true
		farthestJump = min(i + nums[i], len(nums) - 1)
		for j in range(i + 1, farthestJump + 1):
			if canJumpFromPosition(j):
			 return true
		return false
	return canJumpFromPosition(0)
```
