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

-   **Input:**

    ```
    heights = [[1], [1]]
    ```

-   **Output:** `[[0, 0], [1, 0]]`

### Constraints

-   `1 <= len(heights), len(heights[r]) <= 100`
-   `0 <= heights[r][c] <= 1000`

---

### Approach 1: Depth-First Search (DFS)

-   **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.
-   **Space Complexity:** `O(m * n)` in the worst case for the recursive stack.
-   **Description:** The idea is to use DFS starting from the ocean edges and moving inwards. We'll mark the cells that can flow into each ocean and then find the intersection of these cells.
-   **Algorithm:**

    1. Create two matrices to track which cells can flow to the Pacific and Atlantic oceans.
    2. Perform DFS for each cell on the Pacific and Atlantic borders.
    3. For each DFS, mark the cells that can flow to the respective ocean.
    4. The final result is the intersection of cells marked for both oceans.

```pseudo
function pacificAtlantic(heights):
	if not heights or not heights[0]:
		return []

	rows, cols = len(heights), len(heights[0])
	pacificReachable = initialize a matrix of False with dimensions (rows, cols)
	atlanticReachable = initialize a matrix of False with dimensions (rows, cols)

	def dfs(r, c, reachable):
		reachable[r][c] = True
		for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			newR, newC = r + dr, c + dc
			if 0 <= newR < rows and 0 <= newC < cols and not reachable[newR][newC] and heights[newR][newC] >= heights[r][c]:
				dfs(newR, newC, reachable)

	for i in initialize range of rows:
		dfs(i, 0, pacificReachable)
		dfs(i, cols - 1, atlanticReachable)

	for j in initialize range of cols:
		dfs(0, j, pacificReachable)
		dfs(rows - 1, j, atlanticReachable)

	result = []
	for r in initialize range of rows:
		for c in initialize range of cols:
			if pacificReachable[r][c] and atlanticReachable[r][c]:
				result.append([r, c])

	return result
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

	result = []
	for r in initialize range of rows:
		for c in initialize range of cols:
			if pacificReachable[r][c] and atlanticReachable[r][c]:
				result.append([r, c])

	return result
```

---

### Approach 3: Matrix Reduction

-   **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.
-   **Space Complexity:** `O(m * n)` for maintaining the reachable matrices.
-   **Description:** The Matrix Reduction approach involves reducing the problem to finding cells that are reachable from both oceans by using similar methods as DFS or BFS but focusing on reducing the matrix to areas of interest iteratively.
-   **Algorithm:**

    1. Create matrices to track cells that can flow to each ocean.
    2. Start from the borders and reduce the matrix by marking cells that can flow to the oceans.
    3. Continue reducing until all possible flows are found.
    4. The final cells that can reach both oceans are your answer.

```pseudo
function pacificAtlantic(heights):
	if not heights or not heights[0]:
		return []

	rows, cols = len(heights), len(heights[0])
	pacificReachable = initialize a matrix of False with dimensions (rows, cols)
	atlanticReachable = initialize a matrix of False with dimensions (rows, cols)

	def reduceMatrix(r, c, ocean):
		if ocean == "pacific":
			return r == 0 or c == 0 or (r > 0 and pacificReachable[r - 1][c]) or (c > 0 and pacificReachable[r][c - 1])
		else:
			return r == rows - 1 or c == cols - 1 or (r < rows - 1 and atlanticReachable[r + 1][c]) or (c < cols - 1 and atlanticReachable[r][c + 1])

	for r in initialize range of rows:
		for c in initialize range of cols:
			if reduceMatrix(r, c, "pacific"):
				pacificReachable[r][c] = True
			if reduceMatrix(r, c, "atlantic"):
				atlanticReachable[r][c] = True

	result = []
	for r in initialize range of rows:
		for c in initialize range of cols:
			if pacificReachable[r][c] and atlanticReachable[r][c]:
				result.append([r, c])

	return result
```
