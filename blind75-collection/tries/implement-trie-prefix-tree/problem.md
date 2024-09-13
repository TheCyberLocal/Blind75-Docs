# Blind75: Implement Trie (Prefix Tree)

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the `PrefixTree` class:

- `PrefixTree()`: Initializes the prefix tree object.
- `void insert(String word)`: Inserts the string `word` into the prefix tree.
- `boolean search(String word)`: Returns `True` if the string `word` is in the prefix tree (i.e., was inserted before), and `False` otherwise.
- `boolean starts_with(String prefix)`: Returns `True` if there is a previously inserted string `word` that has the prefix `prefix`, and `False` otherwise.

**Example 1:**

- **Input:**
  `["PrefixTree", "insert", "dog", "search", "dog", "search", "do", "starts_with", "do", "insert", "do", "search", "do"]`
- **Output:**
  `[null, null, True, False, True, null, True]`

- **Explanation:**
  ```
  PrefixTree prefixTree = new PrefixTree();
  prefixTree.insert("dog");
  prefixTree.search("dog");    // return True
  prefixTree.search("do");     // return False
  prefixTree.starts_with("do"); // return True
  prefixTree.insert("do");
  prefixTree.search("do");     // return True
  ```

### Constraints

- `1 <= word.length, prefix.length <= 1000`
- `word` and `prefix` are made up of lowercase English letters.

---

### Approach 1: Trie Implementation

- **Time Complexity:**
  - `insert`: `O(m)`, where `m` is the length of the word.
  - `search`: `O(m)`, where `m` is the length of the word.
  - `starts_with`: `O(m)`, where `m` is the length of the prefix.
- **Space Complexity:**
  - `O(n * m)`, where `n` is the number of words and `m` is the average length of the words.
- **Description:**
  The Trie is a tree-like data structure that stores words by breaking them into characters. Each node in the Trie represents a single character, and each path down the tree represents a word. The `insert` operation adds words to the Trie, the `search` operation checks if a word exists in the Trie, and the `starts_with` operation checks if any word in the Trie starts with a given prefix.
- **Algorithm:**
  1. **insert:**
     1. Start from the root node.
     2. For each character in the word:
        1. If the character does not have a corresponding child node, create a new node.
        2. Move to the next child node.
     3. After processing all characters, mark the last node as the end of a word.
  2. **search:**
     1. Start from the root node.
     2. For each character in the word:
        1. If the character is not found in the current node, return `False`.
        2. Move to the next child node.
     3. After processing all characters, check if the last node is marked as the end of a word. If so, return `True`; otherwise, return `False`.
  3. **starts_with:**
     1. Start from the root node.
     2. For each character in the prefix:
        1. If the character is not found in the current node, return `False`.
        2. Move to the next child node.
     3. If all characters in the prefix are found, return `True`.

```python
class PrefixTree:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie

        for char in word:
            if char not in node:
                node[char] = {}

            node = node[char]

        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.trie

        for char in word:
            if char not in node:
                return False

            node = node[char]

        return '#' in node

    def starts_with(self, prefix: str) -> bool:
        node = self.trie

        for char in prefix:
            if char not in node:
                return False

            node = node[char]

        return True
```
