# Blind75: Product of Array Except Self

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

Each product is guaranteed to fit in a 32-bit integer.

**Example 1:**

-   **Input**:
    -   `nums = [1,2,4,6]`
-   **Output**:
    -   `[48,24,12,8]`

**Example 2:**

-   **Input**:
    -   `nums = [-1,0,1,2,3]`
-   **Output**:
    -   `[0,-6,0,0,0]`

### Constraints

-   `2 <= len(nums) <= 1000`
-   `-20 <= nums[i] <= 20`

### Approach 1: Left and Right Product Lists

-   **Time Complexity**:
    -   `O(n)` where `n` is the length of `nums`.
-   **Space Complexity**:
    -   `O(n)` for the `left` and `right` product arrays.
-   **Description**: We can solve this problem by computing two arrays: `left` and `right`. The `left[i]` array contains the product of all elements to the left of `nums[i]`, and `right[i]` contains the product of all elements to the right of `nums[i]`. The final `output[i]` is simply `left[i] * right[i]`.
-   **Algorithm**:

    1. Initialize two arrays `left` and `right`, both of the same length as `nums`.
    2. Populate the `left` array such that `left[i]` contains the product of all elements before `i`.
    3. Populate the `right` array such that `right[i]` contains the product of all elements after `i`.
    4. For each index `i`, compute `output[i]` as the product of `left[i]` and `right[i]`.
    5. Return the `output` array.

```pseudo
function productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n

    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    for i in range(n):
        output[i] = left[i] * right[i]

    return output
```

### Approach 2: Optimized Space Approach

-   **Time Complexity**:
    -   `O(n)` where `n` is the length of `nums`.
-   **Space Complexity**:
    -   `O(1)` excluding the output array.
-   **Description**: We can optimize the space complexity by storing the result directly in the output array, first by filling it with the left products and then multiplying it by the right products.
-   **Algorithm**:

    1. Initialize an array `output` where `output[i]` contains the product of all elements before `i`.
    2. Traverse the array from left to right, updating the `output` array with the left products.
    3. Traverse the array from right to left, updating the `output` array with the right products.
    4. Return the `output` array.

```pseudo
function productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    leftProduct = 1
    for i in range(n):
        output[i] = leftProduct
        leftProduct *= nums[i]

    rightProduct = 1
    for i in range(n-1, -1, -1):
        output[i] *= rightProduct
        rightProduct *= nums[i]

    return output
```
