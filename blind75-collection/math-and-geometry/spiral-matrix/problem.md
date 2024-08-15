# Blind75: Spiral Matrix

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

Given an `m x n` matrix of integers `matrix`, return a list of all elements within the matrix in spiral order.

**Example 1:**

-   **Input:**
    ```
    matrix = [[1,2],[3,4]]
    ```
-   **Output:**
    ```
    [1,2,4,3]
    ```

**Example 2:**

-   **Input:**
    ```
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    ```
-   **Output:**
    ```
    [1,2,3,6,9,8,7,4,5]
    ```

**Example 3:**

-   **Input:**
    ```
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ```
-   **Output:**
    ```
    [1,2,3,4,8,12,11,10,9,5,6,7]
    ```

### Constraints

-   `1 <= len(matrix), len(matrix[0]) <= 10`
-   `-100 <= matrix[i][j] <= 100`

---

### Approach 1: Layer-by-Layer Traversal

-   **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.
-   **Space Complexity:** `O(1)` in terms of auxiliary space, although the output list will have a size of `m * n`.
-   **Description:** This approach traverses the matrix in layers, moving from the outermost elements towards the center. We define four boundaries: top, bottom, left, and right. We iterate through these boundaries, adding elements to the output list in the order of top row, right column, bottom row, and left column. After processing each layer, we move the boundaries inward and continue until all elements are processed.
-   **Algorithm:**

    1. Initialize `top`, `bottom`, `left`, and `right` boundaries to represent the edges of the matrix.
    2. While `top` is less than or equal to `bottom` and `left` is less than or equal to `right`:
        - Traverse from `left` to `right` along the `top` boundary, and then increment `top`.
        - Traverse from `top` to `bottom` along the `right` boundary, and then decrement `right`.
        - Traverse from `right` to `left` along the `bottom` boundary if `top` still <= `bottom`, and then decrement `bottom`.
        - Traverse from `bottom` to `top` along the `left` boundary if `left` still <= `right`, and then increment `left`.
    3. Return the list of elements collected in spiral order.

```pseudo
function spiralOrder(matrix):
	m = len(matrix)
	n = len(matrix[0])
	top , bottom = 0, m
    left, right = 0, n
	result = []

	while top <= bottom and left <= right:
		for j from left to right:
			result.append(matrix[top][j])
		top = top + 1

		for i from top to bottom:
			result.append(matrix[i][right])
		right = right - 1

		if top <= bottom:
			for j from right to left:
				result.append(matrix[bottom][j])
			bottom = bottom - 1

		if left <= right:
			for i from bottom to top:
				result.append(matrix[i][left])
			left = left + 1

	return result
```
