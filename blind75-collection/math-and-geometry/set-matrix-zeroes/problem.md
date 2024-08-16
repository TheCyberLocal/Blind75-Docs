# Blind75: Set Matrix Zeroes

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

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

-   **Time Complexity:** `O(m * n)`, where m and n are the dimensions of the matrix.
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

    firstRowZero = false
    firstColZero = false

    for j from 0 to n - 1:
        if matrix[0][j] == 0:
            firstRowZero = true

    for i from 0 to m - 1:
        if matrix[i][0] == 0:
            firstColZero = true

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

---

### Approach 2: Optimized In-Place Solution Using Markers

-   **Time Complexity:** `O(m * n)`, where `m` and `n` are the dimensions of the matrix.
-   **Space Complexity:** `O(1)` for the optimal solution that does not use additional space beyond the input matrix.
-   **Description:** This approach marks the first row and first column to indicate which rows and columns need to be zeroed. It also handles the first row separately if it contains any zeroes. This allows for an in-place update with no extra space usage.

-   **Algorithm:**
    1. Initialize `n` as the number of rows and `m` as the number of columns in the matrix.
    2. Initialize a boolean `rowZero` to `false` to track if the first row contains any zeroes.
    3. Traverse the matrix:
        - For each zero found at `matrix[r][c]`, set `matrix[0][c]` to zero (to mark the column).
        - If the zero is not in the first row, set `matrix[r][0]` to zero (to mark the row).
        - If the zero is in the first row, set `rowZero` to `true`.
    4. Traverse the matrix again starting from the second row and second column:
        - Set `matrix[r][c]` to zero if either `matrix[0][c]` or `matrix[r][0]` is zero.
    5. If `matrix[0][0]` is zero, set the entire first column to zero.
    6. If `rowZero` is `true`, set the entire first row to zero.

```pseudo
function setMatrixZeroes(matrix):
    n, m = len(matrix), len(matrix[0])
    rowZero = false

    for r from 0 to n - 1:
        for c from 0 to m - 1:
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = true

    for r from 1 to n - 1:
        for c from 1 to m - 1:
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r from 0 to n - 1:
            matrix[r][0] = 0

    if rowZero:
        for c from 0 to m - 1:
            matrix[0][c] = 0
```
