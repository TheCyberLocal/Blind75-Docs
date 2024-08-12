# Blind75: Two Sum

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.

Return the answer with the smaller index first.

**Example 1:**

-   **Input**:
    -   `nums = [3,4,5,6]`
    -   `target = 7`
-   **Output**: `[0,1]`
-   **Explanation**: `nums[0] + nums[1] == 7`, so we return `[0, 1]`.

**Example 2:**

-   **Input**:
    -   `nums = [4,5,6]`
    -   `target = 10`
-   **Output**: `[0,2]`

**Example 3:**

-   **Input**:
    -   `nums = [5,5]`
    -   `target = 10`
-   **Output**: `[0,1]`

### Constraints

-   `2 <= len(nums) <= 1000`
-   `-10^7 <= nums[i] <= 10^7`
-   `-10^7 <= target <= 10^7`

---

### Approach 1: Hash Map Complements

-   **Time Complexity**: `O(n)` where `n` is the number of elements in the array.
-   **Space Complexity**: `O(n)` for storing the elements and their indices in a hash map.
-   **Description**: We traverse the array and use a hash map to store the difference between the `target` and each element (`target - nums[i]`) along with the corresponding index. As we continue traversing, if we find an element that is in the hash map, it means we've found the two numbers that sum to the target.
-   **Algorithm**:

    1. Initialize an empty hash map `compMap`.
    2. Iterate through the array `nums` with index `i`:
        - Calculate the complement `comp = target - nums[i]`.
        - If `comp` is in `compMap`, return `[compMap[comp], i]`.
        - Otherwise, store the index of `nums[i]` in `compMap`.
    3. The function will return the pair `[i, j]` as soon as it finds the correct indices.

```pseudo
function twoSum(nums, target):
    compMap = {}
    for i from 0 to len(nums) - 1:
        comp = target - nums[i]
        if comp in compMap:
            return [compMap[comp], i]
        compMap[nums[i]] = i
```

---

### Approach 2: Exhaustive Pairwise Check

-   **Time Complexity**: `O(n^2)` where `n` is the number of elements in the array.
-   **Space Complexity**: `O(1)` as no additional space is required.
-   **Description**: This approach involves iterating through each element in the array and then iterating through all other elements to check if their sum equals the target. The brute force method systematically checks every possible pair of elements until it finds the two that sum to the target. While not the most efficient in terms of time, it has the advantage of not requiring extra space.
-   **Algorithm**:

    1. Iterate through the array `nums` with index `i`.
    2. For each `i`, iterate through the array again with index `j` starting from `i + 1` to avoid pairing an element with itself and to ensure the smaller index comes first.
    3. If the sum of `nums[i]` and `nums[j]` equals the `target`, return the indices `[i, j]`.
    4. Since the problem guarantees that there is exactly one solution, the function will return as soon as the correct pair is found.

```pseudo
function twoSum(nums, target):
    for i from 0 to len(nums) - 2:
        for j from i + 1 to len(nums) - 1:
            if nums[i] + nums[j] == target:
                return [i, j]
```
