# Blind75: Climbing Stairs

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer `n` representing the number of steps to reach the top of a staircase. You can climb with either `1` or `2` steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

**Example 1:**

-   **Input**: `n = 2`
-   **Output**: `2`
-   **Explanation**:
    1.  `1 + 1 = 2`
    2.  `2 = 2`

**Example 2:**

-   **Input**: `n = 3`
-   **Output**: `3`
-   **Explanation**:
    1.  `1 + 1 + 1 = 3`
    2.  `1 + 2 = 3`
    3.  `2 + 1 = 3`

### Constraints

-   `1 <= n <= 30`

---

### Approach 1: Optimized Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(1)`
-   **Description**: This approach uses two variables to keep track of the number of ways to reach the current and previous steps. Starting from the top, it calculates the number of ways to reach the top by summing the ways for both the next two steps.
-   **Algorithm**:

    1.  Initialize two variables, `p1` and `p2`, to store the number of ways to reach the current step and the previous step, respectively. Both are initialized to 1.
    2.  Iterate `n - 2` times, updating the two variables at each step:
        -   Update `p1` to the sum of `p1` and `p2`.
        -   Update `p2` to the previous value of `p1`.
    3.  Return `p1`, which contains the number of ways to reach the `n`-th step.

```python
def climbStairs(n: int) -> int:
    p1 = p2 = 1
    for _ in range(n - 1):
        p1, p2 = p1 + p2, p1
    return p1
```

---

### Approach 2: Mathematics (Binet's Formula)

-   **Time Complexity**: `O(1)`
-   **Space Complexity**: `O(1)`
-   **Description**: This approach leverages the fact that the problem of counting the number of ways to reach the top of the staircase is equivalent to finding the `n`-th Fibonacci number. The Fibonacci sequence can be calculated using a closed-form expression known as Binet's Formula. By directly applying this formula, we can compute the number of ways to climb the stairs in constant time.
-   **Algorithm**:

    1. Use Binet's Formula to calculate the `n`-th Fibonacci number: $F(n) = \frac{\phi^n - \psi^n}{\sqrt{5}}$, where `phi` is the golden ratio and `psi` is its conjugate.
    2. The number of distinct ways to climb to the top of the staircase is equivalent to $F(n + 1)$ because the problem is one-based.
    3. Return the result, rounded to the nearest integer.

```python
def climbStairs(n: int) -> int:
    def fib(n: int) -> int:
        sqrt_5 = 5 ** 0.5
        phi = (1 + sqrt_5) / 2
        psi = (1 - sqrt_5) / 2
        return round((phi ** n - psi ** n) / sqrt_5)
    return fib(n + 1)
```
