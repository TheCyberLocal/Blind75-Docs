# Blind75: Set Matrix Zeroes

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

Given an `m x n` matrix of integers `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must update the matrix **in-place**.

**Example 1:**

-   **Input:**
    ```
    matrix = [
      [0,1],
      [1,1]
    ]
    ```
-   **Output:**
    ```
    [
      [0,0],
      [0,1]
    ]
    ```

**Example 2:**

-   **Input:**
    ```
    matrix = [
      [1,2,3],
      [4,0,5],
      [6,7,8]
    ]
    ```
-   **Output:**
    ```
    [
      [1,0,3],
      [0,0,0],
      [6,0,8]
    ]
    ```

### Constraints

-   `1 <= len(matrix), len(matrix[0]) <= 100`
-   `-2^31 <= matrix[i][j] <= 2^31 - 1`

---

### Approach 1: Optimized In-Place Solution

-   **Time Complexity:** `O(m * n)`, where `m` and `n` are the dimensions of the matrix.
-   **Space Complexity:** `O(1)` for the optimal solution that does not use additional space beyond the input matrix.
-   **Description:** The goal is to set the entire row and column to zero if any element in the matrix is zero, and do so efficiently in-place with `O(1)` additional space. This can be achieved by using the first row and first column as markers. If an element in the matrix is zero, the corresponding element in the first row and first column is set to zero. This helps in tracking which rows and columns should be set to zero later without requiring additional space. After marking, we traverse the matrix and update the elements based on these markers. Finally, we handle the first row and first column separately if they originally contained zeroes.

-   **Algorithm:**
    1. Initialize two flags `firstRowZero` and `firstColZero` to check if the first row and first column originally contain any zeroes.
    2. Traverse the matrix and use the first row and first column as markers. If `matrix[i][j]` is zero, set `matrix[i][0]` and `matrix[0][j]` to zero.
    3. Iterate over the matrix again, using the markers to set the elements to zero if required.
    4. Finally, update the first row and first column based on the `firstRowZero` and `firstColZero` flags.

```pseudo
function setMatrixZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    firstRowZero = False
    firstColZero = False

    for j from 0 to n - 1:
        if matrix[0][j] == 0:
            firstRowZero = True

    for i from 0 to m - 1:
        if matrix[i][0] == 0:
            firstColZero = True

    for i from 1 to m - 1:
        for j from 1 to n - 1:
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i from 1 to m - 1:
        for j from 1 to n - 1:
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if firstRowZero:
        for j from 0 to n - 1:
            matrix[0][j] = 0

    if firstColZero:
        for i from 0 to m - 1:
            matrix[i][0] = 0
```
