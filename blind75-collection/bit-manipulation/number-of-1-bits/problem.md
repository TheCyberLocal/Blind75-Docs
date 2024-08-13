# Blind75: Number of One Bits

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an unsigned integer `n`. Return the number of `1` bits in its binary representation.

You may assume `n` is a non-negative integer which fits within `32-bits`.

**Example 1:**

-   **Input**: `n = 00000000000000000000000000010111`
-   **Output**: `4`

**Example 2:**

-   **Input**: `n = 01111111111111111111111111111101`
-   **Output**: `30`

### Constraints

-   `0 <= n <= 2^32 - 1`

### Approach 1: Bit Manipulation

-   **Time Complexity**: `O(1)` because the loop iterates over a constant number of bits.
-   **Space Complexity**: `O(1)` as no extra space is used.
-   **Description**: Count the number of `1` bits by iterating through the binary representation of `n` and checking if the least significant bit is `1`. Shift `n` right by `1` in each iteration.
-   **Algorithm**:

    1.  Initialize a counter `count = 0`.
    2.  While `n` is not `0`:
        -   If the least significant bit of `n` is `1`, increment `count`.
        -   Right shift `n` by `1`.
    3.  Return `count`.

```pseudo
function hammingWeight(n):
	count = 0
	while n != 0:
		if n & 1 == 1:
			count += 1
		n = n >> 1
	return count
```
