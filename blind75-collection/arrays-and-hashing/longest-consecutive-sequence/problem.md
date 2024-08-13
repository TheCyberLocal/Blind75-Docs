# Blind75: Longest Consecutive Sequence

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly `1` greater than the previous element.

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

-   **Input**: `nums = [2,20,4,10,3,4,5]`
-   **Output**: `4`
-   **Explanation**: The longest consecutive sequence is `[2, 3, 4, 5]`.

**Example 2:**

-   **Input**: `nums = [0,3,2,5,4,6,1,1]`
-   **Output**: `7`

### Constraints

-   `0 <= len(nums) <= 1000`
-   `-10^9 <= nums[i] <= 10^9`

---

### Approach 1: Hash Set with Linear Scan

-   **Time Complexity**: `O(n)` where `n` is the length of `nums`.
-   **Space Complexity**: `O(n)` for the hash set.
-   **Description**: This approach utilizes a hash set to allow `O(1)` lookups, which helps efficiently identify the start of each sequence. By iterating through the set and determining the length of each sequence that begins with a number, the algorithm finds the longest consecutive sequence in linear time.
-   **Algorithm**:

    1. Convert the array `nums` into a set `numSet` for `O(1)` lookups.
    2. Initialize `longest` to 0.
    3. Iterate through each number `num` in `numSet`:
        - If `num - 1` is not in `numSet`, it indicates the start of a new sequence.
        - Set `length` to 1.
        - While `num + length` exists in `numSet`, increment `length`.
        - Update `longest` with the maximum of `length` and `longest`.
    4. Return `longest` as the length of the longest consecutive sequence.

```pseudo
function longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if num - 1 not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
```
