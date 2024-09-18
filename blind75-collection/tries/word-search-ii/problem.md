# Blind75: Word Search II

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a 2-D grid of characters `board` and a list of strings `words`, return all words that are present in the grid.

For a word to be present, it must be possible to form the word with a path in the board using horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

**Example 1:**

- **Input:**
  ```plaintext
  board = [
    ["a","b","c","d"],
    ["s","a","a","t"],
    ["a","c","k","e"],
    ["a","c","d","n"]
  ],
  words = ["bat","cat","back","backend","stack"]
  ```
- **Output:** `["cat","back","backend"]`

**Example 2:**

- **Input:**
  ```plaintext
  board = [
    ["x","o"],
    ["x","o"]
  ],
  words = ["xoxo"]
  ```
- **Output:** `[]`

### Constraints

- `1 <= len(board), len(board[i]) <= 10`
- `board[i]` consists only of lowercase English letters.
- `1 <= len(words) <= 100`
- `1 <= len(words[i]) <= 10`
- `words[i]` consists only of lowercase English letters.
- All strings within `words` are distinct.

---

### Approach 1: Trie + Backtracking

- **Time Complexity:**
  The time complexity is `O(m * n * l)`, where `m` and `n` are the dimensions of the board, and `l` is the total number of letters in all words.
- **Space Complexity:**
  The space complexity is `O(k * l)`, where `k` is the number of words and `l` is the length of the longest word.
- **Description:**
  The problem is tackled by combining a Trie data structure with backtracking. The Trie helps in efficiently searching for word prefixes, while backtracking explores the grid to find all valid paths that form words.

- **Algorithm:**
  1. **Build the Trie:**
     - Insert all words into the Trie. Each node in the Trie represents a letter, and a path from the root to a node spells out a word.
  2. **Backtracking on the Grid:**
     - For each cell in the grid, start a DFS search:
       1. If the character matches a Trie node, move to that node.
       2. Explore all four directions (up, down, left, right) recursively.
       3. If a word is found (i.e., if the Trie node represents the end of a word), add it to the result set.
       4. Mark the cell as visited and backtrack to explore other paths.
     - Return the set of all found words.

```python
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end_of_word

    def starts_with(self, prefix) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True

def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    def backtrack(node, i, j, path):
        if node.is_end_of_word:
            result.add(path)
            node.is_end_of_word = False  # Avoid duplicate entries

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
    for i in range(board):
        for j in range(board[0]):
            backtrack(trie.root, i, j, "")

    return list(result)
```

---

### Approach 2: Optimized Trie with DFS

- **Time Complexity:** The time complexity is `O(m * n * l)`, where `m` and `n` are the dimensions of the board, and `l` is the total length of all words.
- **Space Complexity:** The space complexity is `O(k * l)`, where `k` is the number of words and `l` is the average length of the words.
- **Description:** This approach uses a Trie to store the given list of words, enabling efficient prefix searching and word lookup. A depth-first search (DFS) is performed on each cell of the board, exploring all possible paths that form valid words. The Trie nodes are augmented with reference counts to manage the removal of words once they are found, preventing redundant searches. As the search progresses, cells are marked as visited to ensure that each cell is only used once per word search. The found words are collected and returned as the result.
- **Algorithm:**
  1. Insert each word into the Trie, where each node in the Trie represents a letter. As each word is added, increment the reference count at each node along the path.
  2. For each cell in the grid:
     1. If the current cell is out of bounds, the character does not exist in the current Trie node's children, or the reference count is less than 1, terminate the current path.
     2. Add the current cell to the visited set to avoid revisiting.
     3. Traverse to the corresponding child node in the Trie and add the character to the current word path.
     4. If a valid word is found (indicated by the `is_word` flag in the Trie node), mark the word as found, remove it from the Trie, and add it to the result set.
     5. Recursively explore all four possible directions (up, down, left, right) from the current cell.
     6. After exploring all possible directions, remove the current cell from the visited set to allow other DFS paths to use it.
  3. After exploring all cells and paths, convert the result set to a list and return it.

```python
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False
        self.refs = 0

    def add_word(self, word) -> None:
        cur = self
        cur.refs += 1

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]
            cur.refs += 1

        cur.is_word = True

    def remove_word(self, word) -> None:
        cur = self
        cur.refs -= 1

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()

    for w in words:
        root.add_word(w)

    rows, cols = len(board), len(board[0])
    res, visit = set(), set()

    def dfs(r, c, node, word):
        if (
            0 > r or r >= len(rows)
            or 0 > c or c >= len(cols)
            or board[r][c] not in node.children
            or node.children[board[r][c]].refs < 1
            or (r, c) in visit
        ):
            return

        visit.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]

        if node.is_word:
            node.is_word = False
            res.add(word)
            root.remove_word(word)

        dfs(r + 1, c, node, word)
        dfs(r - 1, c, node, word)
        dfs(r, c + 1, node, word)
        dfs(r, c - 1, node, word)

        visit.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "")

    return list(res)
```
