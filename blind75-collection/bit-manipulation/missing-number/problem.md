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

---

### Approach 1: Summation Formula

-   **Time Complexity**: `O(n)` where `n` is the length of the array.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: Calculate the expected sum of the range `[0, n]` using the formula `n * (n + 1) / 2` and subtract the sum of the array `nums`. The difference will be the missing number.
-   **Algorithm**:

    1.  Calculate `n` as `len(nums)`.
    2.  Compute the expected sum as `expected_sum = n * (n + 1) // 2`.
    3.  Compute the actual sum of elements in `nums`.
    4.  The missing number is `expected_sum - actual_sum`.
    5.  Return the missing number.

```python
def find_missing(nums: List[int]) -> int:
	n = len(nums)
	expected_sum = n * (n + 1) // 2
	actual_sum = sum(nums)
	return expected_sum - actual_sum
```

---

### Approach 2: XOR

-   **Time Complexity**: `O(n)` where `n` is the length of the array.
-   **Space Complexity**: `O(1)` for constant space usage.
-   **Description**: XOR all the indices and the elements in `nums`. The result will be the missing number because XORing a number with itself cancels out the number, leaving the missing number as the result.
-   **Algorithm**:

    1.  Initialize `xor_sum` as `0`.
    2.  Iterate over the range `[0, n]` and for each index `i`, compute `xor_sum ^= i`.
    3.  Iterate over each element `num` in `nums` and compute `xor_sum ^= num`.
    4.  The missing number is `xor_sum`.
    5.  Return the missing number.

```python
def find_missing(nums: List[int]) -> int:
	n = len(nums)
	xor_sum = 0

	for i from 0 to n:
		xor_sum ^= i

	for num in nums:
		xor_sum ^= num

	return xor_sum
```

---

### Approach 3: Counting with XOR and Summation

-   **Time Complexity**: `O(n)` where `n` is the number of elements in the array.
-   **Space Complexity**: `O(1)` since only a few variables are used.
-   **Description**: This approach calculates the missing number in a series by using the sum formula for the first `n` natural numbers and comparing it with the sum of the array's elements. The difference gives the missing number.
-   **Algorithm**:

    1. Initialize a variable `res` to `len(nums)`.
    2. Iterate over the array:
        - For each index `i`, update `res` as `res += i - nums[i]`.
    3. Return `res` which will hold the missing number after the loop.

```python
def find_missing(nums: List[int]) -> int:
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]

    return res
```
