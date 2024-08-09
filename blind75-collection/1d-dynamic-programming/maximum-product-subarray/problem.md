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
- **Description**: This approach is an extension of Kadane's algorithm, which is typically used to find the maximum sum subarray. Here, we maintain two variables, `maxProd` and `minProd`, to keep track of the maximum and minimum products up to the current index. This is necessary because a negative number can turn a large positive product into a small one, or a small negative product into a large positive one.
- **Algorithm**:

  1. Initialize `maxProd`, `minProd`, and `res` with the first element of the array.
  2. Iterate through the array starting from the second element.
  3. For each element, calculate the temporary maximum and minimum products by comparing the current number, the product of `maxProd` with the current number, and the product of `minProd` with the current number.
  4. Update `maxProd` and `minProd` accordingly.
  5. Update `res` with the maximum value between `res` and `maxProd`.
  6. Return `res` as the maximum product subarray.

  ```pseudo
  function maxProduct(nums):
    maxProd = nums[0]
    minProd = nums[0]
    res = nums[0]

    for i from 1 to len(nums):
        tmp = max(nums[i], maxProd * nums[i], minProd * nums[i])
        minProd = min(nums[i], maxProd * nums[i], minProd * nums[i])
        maxProd = tmp
        res = max(res, maxProd)

    return res
  ```

---

### Approach 2: Reset on Zero

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: This approach refines the dynamic programming method by focusing on the impact of negative numbers on the product. The main idea is to track both the maximum and minimum products up to each index, as a negative number could turn the smallest product into the largest one. Unlike the first approach, we don't explicitly reset on zeros but rather handle each element based on its value. Specifically, when encountering a negative number, we swap `maxProd` and `minProd` before updating them, since multiplying by a negative number would flip the signs. This ensures that `maxProd` always holds the maximum possible product up to the current element.
- **Algorithm**:

  1. Initialize `res` with the maximum value in the array to account for cases where the array might contain only negative numbers or zeros.
  2. Initialize `maxProd` and `minProd` to 1.
  3. Iterate through each number in `nums`:
     - Calculate a temporary value `tmp` as the product of `maxProd` and the current number.
     - Update `maxProd` to the minimum of `num`, `minProd * num`, and `maxProd * num`. This accounts for the possibility that multiplying by a negative number could yield a higher product.
     - Update `minProd` to the maximum of `num`, `minProd * num`, and `tmp` to ensure that `minProd` correctly tracks the smallest product, which could become the largest when multiplied by another negative number.
     - Update `res` to be the maximum of `res` and `maxProd`.
  4. Return `res`, which contains the maximum product subarray.

```pseudo
function maxProduct(nums):
    res = max(nums)
    maxProd, minProd = 1, 1

    for num in nums:
        tmp = maxProd * num
        maxProd = min(num, minProd * num, maxProd * num)
        minProd = max(num, minProd * num, tmp)
        res = max(res, maxProd)

    return res
```
