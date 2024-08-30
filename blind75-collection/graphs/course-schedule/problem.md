# Blind75: Course Schedule

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`.

The pair `[0, 1]` indicates that you must take course `1` before taking course `0`.

There are a total of `num_courses` courses you are required to take, labeled from `0` to `num_courses - 1`.

Return `True` if it is possible to finish all courses, otherwise return `False`.

**Example 1:**

-   **Input**: `num_courses = 2`, `prerequisites = [[0,1]]`
-   **Output**: `True`
-   **Explanation**: First take course `1` (no prerequisites) and then take course `0`.

**Example 2:**

-   **Input**: `num_courses = 2`, `prerequisites = [[0,1],[1,0]]`
-   **Output**: `False`
-   **Explanation**: In order to take course `1`, you must take course `0`, and to take course `0`, you must take course `1`. This forms a cycle, making it impossible.

### Constraints

-   `1 <= num_courses <= 1000`
-   `0 <= len(prerequisites) <= 1000`
-   All prerequisite pairs are unique.

---

### Approach 1: Topological Sort using Kahn's Algorithm

-   **Time Complexity**: `O(V + E)` where `V` is the number of courses (nodes) and `E` is the number of prerequisite pairs (edges).
-   **Space Complexity**: `O(V + E)` to store the graph and the indegree array.
-   **Description**: We can use Kahn's Algorithm for topological sorting, which involves iteratively removing nodes with no incoming edges (indegree 0) from the graph. If we can remove all nodes this way, there is no cycle, and all courses can be completed.
-   **Algorithm**:

    1.  Create an adjacency list to represent the graph and an array to store the indegree of each node.
    2.  Initialize a queue and add all nodes with indegree 0.
    3.  Process each node in the queue by:
        -   Removing the node from the queue.
        -   Decreasing the indegree of its neighbors.
        -   Adding neighbors with indegree 0 to the queue.
    4.  After processing all nodes, if the number of nodes processed equals `num_courses`, return `True` (no cycle exists); otherwise, return `False` (a cycle exists).

```python
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
        indegree = [0] * num_courses

	for course, prereq in prerequisites:
		graph[prereq].append(course)
		indegree[course] += 1

	queue = [i for i in range(num_courses) if indegree[i] == 0]
    processedCourses = 0

	while queue:
		node = queue.pop(0)
		processed_courses += 1

		for neighbor in graph[node]:
			indegree[neighbor] -= 1

			if indegree[neighbor] == 0:
				queue.append(neighbor)

	return processed_courses == num_courses
```

---

### Approach 2: Depth-First Search (DFS) to Detect Cycles

-   **Time Complexity**: `O(V + E)` where `V` is the number of courses (nodes) and `E` is the number of prerequisite pairs (edges).
-   **Space Complexity**: `O(V + E)` to store the graph, recursion stack, and visited set.
-   **Description**: We can perform a DFS to detect cycles in the graph. If a cycle is detected, it means it's impossible to complete all courses. We use three states for each node: unvisited, visiting, and visited.
-   **Algorithm**:

    1.  Create an adjacency list to represent the graph.
    2.  Initialize a visited array with states `0` (unvisited), `1` (visiting), and `2` (visited).
    3.  Define a recursive function `dfs(node)`:
        -   If the node is visiting, return `True` (a cycle is detected).
        -   If the node is visited, return `False`.
        -   Mark the node as visiting.
        -   Recursively visit all its neighbors.
        -   After visiting all neighbors, mark the node as visited and return `False`.
    4.  Iterate over all nodes and call `dfs(node)` for unvisited nodes.
    5.  If any call to `dfs` returns `True`, return `False`. Otherwise, return `True`.

```python
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    visited = [0] * num_courses

	for course, prereq in prerequisites:
		graph[prereq].append(course)

	def dfs(node: int) -> bool:
		if visited[node] == 1:
			return True

		if visited[node] == 2:
			return False

		visited[node] = 1

		for neighbor in graph[node]:
			if dfs(neighbor):
				return True

		visited[node] = 2
		return False

	for i in range(num_courses):
		if visited[i] == 0 and dfs(i):
			return False

	return True
```
