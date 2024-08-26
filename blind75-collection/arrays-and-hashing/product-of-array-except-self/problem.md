# Blind75: Prod of Array Except Self

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

Each product is guaranteed to fit in a 32-bit integer.

**Example 1:**

-   **Input**: `nums = [1,2,4,6]`
-   **Output**: `[48,24,12,8]`

**Example 2:**

-   **Input**: `nums = [-1,0,1,2,3]`
-   **Output**: `[0,-6,0,0,0]`

### Constraints

-   `2 <= len(nums) <= 1000`
-   `-20 <= nums[i] <= 20`

---

### Approach 1: Left and Right Prod Lists

-   **Time Complexity**: `O(n)` where `n` is the length of `nums`.
-   **Space Complexity**: `O(n)` for the `left` and `right` product arrays.
-   **Description**: We can solve this problem by computing two arrays: `left` and `right`. The `left[i]` array contains the product of all elements to the left of `nums[i]`, and `right[i]` contains the product of all elements to the right of `nums[i]`. The final `product[i]` is simply `left[i] * right[i]`.
-   **Algorithm**:

    1. Initialize two arrays `left` and `right`, both of the same length as `nums`.
    2. Populate the `left` array such that `left[i]` contains the product of all elements before `i`.
    3. Populate the `right` array such that `right[i]` contains the product of all elements after `i`.
    4. For each index `i`, compute `product[i]` as the product of `left[i]` and `right[i]`.
    5. Return the `product` array.

```python
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        product[i] = left[i] * right[i]

    return product
```

---

### Approach 2: Optimized Space Approach

-   **Time Complexity**: `O(n)` where `n` is the length of `nums`.
-   **Space Complexity**: `O(1)` excluding the output array.
-   **Description**: This approach minimizes space complexity by using the `product` array to store the result directly. First, it fills the `product` array with the left products as it traverses from left to right. Then, it multiplies these values by the right products during a right-to-left traversal. This ensures that each element in `product[i]` contains the product of all elements in the array except `nums[i]`, without requiring additional arrays for left and right products.

-   **Algorithm**:

    1. Initialize an array `product` of size `n` with all elements set to `1`.
    2. Traverse the array from left to right:
        - For each index `i` from `1` to `n - 1`, update `product[i]` to be the product of `product[i - 1]` and `nums[i - 1]`.
    3. Initialize a variable `product` to `1`.
    4. Traverse the array from right to left:
        - For each index `i` from `n - 1` to `0`, update `product[i]` by multiplying it with `product`, then update `product` by multiplying it with `nums[i]`.
    5. Return the `product` array.

```python
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    product = [1] * n

    for i from 1 to n - 1:
        product[i] = product[i - 1] * nums[i - 1]

    product = 1
    for i from n - 1 to 0:
        product[i] *= product
        product *= nums[i]

    return product
```
