# Blind75: Maximum Product Subarray

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an integer array `nums`, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

**Example 1:**

- **Input**: `nums = [1,2,-3,4]`
- **Output**: `4`

**Example 2:**

- **Input**: `nums = [-2,-1]`
- **Output**: `2`

### Constraints

- `1 <= len(nums) <= 1000`
- `-10 <= nums[i] <= 10`

---

### Approach 1: Dynamic Programming (Kadane's Algorithm Variant)

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: This approach is an extension of Kadane's algorithm, which is typically used to find the maximum sum subarray. Here, we maintain two variables, `max_prod` and `min_prod`, to keep track of the maximum and minimum products up to the current index. This is necessary because a negative number can turn a large positive product into a small one, or a small negative product into a large positive one.
- **Algorithm**:

  1. Initialize `max_prod`, `min_prod`, and `res` with the first element of the array.
  2. Iterate through the array starting from the second element.
  3. For each element, calculate the temporary maximum and minimum products by comparing the current number, the product of `max_prod` with the current number, and the product of `min_prod` with the current number.
  4. Update `max_prod` and `min_prod` accordingly.
  5. Update `res` with the maximum value between `res` and `max_prod`.
  6. Return `res` as the maximum product subarray.

  ```pseudo
  function maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    res = nums[0]

    for i from 1 to len(nums):
        tmp = max(nums[i], max_prod * nums[i], min_prod * nums[i])
        min_prod = min(nums[i], max_prod * nums[i], min_prod * nums[i])
        max_prod = tmp
        res = max(res, max_prod)

    return res
  ```

### Approach 2: Reset on Zero

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: This approach also maintains `max_prod` and `min_prod` to track the maximum and minimum products at each step. However, it differs from the first approach by handling zeros explicitly. Whenever a zero is encountered, both `max_prod` and `min_prod` are reset to 1, which effectively breaks the current subarray and starts fresh from the next element. This is necessary because multiplying by zero would reset any product to zero, and thus, a new subarray should be considered starting after the zero. The result is updated at each step with the maximum of the current `max_prod` and the previous `res`.
- **Algorithm**:
  1. Initialize `res` with the maximum value in the array to account for the case where all elements are negative or zero.
  2. Initialize `max_prod` and `min_prod` to 1.
  3. Iterate through each number in `nums`:
     - If the current number is `0`, reset `max_prod` and `min_prod` to 1 and continue to the next element since a zero breaks the product subarray.
     - Calculate a temporary value `tmp` as the product of `max_prod` and the current number.
     - Update `max_prod` to the maximum of `num`, `min_prod * num`, and `max_prod * num` to consider both positive and negative products.
     - Update `min_prod` to the minimum of `num`, `min_prod * num`, and `tmp` to ensure we track the smallest product which may become the largest when multiplied by a negative number.
     - Update `res` to be the maximum of `res` and `max_prod`.
  4. Return `res`, which contains the maximum product subarray.

```pseudo
function maxProduct(nums):
    res = max(nums)
    max_prod, min_prod = 1, 1

    for num in nums:
        if num == 0:
            max_prod, min_prod = 1, 1
            continue

        tmp = max_prod * num
        max_prod = min(num, min_prod * num, max_prod * num)
        min_prod = max(num, min_prod * num, tmp)
        res = max(res, max_prod)

    return res
```
