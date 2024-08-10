# Blind75: Foreign Dictionary

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

There is a foreign language that uses the Latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

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
-   **Space Complexity**: `O(1)`.
-   **Description**: We treat each character as a node in a directed graph, where an edge from node `u` to node `v` means that character `u` comes before character `v`. We construct this graph by comparing adjacent words in the list. After constructing the graph, we perform a topological sort to determine a valid order of characters.
-   **Algorithm**:

    1. Initialize an adjacency list to represent the graph and a dictionary to store the in-degree of each character.
    2. Compare adjacent words to find the first different character, which gives the ordering between the two characters.
    3. Add the edge between the characters and update the in-degree of the destination character.
    4. Perform topological sorting using Kahn's algorithm:
        - Initialize a queue with all characters having an in-degree of `0`.
        - Process each character in the queue, appending it to the result, and reduce the in-degree of its neighbors.
        - If a neighbor's in-degree becomes `0`, add it to the queue.
    5. If the result contains all unique characters, return it as the valid order; otherwise, return an empty string.

```pseudo
function alienOrder(words):
    graph = empty adjacency list
    in_degree = {char: 0 for char in all unique characters in words}

    for each pair of adjacent words (word1, word2):
        for each character pair (char1, char2):
            if char1 != char2:
                add edge from char1 to char2 in graph
                increase in_degree[char2] by 1
                break

    queue = all characters with in-degree 0
    order = empty string

    while queue is not empty:
        char = queue.pop()
        order += char
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.push(neighbor)

    if length of order == number of unique characters:
        return order
    else:
        return empty string
```
