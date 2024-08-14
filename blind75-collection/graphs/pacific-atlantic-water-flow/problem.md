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

```pseudo
function pacificAtlantic(heights):
	if not heights or not heights[0]:
		return []

	rows, cols = len(heights), len(heights[0])
	pacificReachable = set()
	atlanticReachable = set()

	function dfs(r, c, reachable):
		reachable.add((r, c))
		for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			newR, newC = r + dr, c + dc
			if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in reachable and heights[newR][newC] >= heights[r][c]:
				dfs(newR, newC, reachable)

	for i in initialize range of rows:
		dfs(i, 0, pacificReachable)
		dfs(i, cols - 1, atlanticReachable)

	for j in initialize range of cols:
		dfs(0, j, pacificReachable)
		dfs(rows - 1, j, atlanticReachable)

	res = []
	for r in initialize range of rows:
		for c in initialize range of cols:
			if (r, c) in pacificReachable and (r, c) in atlanticReachable:
				res.append([r, c])

	return res
```

---

### Approach 2: Breadth-First Search (BFS)

-   **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.
-   **Space Complexity:** `O(m * n)` in the worst case for the BFS queue.
-   **Description:** Similar to DFS, but we use BFS from the ocean edges, gradually marking the cells that can flow to each ocean and then finding the intersection.
-   **Algorithm:**

    1. Create two matrices to track cells reachable from each ocean.
    2. Perform BFS for each ocean from its respective borders.
    3. The BFS will explore cells in layers, marking reachable cells as it goes.
    4. The intersection of the two matrices gives the desired cells.

```pseudo
function pacificAtlantic(heights):
	if not heights or not heights[0]:
		return []

	rows, cols = len(heights), len(heights[0])
	pacificReachable = initialize a matrix of False with dimensions (rows, cols)
	atlanticReachable = initialize a matrix of False with dimensions (rows, cols)
	pacificQueue = initialize a queue with all cells along the Pacific border
	atlanticQueue = initialize a queue with all cells along the Atlantic border

	def bfs(queue, reachable):
		while queue:
			r, c = queue.pop(0)
			reachable[r][c] = True
			for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				newR, newC = r + dr, c + dc
				if 0 <= newR < rows and 0 <= newC < cols and not reachable[newR][newC] and heights[newR][newC] >= heights[r][c]:
					queue.append((newR, newC))

	bfs(pacificQueue, pacificReachable)
	bfs(atlanticQueue, atlanticReachable)

	res = []
	for r in initialize range of rows:
		for c in initialize range of cols:
			if pacificReachable[r][c] and atlanticReachable[r][c]:
				res.append([r, c])

	return res
```
