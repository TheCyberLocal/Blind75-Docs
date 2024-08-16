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

```pseudo
function maxSubArray(nums):
	maxSum = nums[0]
	currentSum = nums[0]
	for i in initialize range from 1 to len(nums):
		currentSum = max(nums[i], currentSum + nums[i])
		maxSum = max(maxSum, currentSum)
	return maxSum
```

---

### Approach 2: Divide and Conquer

-   **Time Complexity:** `O(n log n)` where `n` is the length of the array.
-   **Space Complexity:** `O(log n)` due to recursion stack space.
-   **Description:** This approach divides the array into two halves and finds the maximum subarray sum for the left half, right half, and a subarray that crosses the midpoint. The final result is the maximum of these three sums.
-   **Algorithm:**

    1. If the array contains only one element, return that element.
    2. Find the midpoint of the array and recursively find the maximum subarray sum for the left and right halves.
    3. Find the maximum sum of a subarray that crosses the midpoint.
    4. Return the maximum of the left half, right half, and crossing subarray sums.

```pseudo
function maxSubArray(nums):
	function helper(left, right):
		if left == right:
		 return nums[left]
		mid = (left + right) // 2
		leftSum = helper(left, mid)
		rightSum = helper(mid + 1, right)
		crossSum = findCrossSum(nums, left, mid, right)
		return max(leftSum, rightSum, crossSum)

	function findCrossSum(nums, left, mid, right):
		leftMax = float('-inf')
		rightMax = float('-inf')
		currentSum = 0
		for i in range(mid, left - 1, -1):
			currentSum += nums[i]
			leftMax = max(leftMax, currentSum)
		currentSum = 0
		for i in range(mid + 1, right + 1):
			currentSum += nums[i]
			rightMax = max(rightMax, currentSum)
		return leftMax + rightMax

	return helper(0, len(nums) - 1)
```
