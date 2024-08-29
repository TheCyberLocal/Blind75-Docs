# Blind75: Number of One Bits

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an unsigned integer `n`. Return the number of `1` bits in its binary representation. This is also known as the Hamming weight.

You may assume `n` is a non-negative integer which fits within `32-bits`.

**Example 1:**

-   **Input**: `n = 00000000000000000000000000010111`
-   **Output**: `4`

**Example 2:**

-   **Input**: `n = 01111111111111111111111111111101`
-   **Output**: `30`

### Constraints

-   `0 <= n <= 2^32 - 1`

---

### Approach 1: Brian Kernighan's Algorithm

-   **Time Complexity**: `O(1)` because the loop iterates over a constant number of bits.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: Brian Kernighan's Algorithm is an efficient way to count the number of `1` bits in an integer. The key insight is that subtracting `1` from a number flips all the bits after the rightmost `1` bit, including the `1` bit itself. By performing `n = n & (n - 1)`, we effectively remove the rightmost `1` bit from `n`. This process continues until `n` becomes `0`, and the number of iterations is equal to the number of `1` bits in the original number.
-   **Algorithm**:

    1. Initialize a counter `count = 0`.
    2. While `n` is not `0`:
        - Perform `n = n & (n - 1)` to remove the rightmost `1` bit.
        - Increment `count`.
    3. Return `count`.

```python
def hamming_weight(n: int) -> int:
    count = 0

    while n:
        n &= (n - 1)
        count += 1

    return count
```

---

### Approach 2: Bitwise Iteration

-   **Time Complexity**: `O(1)` because the loop iterates over a constant number of bits.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: Count the number of `1` bits by iterating through the binary representation of `n` and checking if the least significant bit is `1`. Shift `n` right by `1` in each iteration.
-   **Algorithm**:

    1.  Initialize a counter `count = 0`.
    2.  While `n` is not `0`:
        -   If the least significant bit of `n` is `1`, increment `count`.
        -   Right shift `n` by `1`.
    3.  Return `count`.

```python
def hamming_weight(n: int) -> int:
	count = 0

	while n:
		if n & 1 == 1:
			count += 1

		n >>= 1

	return count
```
