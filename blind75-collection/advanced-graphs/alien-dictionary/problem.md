# Blind75: Alien Dictionary

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

There is an alien language that uses the Latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings `words` from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid orders of letters, return any of them.

A string `a` is lexicographically smaller than a string `b` if either of the following is true:

-   The first letter where they differ is smaller in `a` than in `b`.
-   There is no index `i` such that `a[i] != b[i]` and `len(a) < len(b)`.

**Example 1:**

-   **Input**: `["z","o"]`
-   **Output**: `"zo"`
-   **Explanation**: From "z" and "o", we know 'z' < 'o', so return `"zo"`.

**Example 2:**

-   **Input**: `["hrn","hrf","er","enn","rfnn"]`
-   **Output**: `"hernf"`
-   **Explanation**:
    -   From "hrn" and "hrf", we know 'n' < 'f'.
    -   From "hrf" and "er", we know 'h' < 'e'.
    -   From "er" and "enn", we know 'r' < 'n'.
    -   From "enn" and "rfnn", we know 'e' < 'r'.
    -   So one possible solution is `"hernf"`.

### Constraints

-   The input `words` will contain characters only from lowercase 'a' to 'z'.
-   `1 <= len(words) <= 100`
-   `1 <= len(words[i]) <= 100`

---

### Approach 1: Topological Sorting (Kahn's Algorithm)

-   **Time Complexity**: `O(n)` where `n` is the total number of characters in all words.
-   **Space Complexity**: `O(1)`
-   **Description**: We treat each character as a node in a directed graph, where an edge from node `u` to node `v` means that character `u` comes before character `v`. We construct this graph by comparing adjacent words in the list. After constructing the graph, we perform a topological sort to determine a valid order of characters.
-   **Algorithm**:

    1. Initialize an empty adjacency list `graph` and a dictionary `in_degree` to store the in-degree of each character.
    2. For each pair of adjacent words `w1` and `w2`:
        - Compare the characters `c1` and `c2` at each position.
        - If `c1 != c2`, add an edge from `c1` to `c2` in `graph` and increment `in_degree[c2]` by 1.
        - Break the loop after finding the first different character.
    3. Initialize a queue with all characters that have an in-degree of `0`.
    4. Process the queue:
        - Pop a character from the queue, append it to `order`.
        - Decrease the in-degree of each neighbor. If a neighbor's in-degree becomes `0`, add it to the queue.
    5. Return `order` joined as a string if it contains all unique characters; otherwise, return an empty string.

```python
def alien_order(words: List[str]) -> str:
    graph = {}
    in_degree = {char: 0 for word in words for char in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_length = min(len(w1), len(w2))
        for j in range(min_length):
            c1, c2 = w1[j], w2[j]
            if c1 != c2:
                if c2 not in graph:
                    graph[c2] = []
                if c1 not in graph:
                    graph[c1] = []
                if c2 not in graph[c1]:
                    graph[c1].append(c2)
                    in_degree[c2] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""

    queue = [char for char in in_degree if in_degree[char] == 0]
    order = []

    while queue:
        char = queue.pop(0)
        order.append(char)
        if char in graph:
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return "".join(order) if len(order) == len(in_degree) else ""
```

---

### Approach 2: Depth-First Search (DFS) with Cycle Detection

-   **Time Complexity**: `O(n)` where `n` is the total number of characters in all words.
-   **Space Complexity**: `O(1)`
-   **Description**: This approach uses a depth-first search (DFS) to determine the topological order of the characters while detecting cycles. Each character is treated as a node in a directed graph, and the adjacency list `adj` represents the edges between nodes (characters). The graph is built by comparing adjacent words, and a DFS is performed on each character to establish the order. During the DFS, a cycle is detected if we revisit a node that is part of the current path, indicating that no valid order exists.

-   **Algorithm**:

    1. Initialize an adjacency list `adj` using a dictionary where each character is mapped to a set of characters it precedes.
    2. Construct the graph:
        - Iterate through each pair of adjacent words `w1` and `w2`.
        - Compare characters at each position up to the length of the shorter word.
        - If the prefix of `w1` matches `w2` but `w1` is longer, return an empty string, as this indicates an invalid order.
        - If a mismatch is found between characters `w1[j]` and `w2[j]`, add an edge from `w1[j]` to `w2[j]` in `adj`, and break out of the loop.
    3. Initialize a `visited` dictionary to track the state of each character:
        - `false` if the character has been fully processed.
        - `true` if the character is currently in the DFS path.
    4. Define a recursive DFS function:
        - If the character is already in `visited` and part of the current path (`true`), a cycle is detected, so return `true`.
        - Mark the character as part of the current path.
        - Recursively visit all adjacent characters. If a cycle is found, return `true`.
        - After processing all neighbors, mark the character as fully visited (`false`), and add it to the result list.
    5. Perform DFS on each character in the adjacency list. If a cycle is detected, return an empty string.
    6. Reverse the result list, as characters are added in reverse order during DFS, and return the joined string.

```python
def alien_order(words: List[str]) -> str:
    # Initialize the adjacency list
    adj = {char: set() for word in words for char in word}

    # Build the graph
    for i from 0 to len(words) - 1:
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for j from 0 to minLen:
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    # Initialize visited dictionary and result list
    visited = {}  # {char: bool} false visited, true current path
    res = []

    # Depth-first search function
    def dfs(char):
        if char in visited:
            return visited[char]

        visited[char] = true

        for neigh_char in adj[char]:
            if dfs(neigh_char):
                return true

        visited[char] = false
        res.append(char)

    # Perform DFS for each character in the adjacency list
    for char in adj:
        if dfs(char):
            return ""

    res.reverse()
    return "".join(res)
```
