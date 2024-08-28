# Blind75: Word Search

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a 2-D grid of characters `board` and a string `word`, return `True` if the word is present in the grid; otherwise, return `False`.

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
-   **Output**: `True`
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
-   **Output**: `False`

### Constraints

-   `1 <= len(board), len(board[i]) <= 5`
-   `1 <= len(word) <= 10`
-   `board` and `word` consist only of alphabetical characters.

---

### Approach 1: Backtracking

-   **Time Complexity**: `O(m * n * 4^l)` where `m` and `n` are the dimensions of the board and `l` is the length of the word.
-   **Space Complexity**: `O(l)` for the recursion stack where `l` is the length of the word.
-   **Description**: Use a backtracking approach to explore all possible paths in the grid that could form the `word`. Start from each cell, explore all four directions (up, down, left, right), and backtrack if the current path does not lead to a solution.
-   **Algorithm**:

    1.  Define a helper function `backtrack(row, col, idx)` that:
        -   Returns `True` if all characters in `word` have been matched.
        -   Returns `False` if the current position is out of bounds, or the current character does not match `word[idx]`.
    2.  Mark the current cell as visited by temporarily setting `board[row][col]` to `#`.
    3.  Explore all four directions (up, down, left, right) by recursively calling `backtrack` with the updated position and index.
    4.  Restore the current cell's value after exploring all directions.
    5.  Iterate over every cell in the grid, initiating the backtracking from each cell.
    6.  Return `True` if any path forms the word; otherwise, return `False`.

```python
def exist(board, word):
	def backtrack(row, col, idx):
		if idx == len(word):
			return True

		rowOutOfBounds = row < 0 or row >= rows
		colOutOfBounds = col < 0 or col >= cols
		charMismatch = board[row][col] != word[idx]

		if rowOutOfBounds or colOutOfBounds or charMismatch:
			return False

		tmp = board[row][col]
		board[row][col] = '#'

		for (r, c) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			if backtrack(row + r, col + c, idx + 1):
				return True

		board[row][col] = tmp
		return False

	rows, cols = len(board), len(board[0])

	for row in range(rows):
		for col in range(cols):
			if backtrack(row, col, 0):
				return True

	return False
```

---

### Approach 2: Optimized Dynamic Programming with Bitmasking

-   **Time Complexity**: `O(m * n * l)` where `m` and `n` are the dimensions of the board and `l` is the length of the word.
-   **Space Complexity**: `O(m * n * l)` for the memoization table.
-   **Description**: This approach leverages dynamic programming with memoization and bitmasking to optimize the search process. We use a 3D DP table where `dp[row][col][idx]` represents whether it's possible to match the substring `word[idx:]` starting from position `(row, col)` on the board.

    Bitmasking is used to track visited cells, allowing us to efficiently handle the constraint that each cell can be used only once in forming the word.

-   **Algorithm**:

    1. Initialize a 3D memoization table `dp` with dimensions `(rows, cols, len(word))` set to `None`.
    2. Define a recursive function `dp(row, col, idx, visited)` that:
        - Returns `True` if `idx` is equal to `len(word)` (meaning the entire word has been matched).
        - Returns `False` if the current position is out of bounds, or if the current cell is not equal to `word[idx]`, or if the cell has already been visited.
        - If `dp[row][col][idx]` is not `None`, return the stored result to avoid redundant calculations.
        - Mark the current cell as visited by updating the `visited` bitmask.
        - Recursively explore all four directions (up, down, left, right).
        - Restore the current state and store the result in `dp[row][col][idx]`.
    3. Iterate over every cell in the grid, initiating the DP search from each cell.
    4. Return `True` if any path forms the word; otherwise, return `False`.

```python
def exist(board, word):
	rows, cols = len(board), len(board[0])
	memo = [[[None for _ in range(len(word))] for _ in range(cols)] for _ in range(rows)]
	visited = 0

	def dp(row, col, idx, visited):
		if idx == len(word):
			return True

		rowOutOfBounds = row < 0 or row >= rows
		colOutOfBounds = col < 0 or col >= cols
		charMismatch = board[row][col] != word[idx]

		if rowOutOfBounds or colOutOfBounds or charMismatch:
			return False

		if (1 << (row * cols + col)) & visited:
			return False

		if memo[row][col][idx] != None:
			return memo[row][col][idx]

		visited |= (1 << (row * cols + col))

		for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			if dp(row + dr, col + dc, idx + 1, visited):
				memo[row][col][idx] = True
				return True

		visited &= ~(1 << (row * cols + col))
		memo[row][col][idx] = False
		return False

	for row in range(rows):
		for col in range(cols):
			if dp(row, col, 0, visited):
				return True

	return False
```
