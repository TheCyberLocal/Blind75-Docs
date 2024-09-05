# Blind75: Rotate Image

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a square `n x n` matrix of integers `matrix`, rotate it by 90 degrees clockwise.

You must rotate the matrix **in-place**. Do not allocate another 2D matrix and do the rotation.

**Example 1:**

-   **Input:**
    ```
    matrix = [
        [1,2],
        [3,4]
    ]
    ```
-   **Output:**
    ```
    [
        [3,1],
        [4,2]
    ]
    ```

**Example 2:**

-   **Input:**
    ```
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    ```
-   **Output:**
    ```
    [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    ```

### Constraints

-   `n == len(matrix) == len(matrix[i])`
-   `1 <= n <= 20`
-   `-1000 <= matrix[i][j] <= 1000`

---

### Approach 1: Transpose and Reflect

-   **Time Complexity:** `O(n^2)` where `n` is the size of the matrix.
-   **Space Complexity:** `O(1)` since the operation is performed in-place.
-   **Description:** This approach involves two main steps: transposing the matrix and then reflecting it horizontally. Transposing a matrix means swapping its rows and columns, while reflecting it horizontally means flipping it along its vertical axis.
-   **Algorithm:**

    1. Transpose the matrix by iterating over each element above the diagonal (i.e., where `i < j`), and swap `matrix[i][j]` with `matrix[j][i]`.
    2. Reflect the matrix horizontally by iterating over each row, and swapping elements symmetrically (i.e., `matrix[i][j]` with `matrix[i][n - j - 1]`).

```python
def rotate(matrix: List[List[int]]) -> None:
	n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
```
