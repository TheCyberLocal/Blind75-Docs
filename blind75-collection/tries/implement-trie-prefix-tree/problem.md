# Blind75: Implement Trie (Prefix Tree)

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the `PrefixTree` class:

-   `PrefixTree()`: Initializes the prefix tree object.
-   `void insert(String word)`: Inserts the string `word` into the prefix tree.
-   `boolean search(String word)`: Returns `true` if the string `word` is in the prefix tree (i.e., was inserted before), and `false` otherwise.
-   `boolean startsWith(String prefix)`: Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Example 1:**

-   **Input:**
    `["PrefixTree", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]`
-   **Output:**
    `[null, null, true, false, true, null, true]`

-   **Explanation:**
    ```
    PrefixTree prefixTree = new PrefixTree();
    prefixTree.insert("dog");
    prefixTree.search("dog");    // return true
    prefixTree.search("do");     // return false
    prefixTree.startsWith("do"); // return true
    prefixTree.insert("do");
    prefixTree.search("do");     // return true
    ```

### Constraints

-   `1 <= word.length, prefix.length <= 1000`
-   `word` and `prefix` are made up of lowercase English letters.

---

### Approach: Trie Implementation

-   **Time Complexity:**
    -   `insert`: `O(m)`, where `m` is the length of the word.
    -   `search`: `O(m)`, where `m` is the length of the word.
    -   `startsWith`: `O(m)`, where `m` is the length of the prefix.
-   **Space Complexity:**
    -   `O(n * m)`, where `n` is the number of words and `m` is the average length of the words.
-   **Description:**
    The Trie is a tree-like data structure that stores words by breaking them into characters. Each node in the Trie represents a single character, and each path down the tree represents a word. The `insert` operation adds words to the Trie, the `search` operation checks if a word exists in the Trie, and the `startsWith` operation checks if any word in the Trie starts with a given prefix.
-   **Algorithm:**
    1. **insert:**
        1. Start from the root node.
        2. For each character in the word:
            1. If the character does not have a corresponding child node, create a new node.
            2. Move to the next child node.
        3. After processing all characters, mark the last node as the end of a word.
    2. **search:**
        1. Start from the root node.
        2. For each character in the word:
            1. If the character is not found in the current node, return `false`.
            2. Move to the next child node.
        3. After processing all characters, check if the last node is marked as the end of a word. If so, return `true`; otherwise, return `false`.
    3. **startsWith:**
        1. Start from the root node.
        2. For each character in the prefix:
            1. If the character is not found in the current node, return `false`.
            2. Move to the next child node.
        3. If all characters in the prefix are found, return `true`.

```pseudo
class PrefixTree:
    function constructor():
        self.trie = {}

    function insert(word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    function search(word):
        node = self.trie
        for char in word:
            if char not in node:
                return false
            node = node[char]
        return '#' in node

    function startsWith(prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return false
            node = node[char]
        return true
```
