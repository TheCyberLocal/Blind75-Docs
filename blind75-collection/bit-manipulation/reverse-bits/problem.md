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

---

### Approach 1: Direct Bit Placement

-   **Time Complexity**: `O(1)` because the loop iterates over a constant number of bits.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: Instead of shifting the result bit by bit, this approach directly places each bit from the original position to its reversed position.
-   **Algorithm**:

    1.  Initialize `res = 0`.
    2.  For `i` from `0` to `31` inclusive:
        -   Extract the bit at position `i` from `n`.
        -   Place this bit at position `31 - i` in `res`.
    3.  Return `res`.

```python
def reverse_bits(n: int) -> int:
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res += (bit << (31 - i))

    return res
```

---

### Approach 2: Iterative Bitwise Reversal

-   **Time Complexity**: `O(1)` because the loop iterates over a constant number of bits.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: Reverse the bits of `n` by iterating over each bit from the least significant to the most significant and constructing the reversed number by shifting and setting bits accordingly.
-   **Algorithm**:

    1.  Initialize `res = 0`.
    2.  For `i` from `0` to `31` inclusive:
        -   Left shift `res` by `1`.
        -   Add the least significant bit of `n` to `res`.
        -   Right shift `n` by `1`.
    3.  Return `res`.

```python
def reverse_bits(n: int) -> int:
	res = 0

	for i in range(32):
		res <<= 1
		res |= (n & 1)
		n >>= 1

	return res
```
