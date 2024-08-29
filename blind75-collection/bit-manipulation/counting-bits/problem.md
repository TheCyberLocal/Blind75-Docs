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

---

### Approach 1: Dynamic Programming with Bit Manipulation

-   **Time Complexity**: `O(n)` where `n` is the input number.
-   **Space Complexity**: `O(n)` for the output array.
-   **Description**: Leverage the relationship between numbers to efficiently compute the number of `1`'s in the binary representation. For any number `i`, the count of `1`'s in `i` is the count of `1`'s in `i // 2` plus `i % 2`.
-   **Algorithm**:

    1.  Initialize an array `bits` with length `n + 1` filled with zeros.
    2.  Iterate over the range `1` to `n` inclusive:
        -   For each index `i`, calculate `bits[i] = bits[i >> 1] + (i & 1)`.
    3.  Return `bits`.

```python
def countBits(n: int) -> List[int]:
	bits = [0] * (n + 1)

	for i in range(1, n + 1):
		bits[i] = bits[i >> 1] + (i & 1)

	return bits
```

---

### Approach 2: Dynamic Programming with Offset Tracking

-   **Time Complexity**: `O(n)` where `n` is the input number.
-   **Space Complexity**: `O(n)` for the output array.
-   **Description**: This approach takes advantage of the observation that the number of `1`'s in the binary representation of a number can be derived from a previously computed value with the addition of `1`. The key insight is that numbers can be grouped based on their highest power of two, which is used as an "offset."
-   **Algorithm**:

    1. Initialize an array `dp` with length `n + 1` filled with zeros.
    2. Set an initial `offset` to `1`. This offset represents the current highest power of two within the range of `[0, n]`.
    3. Iterate over the range `1` to `n` inclusive:
        - If `i` reaches twice the current `offset`, update `offset` to `i`.
        - Compute `dp[i]` as `1 + dp[i - offset]`, leveraging the previously computed values.
    4. Return `dp`.

```pseudo
function countBits(n):
    dp = an array of length n + 1 initialized to 0
    offset = 1

    for i from 1 to n:
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp
```
