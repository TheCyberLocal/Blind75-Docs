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

---

### Approach 1: Bit Manipulation with Masking

-   **Time Complexity**: `O(1)` because the number of iterations depends on the fixed bit length of the integers, usually 32 or 64 bits.
-   **Space Complexity**: `O(1)` as the solution only uses a constant amount of space.
-   **Description**: This approach uses bitwise operations to compute the sum of two integers without using the `+` or `-` operators. The key idea is to break the addition into two components: the sum without carrying, and the carry itself. The XOR operation (`a ^ b`) calculates the sum of the bits where there is no carry, while the AND operation (`a & b`) followed by a left shift calculates the carry. This process repeats until there are no more carry bits to add.
-   **Algorithm**:

    1. Start by initializing a `mask` with a value of `0xFFFFFFFF` (which represents a 32-bit integer).
    2. In a loop, compute the sum of `a` and `b` using the XOR operation (`a ^ b`). This effectively adds the bits of `a` and `b` where there is no carry.
    3. Compute the carry by using the AND operation (`a & b`) followed by a left shift (`<< 1`). This identifies where the carry occurs and shifts it to the next higher bit.
    4. Update `a` to be the result of the XOR operation and `b` to be the result of the carry calculation.
    5. Repeat the loop until there are no carry bits left (`b == 0`).
    6. Once the loop ends, if `a` is positive, return `a` directly. If `a` is negative (greater than `0x7FFFFFFF`), return the 32-bit two's complement of `a` by XORing `a` with the mask and inverting the result.

```pseudo
function getSum(a, b):
    mask = 0xFFFFFFFF

    while b:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    return a if a <= 0x7FFFFFFF else ~(a ^ mask)
```

---

### Approach 2: Bit Manipulation with Recursion

-   **Time Complexity**: `O(1)` because the loop iterates over a constant number of bits.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: This approach uses a recursive function to simulate the addition of two integers without using the `+` or `-` operators. The core idea is to use the XOR operation to add the bits without considering the carry, and the AND operation followed by a left shift to calculate the carry. The recursion continues until there is no carry left.
-   **Algorithm**:

    1. Define a recursive function `add(a, b)` that:
        - Returns `a` or `b` if one of them is zero (base case).
        - Otherwise, recursively calls itself with `a ^ b` (sum without carry) and `(a & b) << 1` (carry).
    2. Handle cases where `a` and `b` have opposite signs:
        - Swap `a` and `b` if `a` is negative and `b` is positive.
        - Return `0` if `b` is the negation of `a`.
        - If the magnitude of `b` is greater than the magnitude of `a`, return the negation of the recursive sum of the negated values.
    3. Call the `add` function with the original values of `a` and `b`.
    4. Return the final result.

```pseudo
function getSum(a, b):
    function add(a, b):
        if not a or not b:
            return a or b
        return add(a ^ b, (a & b) << 1)

    if a * b < 0:
        if a > 0:
            return getSum(b, a)
        if add(~a, 1) == b:
            return 0
        if add(~a, 1) < b:
            return add(~add(add(~a, 1), add(~b, 1)), 1)

    return add(a, b)
```
