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
-   **Description:**

    -   Use two pointers, `left` starting at the beginning and `right` at the end of the `height` array.
    -   Calculate the area formed between the bars at `left` and `right`.
    -   Move the pointer with the shorter bar inward to potentially find a larger container.
    -   Continue this process until the pointers meet.

-   **Algorithm:**

    1. Initialize `left` to `0` and `right` to `len(height) - 1`.
    2. Set `maxWater` to `0`.
    3. While `left` is less than `right`:
        1. Calculate the width as `right - left`.
        2. Determine the minimum height between `height[left]` and `height[right]`.
        3. Calculate the current area as `width * min(height[left], height[right])`.
        4. Update `maxWater` to be the maximum of `maxWater` and `current area`.
        5. If `height[left]` is less than `height[right]`, increment `left`; otherwise, decrement `right`.
    4. Return `maxWater`.

```pseudo
function maxArea(height):
	left = 0
	right = len(height) - 1
	maxWater = 0
	while left < right:
		width = right - left
		currentHeight = min(height[left], height[right])
		currentArea = width * currentHeight
		maxWater = max(maxWater, currentArea)
		if height[left] < height[right]:
			left += 1
		else:
			right -= 1
	return maxWater
```
