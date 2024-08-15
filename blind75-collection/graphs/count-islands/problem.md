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

```pseudo
function numIslands(grid):
	if not grid:
		return 0

	def bfs(startX, startY):
		queue = [(startX, startY)]
		grid[startX][startY] = '0'  # Mark the cell as visited
		while queue is not empty:
			x, y = queue.pop(0)
			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				newX, newY = x + dx, y + dy
				if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[0]) and grid[newX][newY] == '1':
					grid[newX][newY] = '0'  # Mark the cell as visited
					queue.append((newX, newY))

	islandCount = 0
	for i from 0 to len(grid) - 1:
		for j from 0 to len(grid[0]) - 1:
			if grid[i][j] == '1':
				bfs(i, j)
				islandCount += 1

	return islandCount
```

---

### Approach 2: Union-Find (Disjoint Set)

-   **Time Complexity**: `O(m * n)` for processing all cells.
-   **Space Complexity**: `O(m * n)` for the parent and rank arrays.
-   **Description**: Union-Find is used to dynamically connect cells that are part of the same island. The number of unique roots at the end represents the number of islands.
-   **Algorithm**:

    1.  Initialize an array `parent` where each cell is its own parent.
    2.  Initialize an array `rank` to keep track of the tree height for each node.
    3.  Define the `find(x)` function to find the root of `x`.
    4.  Define the `union(x, y)` function to unite the sets containing `x` and `y`.
    5.  Iterate over the grid and for each cell that is `'1'`, union it with its adjacent `'1'`s.
    6.  Count the number of unique roots representing distinct islands.

```pseudo
function numIslands(grid):
	if not grid:
		return 0

	rows = len(grid)
	cols = len(grid[0])
	parent = a map of keys from 0 to rows * cols - 1 where grid[i][j] == '1' initialized to its own index
	rank = an array of size rows * cols initialized to 1 for each index where grid[i][j] == '1'

	def find(x):
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

	def union(x, y):
		rootX = find(x)
		rootY = find(y)
		if rootX != rootY:
			if rank[rootX] > rank[rootY]:
				parent[rootY] = rootX
			else if rank[rootX] < rank[rootY]:
				parent[rootX] = rootY
			else:
				parent[rootY] = rootX
				rank[rootX] += 1

	for i from 0 to rows - 1:
		for j from 0 to cols - 1:
			if grid[i][j] == '1':
				for dx, dy in [(1, 0), (0, 1)]:
					newX = i + dx
					newY = j + dy
					if newX >= 0 and newY >= 0 and newX < rows and newY < cols and grid[newX][newY] == '1':
						union(i * cols + j, newX * cols + newY)

	return len(set(find(x) for x in parent))
```
