# Blind75: Reverse Bits

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a 32-bit unsigned integer `n`, reverse the bits of the binary representation of `n` and return the result.

**Example 1:**

-   **Input**: `n = 00000000000000000000000000010101`
-   **Output**: `2818572288 (10101000000000000000000000000000)`
-   **Explanation**: Reversing `00000000000000000000000000010101`, which represents the unsigned integer `21`, gives us `10101000000000000000000000000000`, which represents the unsigned integer `2818572288`.

### Constraints

-   `0 <= n <= 2^32 - 1`

### Approach 1: Bit Manipulation

-   **Time Complexity**: `O(1)` because the loop iterates exactly 32 times (constant number of bits).
-   **Space Complexity**: `O(1)` as no extra space proportional to input size is used.
-   **Description**: Reverse the bits of `n` by iterating over each bit from the least significant to the most significant and constructing the reversed number by shifting and setting bits accordingly.
-   **Algorithm**:

    1.  Initialize `result = 0`.
    2.  For `i` from `0` to `31`:
        -   Left shift `result` by `1`.
        -   Add the least significant bit of `n` to `result`.
        -   Right shift `n` by `1`.
    3.  Return `result`.

```pseudo
function reverseBits(n):
	result = 0
	for i = 0 to 31:
		result = result << 1
		result = result | (n & 1)
		n = n >> 1
	return result
```
