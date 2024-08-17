# Blind75: Word Search II

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a 2-D grid of characters `board` and a list of strings `words`, return all words that are present in the grid.

For a word to be present, it must be possible to form the word with a path in the board using horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

**Example 1:**

-   **Input:**
    ```plaintext
    board = [
      ["a","b","c","d"],
      ["s","a","a","t"],
      ["a","c","k","e"],
      ["a","c","d","n"]
    ],
    words = ["bat","cat","back","backend","stack"]
    ```
-   **Output:** `["cat","back","backend"]`

**Example 2:**

-   **Input:**
    ```plaintext
    board = [
      ["x","o"],
      ["x","o"]
    ],
    words = ["xoxo"]
    ```
-   **Output:** `[]`

### Constraints

-   `1 <= len(board), len(board[i]) <= 10`
-   `board[i]` consists only of lowercase English letters.
-   `1 <= len(words) <= 100`
-   `1 <= len(words[i]) <= 10`
-   `words[i]` consists only of lowercase English letters.
-   All strings within `words` are distinct.

---

### Approach 1: Trie + Backtracking

-   **Time Complexity:**
    The time complexity is `O(m * n * l)`, where `m` and `n` are the dimensions of the board, and `l` is the total number of letters in all words.
-   **Space Complexity:**
    The space complexity is `O(n * l)`, where `n` is the number of words and `l` is the length of the longest word.
-   **Description:**
    The problem is tackled by combining a Trie data structure with backtracking. The Trie helps in efficiently searching for word prefixes, while backtracking explores the grid to find all valid paths that form words.

-   **Algorithm:**
    1. **Build the Trie:**
        - Insert all words into the Trie. Each node in the Trie represents a letter, and a path from the root to a node spells out a word.
    2. **Backtracking on the Grid:**
        - For each cell in the grid, start a DFS search:
            1. If the character matches a Trie node, move to that node.
            2. Explore all four directions (up, down, left, right) recursively.
            3. If a word is found (i.e., if the Trie node represents the end of a word), add it to the result set.
            4. Mark the cell as visited and backtrack to explore other paths.
        - Return the set of all found words.

```pseudo
class TrieNode:
    function constructor():
        self.children = {}
        self.isEndOfWord = False

class Trie:
    function constructor():
        self.root = TrieNode()

    function insert(word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    function search(word):
        node = self.root
        for char in word:
            if char not in node.children:
                return false
            node = node.children[char]
        return node.isEndOfWord

    function startsWith(prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return false
            node = node.children[char]
        return true

function findWords(board, words):
    function backtrack(node, i, j, path):
        if node.isEndOfWord:
            result.add(path)
            node.isEndOfWord = False  # Avoid duplicate entries

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        temp = board[i][j]
        if temp not in node.children:
            return

        board[i][j] = '#'  # Mark visited
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + x, j + y
            backtrack(node.children[temp], ni, nj, path + temp)
        board[i][j] = temp  # Reset visited mark

    trie = Trie()
    for word in words:
        trie.insert(word)

    result = set()
    for i from 0 to len(board) - 1:
        for j from 0 to len(board[0]) - 1:
            backtrack(trie.root, i, j, "")

    return list(result)
```
