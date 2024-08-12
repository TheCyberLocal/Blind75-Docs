# Blind75: Longest Consecutive Sequence

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly `1` greater than the previous element.

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

-   **Input**:
    -   `nums = [2,20,4,10,3,4,5]`
-   **Output**:
    -   `4`
-   **Explanation**: The longest consecutive sequence is `[2, 3, 4, 5]`.

**Example 2:**

-   **Input**:
    -   `nums = [0,3,2,5,4,6,1,1]`
-   **Output**:
    -   `7`

### Constraints

-   `0 <= len(nums) <= 1000`
-   `-10^9 <= nums[i] <= 10^9`

---

### Approach 1: Hash Set with Linear Scan

-   **Time Complexity**:
    -   `O(n)` where `n` is the length of `nums`.
-   **Space Complexity**:
    -   `O(n)` for the hash set.
-   **Description**: We can solve this problem efficiently by using a hash set. The key observation is that a number is the start of a sequence if the previous number is not in the set. By iterating through each number and counting the length of the sequence starting from that number, we can find the longest consecutive sequence.
-   **Algorithm**:

    1. Convert the array `nums` into a set `numSet` for `O(1)` lookups.
    2. Initialize `longestStreak` to 0.
    3. For each number in `nums`, if it's the start of a sequence (i.e., `num - 1` is not in `numSet`), find the length of the consecutive sequence starting from that number.
    4. Update `longestStreak` if the current sequence is longer.
    5. Return `longestStreak`.

```pseudo
function longestConsecutive(nums):
    if not nums:
        return 0

    numSet = set(nums)
    longestStreak = 0

    for num in nums:
        if num - 1 not in numSet:
            currentNum = num
            currentStreak = 1

            while currentNum + 1 in numSet:
                currentNum += 1
                currentStreak += 1

            longestStreak = max(longestStreak, currentStreak)

    return longestStreak
```
