# Blind75: Sum of Two Integers

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given two integers `a` and `b`, return the sum of the two integers without using the `+` and `-` operators.

**Example 1:**

-   **Input**: `a = 1`, `b = 1`
-   **Output**: `2`

**Example 2:**

-   **Input**: `a = 4`, `b = 7`
-   **Output**: `11`

### Constraints

-   `-1000 <= a, b <= 1000`

### Approach 1: Bit Manipulation

-   **Time Complexity**: `O(1)` because the loop iterates over a constant number of bits.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: Use bitwise operations to simulate the addition of two integers. The key idea is to use the XOR operation to add the bits without considering the carry, and the AND operation followed by a left shift to calculate the carry.
-   **Algorithm**:

    1.  Continue looping until there is no carry:
        -   Calculate the carry as `carry = (a & b) << 1`.
        -   Update `a` to the sum without the carry: `a = a ^ b`.
        -   Update `b` to the carry value.
    2.  Return `a` as the result.

```pseudo
function sumTwoIntegers(a, b):
	while b:
		carry = (a & b) << 1
		a = a ^ b
		b = carry
	return a
```
