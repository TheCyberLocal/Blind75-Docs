# Blind75: Counting Bits

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an integer `n`, count the number of `1`'s in the binary representation of every number in the range `[0, n]`.

Return an array `output` where `output[i]` is the number of `1`'s in the binary representation of `i`.

**Example 1:**

-   **Input**: `n = 4`
-   **Output**: `[0,1,1,2,1]`
-   **Explanation**:
    -   `0` --> `0`
    -   `1` --> `1`
    -   `2` --> `10`
    -   `3` --> `11`
    -   `4` --> `100`

### Constraints

-   `0 <= n <= 1000`

### Approach 1: Dynamic Programming with Bit Manipulation

-   **Time Complexity**: `O(n)` where `n` is the input number.
-   **Space Complexity**: `O(n)` for the output array.
-   **Description**: Leverage the relationship between numbers to efficiently compute the number of `1`'s in the binary representation. For any number `i`, the count of `1`'s in `i` is the count of `1`'s in `i // 2` plus `i % 2`.
-   **Algorithm**:

    1.  Initialize an array `output` with length `n + 1` filled with zeros.
    2.  Iterate over the range `1` to `n` inclusive:
        -   For each index `i`, calculate `output[i] = output[i >> 1] + (i & 1)`.
    3.  Return `output`.

```pseudo
function countBits(n):
	output = [0] * (n + 1)

	for i in range(1, n + 1):
		output[i] = output[i >> 1] + (i & 1)

	return output
```
