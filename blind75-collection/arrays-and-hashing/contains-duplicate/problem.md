# Blind75: Contains Duplicate

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

**Example 1:**

-   **Input**: `nums = [1, 2, 3, 3]`
-   **Output**: `true`

**Example 2:**

-   **Input**: `nums = [1, 2, 3, 4]`
-   **Output**: `false`

### Constraints

-   `1 <= len(nums) <= 10^5`
-   `-10^9 <= nums[i] <= 10^9`

---

### Approach 1: Using a Hash Set

-   **Time Complexity**: `O(n)` where `n` is the number of elements in the array.
-   **Space Complexity**: `O(n)` due to the space required for the hash set.
-   **Description**: Iterate through the array while storing each element in a hash set. If an element is already present in the set, return `true`. If the loop completes without finding a duplicate, return `false`.
-   **Algorithm**:

    1. Initialize an empty hash set `seen`.
    2. Iterate over each element `num` in `nums`:
        - If `num` is already in `seen`, return `true`.
        - Otherwise, add `num` to `seen`.
    3. If no duplicates are found by the end of the loop, return `false`.

```pseudo
function containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return true
        seen.add(num)
    return false
```

---

### Approach 2: Sorting the Array

-   **Time Complexity**: `O(n log n)` due to the sorting step.
-   **Space Complexity**: `O(1)` if sorting in place, otherwise `O(n)` if using extra space for the sorted array.
-   **Description**: Sort the array, then check each adjacent pair of elements. If any adjacent elements are equal, return `true`. If the loop completes without finding a duplicate, return `false`.
-   **Algorithm**:

    1. Sort the array `nums`.
    2. Iterate through the array from index `0` to `len(nums) - 2`:
        - If `nums[i] == nums[i + 1]`, return `true`.
    3. If no duplicates are found, return `false`.

```pseudo
function containsDuplicate(nums):
    nums.sort()
    for i from 0 to len(nums) - 2:
        if nums[i] == nums[i + 1]:
            return true
    return false
```
