# Blind75: Maximum Subarray

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array of integers `nums`, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

**Example 1:**

-   **Input:** `nums = [2, -3, 4, -2, 2, 1, -1, 4]`
-   **Output:** `8`
-   **Explanation:** The subarray `[4, -2, 2, 1, -1, 4]` has the largest sum `8`.

**Example 2:**

-   **Input:** `nums = [-1]`
-   **Output:** `-1`

### Constraints

-   `1 <= len(nums) <= 1000`
-   `-1000 <= nums[i] <= 1000`

---

### Approach 1: Kadane's Algorithm

-   **Time Complexity:** `O(n)` where `n` is the length of the array.
-   **Space Complexity:** `O(1)`
-   **Description:** Kadane's algorithm is a dynamic programming approach to solve this problem in linear time. It iterates through the array, and at each position, it calculates the maximum subarray sum that ends at that position by taking the maximum of the current element or the sum of the current element and the maximum subarray sum ending at the previous position. The global maximum is updated accordingly.
-   **Algorithm:**

    1. Initialize two variables: `maxSum` to hold the global maximum sum and `currentSum` to hold the current subarray sum. Set both to the first element of the array.
    2. Iterate through the array starting from the second element:
        - Update `currentSum` to the maximum of the current element and `currentSum + nums[i]`.
        - Update `maxSum` to the maximum of `maxSum` and `currentSum`.
    3. Return `maxSum` after the loop.

```python
function max_subarray(nums):
	maxSum = nums[0]
	currentSum = nums[0]
	for i in initialize range from 1 to len(nums):
		currentSum = max(nums[i], currentSum + nums[i])
		maxSum = max(maxSum, currentSum)
	return maxSum
```
