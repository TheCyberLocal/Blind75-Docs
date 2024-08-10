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
-   **Space Complexity**: `O(1)`
-   **Description**: We treat each character as a node in a directed graph, where an edge from node `u` to node `v` means that character `u` comes before character `v`. We construct this graph by comparing adjacent words in the list. After constructing the graph, we perform a topological sort to determine a valid order of characters.
-   **Algorithm**:

    1. Initialize an empty adjacency list `graph` and a dictionary `in_degree` to store the in-degree of each character.
    2. For each pair of adjacent words `word1` and `word2`:
        - Compare the characters `char1` and `char2` at each position.
        - If `char1 != char2`, add an edge from `char1` to `char2` in `graph` and increment `in_degree[char2]` by 1.
        - Break the loop after finding the first different character.
    3. Initialize a queue with all characters that have an in-degree of `0`.
    4. Process the queue:
        - Pop a character from the queue, append it to `order`.
        - Decrease the in-degree of each neighbor. If a neighbor's in-degree becomes `0`, add it to the queue.
    5. Return `order` if it contains all unique characters; otherwise, return an empty string.

```pseudo
function alienOrder(words):
    graph = {}  # adjacency list
    in_degree = {char: 0 for char in all unique characters in words}

    for i from 0 to len(words) - 1:
        word1, word2 = words[i], words[i + 1]
        for j from 0 to min(len(word1), len(word2)):
            char1, char2 = word1[j], word2[j]
            if char1 != char2:
                if char2 not in graph[char1]:
                    graph[char1].append(char2)
                    in_degree[char2] += 1
                break

    queue = [char for char in in_degree if in_degree[char] == 0]
    order = ""

    while queue:
        char = queue.pop(0)
        order += char
        for neighbor in graph.get(char, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(in_degree) else ""
```
