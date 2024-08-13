# Blind75: Missing Number

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array `nums` containing `n` integers in the range `[0, n]` without any duplicates, return the single number in the range that is missing from `nums`.

**Example 1:**

-   **Input**: `nums = [1,2,3]`
-   **Output**: `0`
-   **Explanation**: Since there are `3` numbers, the range is `[0,3]`. The missing number is `0` since it does not appear in `nums`.

**Example 2:**

-   **Input**: `nums = [0,2]`
-   **Output**: `1`

### Constraints

-   `1 <= len(nums) <= 1000`

### Approach 1: Summation Formula

-   **Time Complexity**: `O(n)` where `n` is the length of the array.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: Calculate the expected sum of the range `[0, n]` using the formula `n * (n + 1) / 2` and subtract the sum of the array `nums`. The difference will be the missing number.
-   **Algorithm**:

    1.  Calculate `n` as `len(nums)`.
    2.  Compute the expected sum as `expectedSum = n * (n + 1) // 2`.
    3.  Compute the actual sum of elements in `nums`.
    4.  The missing number is `expectedSum - actualSum`.
    5.  Return the missing number.

```pseudo
function findMissing(nums):
	n = len(nums)
	expectedSum = n * (n + 1) // 2
	actualSum = sum(nums)
	return expectedSum - actualSum
```

---

### Approach 2: XOR

-   **Time Complexity**: `O(n)` where `n` is the length of the array.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: XOR all the indices and the elements in `nums`. The result will be the missing number because XORing a number with itself cancels out the number, leaving the missing number as the result.
-   **Algorithm**:

    1.  Initialize `xorSum` as `0`.
    2.  Iterate over the range `[0, n]` and for each index `i`, compute `xorSum ^= i`.
    3.  Iterate over each element `num` in `nums` and compute `xorSum ^= num`.
    4.  The missing number is `xorSum`.
    5.  Return the missing number.

```pseudo
function findMissing(nums):
	n = len(nums)
	xorSum = 0

	for i from 0 to n:
		xorSum ^= i

	for num in nums:
		xorSum ^= num

	return xorSum
```
