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
-   **Description**: This approach minimizes space complexity by directly storing the result in the `output` array. It first calculates the left products by traversing the array from left to right and stores them in `output`. Then, a right-to-left traversal updates the values in `output` by multiplying them with the right products. This ensures that each element in `output[i]` is the product of all elements in the array except `nums[i]`, without needing additional arrays to store intermediate results.
-   **Algorithm**:

    1. Initialize an array `output` of size `n` with all elements set to `1`.
    2. Initialize a variable `left_product` to `1`.
    3. Traverse the array from left to right:
        - For each index `i` from `0` to `n - 1`, set `output[i]` to `left_product` and then update `left_product` by multiplying it with `nums[i]`.
    4. Initialize a variable `right_product` to `1`.
    5. Traverse the array from right to left:
        - For each index `i` from `n - 1` to `0`, multiply `output[i]` by `right_product` and then update `right_product` by multiplying it with `nums[i]`.
    6. Return the `output` array.

```python
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * n

    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output
```
