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

### Approach 1: Hash Map for Complement Lookup

-   **Time Complexity**: `O(n)` where `n` is the number of elements in the array.
-   **Space Complexity**: `O(n)` for storing the elements and their indices in a hash map.
-   **Description**: We traverse the array and use a hash map to store the difference between the `target` and each element (`target - nums[i]`) along with the corresponding index. As we continue traversing, if we find an element that is in the hash map, it means we've found the two numbers that sum to the target.
-   **Algorithm**:

    1. Initialize an empty hash map `num_to_index`.
    2. Iterate through the array `nums` with index `i`:
        - Calculate the complement `complement = target - nums[i]`.
        - If `complement` is in `num_to_index`, return `[num_to_index[complement], i]`.
        - Otherwise, store the index of `nums[i]` in `num_to_index`.
    3. The function will return the pair `[i, j]` as soon as it finds the correct indices.

```pseudo
function twoSum(nums, target):
    num_to_index = {}
    for i from 0 to len(nums) - 1:
        complement = target - nums[i]
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[nums[i]] = i
```
