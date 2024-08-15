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
-   **Description**: This approach solves the problem in reverse, starting from the top of the staircase and working downwards. Since you can only reach a step by taking one or two steps, you only need to track the number of ways to get to the previous two steps. Initially, both the top step and the step immediately below it have exactly one way to reach the top. As you move down each step, you update the number of ways to reach the top by summing the counts of the two steps above it. This process continues until you reach the bottom of the staircase, at which point the computed value represents the total number of distinct ways to climb to the top.
-   **Algorithm**:

    1. **Initialize Variables**: Initialize two variables, `p1` and `p2`. These represent the number of ways to reach the current step (`p1`) and the previous step (`p2`). Both are set to `1` because the top two steps each have only one way to reach the top.

    2. **Iterative Calculation**: For each step from the third-to-last step, where `p1` started, down to the bottom:

        - **Update Step Count**: Update `p1` to be the sum of `p1` and `p2`, reflecting the combined number of ways to reach the top from the current and previous steps.

        - **Shift Variables**: Set `p2` to the previous value of `p1` before it was updated, thereby becoming the pointer for the previous step of `p1`.

    3. **Final Output**: Return `p1`, which now holds the total number of ways to climb from the bottom of the staircase to the top.

```pseudo
function climbStairs(n):
    p1 = p2 = 1
    for (n - 2) times:
        p1, p2 = p1 + p2, p1
    return p1
```

---

### Approach 2: Mathematics (Binet's Formula)

-   **Time Complexity**: `O(1)`
-   **Space Complexity**: `O(1)`
-   **Description**: The reasoning behind this approach is that the number of ways to reach any given step is the sum of the ways to reach the two steps directly before it—mirroring the recursive structure of the Fibonacci sequence. In this context, the top step and the one directly below it each have only one way to reach the top, initializing the sequence. By using Binet's Formula, a closed-form expression for the Fibonacci sequence, we can compute the number of ways to climb the stairs in constant time.
-   **Algorithm**:

    1. **Define Mathematical Components**: Use Binet's Formula to calculate the `n`-th Fibonacci number: $`F(n) = \frac{\phi^n - \psi^n}{\sqrt{5}}`$, where `phi` is the golden ratio and `psi` is its conjugate.

    2. **Apply Binet's Formula**: To account for the one-based nature of the problem (where the first step corresponds to $`F(1)`$), calculate $`F(n + 1)`$, as this reflects the number of ways to reach the top of an `n`-step staircase.

    3. **Round and Return**: Return the result, rounded to the nearest integer, thereby giving the total number of distinct ways to reach the top.

```pseudo
function climbStairs(n):
    function fib(n):
        phi = (1 + sqrt(5)) / 2
        psi = (1 - sqrt(5)) / 2
        return round((phi**n - psi**n) / sqrt(5))
    return fib(n + 1)
```
