# Blind75: Pacific Atlantic Water Flow

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given a rectangular grid `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island borders the Pacific Ocean on the top and left sides, and the Atlantic Ocean on the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal to or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return a 2D list where each element is a list `[r, c]` representing the row and column of the cell. You may return the answer in any order.

**Example 1:**

-   **Input:**
    ```
    heights = [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 4, 7],
        [6, 3, 5, 3, 6]
    ]
    ```
-   **Output:** `[[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]]`

**Example 2:**

-   **Input:** `heights = [[1], [1]]`
-   **Output:** `[[0, 0], [1, 0]]`

### Constraints

-   `1 <= len(heights), len(heights[r]) <= 100`
-   `0 <= heights[r][c] <= 1000`

---

### Approach 1: Depth-First Search (DFS)

-   **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.
-   **Space Complexity:** `O(m * n)` for maintaining the visited sets.
-   **Description:** We use DFS starting from the ocean borders but optimize by using an early termination strategy. If a cell has already been determined to be able to reach both oceans, further exploration from that cell is unnecessary. This reduces redundant computations.
-   **Algorithm:**

    1. Create two sets to track cells that can flow to the Pacific and Atlantic oceans.
    2. Perform DFS starting from the cells adjacent to the Pacific and Atlantic oceans, respectively, marking reachable cells.
    3. For each DFS, if a cell has already been marked as reachable to both oceans, terminate further exploration from that cell.
    4. The final result is the intersection of the cells marked for both oceans.

```python
def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
	if not heights or not heights[0]:
		return []

	rows, cols = len(heights), len(heights[0])
	pacific_reachable = set()
	atlantic_reachable = set()

	def dfs(r: int, c: int, reachable: set) -> None:
		reachable.add((r, c))

		for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			newR, newC = r + dr, c + dc

			if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in reachable and heights[newR][newC] >= heights[r][c]:
				dfs(newR, newC, reachable)

	for i in range(rows):
		dfs(i, 0, pacific_reachable)
		dfs(i, cols - 1, atlantic_reachable)

	for j in range(cols):
		dfs(0, j, pacific_reachable)
		dfs(rows - 1, j, atlantic_reachable)

	res = []
	for r in range(rows):
		for c in range(cols):
			if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
				res.append([r, c])

	return res
```
