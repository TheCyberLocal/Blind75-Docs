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

- `1 <= nums.length <= 1000`
- `-10 <= nums[i] <= 10`

---

### Approach 1: Dynamic Programming (Kadane's Algorithm Variant)

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: This approach is an extension of Kadane's algorithm, which is typically used to find the maximum sum subarray. Here, we maintain two variables, `max_product` and `min_product`, to keep track of the maximum and minimum products up to the current index. This is necessary because a negative number can turn a large positive product into a small one, or a small negative product into a large positive one.
- **Algorithm**:

  1. Initialize `max_product`, `min_product`, and `result` with the first element of the array.
  2. Iterate through the array starting from the second element.
  3. For each element, calculate the temporary maximum and minimum products by comparing the current number, the product of `max_product` with the current number, and the product of `min_product` with the current number.
  4. Update `max_product` and `min_product` accordingly.
  5. Update `result` with the maximum value between `result` and `max_product`.
  6. Return `result` as the maximum product subarray.

  ```pseudo
  function maxProduct(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i from 1 to len(nums):
        temp_max = max(nums[i], max_product * nums[i], min_product * nums[i])
        min_product = min(nums[i], max_product * nums[i], min_product * nums[i])
        max_product = temp_max
        result = max(result, max_product)

    return result
  ```
