# Blind75: Unique Paths

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

There is an `m x n` grid where you are allowed to move either down or to the right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that can be taken from the top-left corner of the grid `(grid[0][0])` to the bottom-right corner of the grid `(grid[m - 1][n - 1])`.

You may assume the output will fit in a 32-bit integer.

**Example 1:**

- **Input**: `m = 3`, `n = 6`
- **Output**: `21`

**Example 2:**

- **Input**: `m = 3`, `n = 3`
- **Output**: `6`

### Constraints

- `1 <= m, n <= 100`

---

### Approach 1: Dynamic Programming

- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`
- **Description**: This approach uses dynamic programming to solve the problem. We create a 2D array `dp` where `dp[i][j]` represents the number of unique paths to reach cell `(i, j)` from the top-left corner. The value in each cell is the sum of the value from the cell directly above it and the cell directly to the left of it, as those are the only two directions you can come from. The base case is that the first row and the first column have only one way to reach each cell (all right or all down).
- **Algorithm**:

  1. Initialize a 2D array `dp` of size `m x n` with all values set to `1`. The first row and the first column are filled with `1` because there is only one way to reach those cells.
  2. Iterate over the array starting from `dp[1][1]`.
  3. For each cell `dp[i][j]`, calculate the value as `dp[i-1][j] + dp[i][j-1]`.
  4. Return `dp[m-1][n-1]` as the result, which represents the number of unique paths to the bottom-right corner.

  ```pseudo
  function uniquePaths(m, n):
      dp = 2D array of size m x n initialized to 1

      for i from 1 to m-1:
          for j from 1 to n-1:
              dp[i][j] = dp[i-1][j] + dp[i][j-1]

      return dp[m-1][n-1]
  ```
