# Blind75: Design Word Search Data Structure

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Design a data structure that supports adding new words and searching for existing words.

Implement the `WordDictionary` class with the following methods:

-   `void addWord(word)`: Adds a `word` to the data structure.
-   `bool search(word)`: Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. The `word` may contain dots `.` where dots can be matched with any letter.

**Example 1:**

-   **Input:**
    `["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]`
-   **Output:**
    `[null, null, null, null, false, true, true, true]`

-   **Explanation:**
    ```
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("day");
    wordDictionary.addWord("bay");
    wordDictionary.addWord("may");
    wordDictionary.search("say"); // return false
    wordDictionary.search("day"); // return true
    wordDictionary.search(".ay"); // return true
    wordDictionary.search("b.."); // return true
    ```

### Constraints

-   `1 <= word.length <= 20`
-   `word` in `addWord` consists of lowercase English letters.
-   `word` in `search` consists of `.` or lowercase English letters.

---

### Approach 1: Trie Data Structure with Recursive Search

-   **Time Complexity:**
    -   `addWord`: `O(m)`, where `m` is the length of the word.
    -   `search`: Worst case `O(m * 26^m)`, where `m` is the length of the word.
-   **Space Complexity:**
    -   `O(n * m)`, where `n` is the number of words added and `m` is the average length of words.
-   **Description:**
    This approach uses a Trie (prefix tree) data structure to store the words. Each node in the Trie represents a character in the words. The search operation can handle both exact matches and pattern matches with the `.` wildcard by recursively checking all possible paths in the Trie.
-   **Algorithm:**

    1. **addWord:**
        1. Initialize a pointer at the root of the Trie.
        2. For each character in the word, if a node for that character does not exist, create a new node.
        3. Move the pointer to the corresponding child node.
        4. After adding all characters, mark the last node as the end of a word.

    2. **search:**
        1. Define a recursive function that takes a node and the current index in the word.
        2. For each character in the word:
            1. If the character is `.` check all child nodes recursively.
            2. If the character is a letter, move to the corresponding child node.
        3. If all characters are matched, check if the last node marks the end of a word.
        4. Return `true` if a valid word is found, otherwise `false`.

```pseudo
class WordDictionary:
    function constructor():
        self.trie = {}

    function addWord(word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = true

    function search(word):
        function dfs(node, i):
            if i == len(word):
                return '#' in node

            if word[i] == '.':
                for child in node:
                    if child != '#' and dfs(node[child], i + 1):
                        return true
            else if word[i] in node:
                return dfs(node[word[i]], i + 1)
            return false

        return dfs(self.trie, 0)
```
