# Blind75: Word Search

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a 2-D grid of characters `board` and a string `word`, return `true` if the word is present in the grid; otherwise, return `false`.

For the word to be present, it must be possible to form it with a path in the `board` using horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

**Example 1:**

-   **Input**:
    ```
    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ],
    word = "CAT"
    ```
-   **Output**: `true`
-   **Explanation**: Indicies `[0][2]`, `[1][2]`, and `[1][3]` form the word `CAT`.

**Example 2:**

-   **Input**:
    ```
    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ],
    word = "BAT"
    ```
-   **Output**: `false`

### Constraints

-   `1 <= len(board), len(board[i]) <= 5`
-   `1 <= len(word) <= 10`
-   `board` and `word` consist of only alphabetical characters.

### Approach 1: Backtracking

-   **Time Complexity**: `O(M * N * 4^L)` where `M` and `N` are the dimensions of the board and `L` is the length of the word.
-   **Space Complexity**: `O(L)` for the recursion stack where `L` is the length of the word.
-   **Description**: Use a backtracking approach to explore all possible paths in the grid that could form the `word`. Start from each cell, explore all four directions (up, down, left, right), and backtrack if the current path does not lead to a solution.
-   **Algorithm**:

    1.  Define a helper function `backtrack(row, col, idx)` that:
        -   Returns `true` if all characters in `word` have been matched.
        -   Returns `false` if the current position is out of bounds, or the current character does not match `word[idx]`.
    2.  Mark the current cell as visited by temporarily setting `board[row][col]` to `#`.
    3.  Explore all four directions (up, down, left, right) by recursively calling `backtrack` with the updated position and index.
    4.  Restore the current cell's value after exploring all directions.
    5.  Iterate over every cell in the grid, initiating the backtracking from each cell.
    6.  Return `true` if any path forms the word; otherwise, return `false`.

```pseudo
function exist(board, word):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if backtrack(row, col, 0):
				return true
	return false

function backtrack(row, col, idx):
	if idx == len(word):
		return true
	if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[idx]:
		return false
	temp = board[row][col]
	board[row][col] = '#'
	for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		if backtrack(row + dr, col + dc, idx + 1):
			return true
	board[row][col] = temp
	return false
```
