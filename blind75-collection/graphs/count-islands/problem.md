Here's the updated markdown file with your preferences incorporated:

---

# Blind75: Count Islands

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a 2D grid `grid` where `'1'` represents land and `'0'` represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water surrounds the grid (i.e., all the edges are water).

**Example 1:**

-   **Input**:
    ```
    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    ```
-   **Output**: `1`

**Example 2:**

-   **Input**:
    ```
    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    ```
-   **Output**: `4`

**Example 3:**

-   **Input**:
    ```
    grid = [
        ["1","0","1","1","0","1","1"]
    ]
    ```
-   **Output**: `3`

### Constraints

-   `1 <= len(grid), len(grid[i]) <= 100`
-   `grid[i][j]` is `'0'` or `'1'`.

---

### Approach 1: Breadth-First Search (BFS)

-   **Time Complexity**: `O(m * n)` where `m` is the number of rows and `n` is the number of columns.
-   **Space Complexity**: `O(min(m, n))` for the queue.
-   **Description**: BFS can also be used to explore each island. When a `'1'` is found, BFS is initiated to explore all its connected cells. These cells are then marked as visited to avoid counting the same island multiple times.
-   **Algorithm**:

    1.  Initialize a counter for the number of islands.
    2.  Iterate over each cell in the grid.
        -   If a cell contains `'1'`, it represents the start of a new island.
        -   Perform BFS from this cell to visit all connected `'1'`s, marking them as `'0'`.
        -   Increment the island counter.
    3.  Return the total number of islands.

```python
def num_islands(grid: List[List[str]]) -> int:
	if not grid:
		return 0

	def bfs(startX: int, startY: int) -> None:
		queue = [(startX, startY)]
		grid[startX][startY] = '0'

		while queue is not empty:
			x, y = queue.pop(0)

			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				newX, newY = x + dx, y + dy

				if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[0]) and grid[newX][newY] == '1':
					grid[newX][newY] = '0'
					queue.append((newX, newY))

	island_count = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '1':
				bfs(i, j)
				island_count += 1

	return island_count
```
