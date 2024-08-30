# Blind75: Count Connected Components

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

There is an undirected graph with `n` nodes. There is also an `edges` array, where `edges[i] = [a, b]` means that there is an edge between node `a` and node `b` in the graph.

The nodes are numbered from `0` to `n - 1`.

Return the total number of connected components in that graph.

**Example 1:**

-   **Input**: `n = 3`, `edges = [[0,1], [0,2]]`
-   **Output**: `1`

**Example 2:**

-   **Input**: `n = 6`, `edges = [[0,1], [1,2], [2,3], [4,5]]`
-   **Output**: `2`

### Constraints

-   `1 <= n <= 100`
-   `0 <= len(edges) <= n * (n - 1) / 2`

---

### Approach 1: Depth-First Search (DFS)

-   **Time Complexity**: `O(V + E)` where `V` is the number of nodes and `E` is the number of edges.
-   **Space Complexity**: `O(V + E)` for storing the adjacency list and visited set.
-   **Description**: The goal is to find the number of connected components in the graph. We can use DFS to explore each component and count how many separate DFS traversals are needed to visit all nodes. Each DFS traversal represents a connected component.
-   **Algorithm**:

    1.  Initialize an adjacency list to represent the graph.
    2.  Create a visited set to track visited nodes.
    3.  Define a recursive `dfs(node)` function:
        -   Mark `node` as visited.
        -   Recursively visit all its neighbors.
    4.  Iterate over all nodes:
        -   If a node is unvisited, perform a DFS and increment the component count.
    5.  Return the total count of connected components.

```python
def count_components(n: int, edges: List[List[int]]) -> int:
	graph = {i: [] for i in range(n)}
	visited = set()
	count = 0

	for x, y in edges:
		graph[x].append(y)
		graph[y].append(x)

	def dfs(node: Node) -> None:
		visited.add(node)

		for neighbor in graph[node]:
			if neighbor not in visited:
				dfs(neighbor)

	for i in range(n):
		if i not in visited:
			dfs(i)
			count += 1

	return count
```

---

### Approach 2: Union-Find

-   **Time Complexity**: `O(E * α(V))`, where `α` is the inverse Ackermann function.
-   **Space Complexity**: `O(V)` for storing the parent and rank arrays.
-   **Description**: Union-Find (Disjoint Set) is used to group nodes into components efficiently. The `union` operation merges two sets, and the `find` operation identifies the root of a node. We iterate through all edges to perform unions and count the unique roots at the end to determine the number of connected components.
-   **Algorithm**:

    1.  Initialize the `parent` array where each node is its own parent.
    2.  Initialize the `rank` array to manage tree height.
    3.  Define the `find(x)` function to find the root of `x`.
    4.  Define the `union(x, y)` function to unite the sets containing `x` and `y`.
        -   Find the roots of `x` and `y`.
        -   If the roots are different, unite them based on rank.
    5.  Iterate through the edges, applying `union` on each pair.
    6.  Count the number of unique roots to determine the number of connected components.

```python
def count_components(n: int, edges: List[List[int]]) -> int:
	parent = list(range(n))
	rank = [1] * n

	def find(x: int) -> int:
		if parent[x] != x:
			parent[x] = find(parent[x])

		return parent[x]

	def union(x: int, y: int) -> None:
		rootX = find(x)
		rootY = find(y)

		if rootX != rootY:
			if rank[rootX] > rank[rootY]:
				parent[rootY] = rootX
			elif rank[rootX] < rank[rootY]:
				parent[rootX] = rootY
			else:
				parent[rootY] = rootX
				rank[rootX] += 1

	for x, y in edges:
		union(x, y)

	unique_roots = {find(i) for i in range(n)}
	return len(unique_roots)
```
