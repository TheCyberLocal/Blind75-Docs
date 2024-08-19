# Blind75: Container With Most Water

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer array `heights` where `heights[i]` represents the height of the `i`-th bar. You may choose any two bars to form a container. Return the maximum amount of water a container can store.

**Example 1:**

-   **Input:** `height = [1,7,2,5,4,7,3,6]`
-   **Output:** `36`

**Example 2:**

-   **Input:** `height = [2,2,2]`
-   **Output:** `4`

### Constraints

-   `2 <= len(height) <= 1000`
-   `0 <= height[i] <= 1000`

---

### Approach 1: Two Pointers

-   **Time Complexity:** `O(n)`, where `n` is the length of `height`.
-   **Space Complexity:** `O(1)`.
-   **Description:** You are given an integer array `heights`, where `heights[i]` represents the height of the i-th bar. You may choose any two bars to form a container, and the task is to return the maximum amount of water that a container can store. The amount of water a container can store is determined by the shorter of the two chosen bars and the distance between them. The goal is to maximize this value by selecting the appropriate pair of bars.
-   **Algorithm:**

    1. Initialize `left` to `0` and `right` to `len(heights) - 1`.
    2. Set `maxWater` to `0`.
    3. While `left` is less than `right`:
        1. Calculate the width as `right - left`.
        2. Determine the minimum height between `heights[left]` and `heights[right]`.
        3. Calculate the current area as `width * min(heights[left], heights[right])`.
        4. Update `maxWater` to be the maximum of `maxWater` and `current area`.
        5. If `heights[left]` is less than `heights[right]`, increment `left`; otherwise, decrement `right`.
    4. Return `maxWater`.

```pseudo
function maxArea(heights):
	left, right = 0, len(heights) - 1
	maxWater = 0
	while left < right:
		width = right - left
		currentHeight = min(heights[left], heights[right])
		currentArea = width * currentHeight
		maxWater = max(maxWater, currentArea)
		if heights[left] < heights[right]:
			left += 1
		else:
			right -= 1
	return maxWater
```
