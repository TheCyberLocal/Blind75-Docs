# Blind75: Combination Sum

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an array of distinct integers `nums` and a target integer `target`. Your task is to return a list of all unique combinations of `nums` where the chosen numbers sum to `target`.

The same number may be chosen from `nums` an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same; otherwise, they are different.

You may return the combinations in any order, and the order of the numbers in each combination can be in any order.

**Example 1:**

-   **Input**: `nums = [2,5,6,9]`, `target = 9`
-   **Output**: `[[2,2,5],[9]]`
-   **Explanation**:
    -   `2 + 2 + 5 = 9`, we use `2` twice, and `5` once.
    -   `9 = 9`, we use `9` once.

**Example 2:**

-   **Input**: `nums = [3,4,5]`, `target = 16`
-   **Output**: `[[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]`

**Example 3:**

-   **Input**: `nums = [3]`, `target = 5`
-   **Output**: `[]`

### Constraints

-   All elements of `nums` are distinct.
-   `1 <= len(nums) <= 20`
-   `2 <= nums[i] <= 30`
-   `2 <= target <= 30`

### Approach 1: Backtracking

-   **Time Complexity**: `O(2^(target / min(nums)))`
-   **Space Complexity**: `O(target / min(nums))` for the recursion stack.
-   **Description**: Recursively explore all possible combinations of `nums` that sum to `target` by either including or excluding each element. Track the current combination and sum, backtracking when necessary.
-   **Algorithm**:

    1. Initialize an empty list `res` to store results.
    2. Define a recursive function `backtrack(remain, comb, start)`:
        - If `remain` is `0`, add a copy of `comb` to `res`.
        - If `remain` is less than `0`, return.
        - Iterate over the elements in `nums` starting from index `start`:
            - Append `nums[i]` to `comb`.
            - Recur with `remain - nums[i]`, the updated `comb`, and the current index `i`.
            - Backtrack by removing the last element added to `comb`.
    3. Start the recursion with `backtrack(target, [], 0)`.
    4. Return `res`.

```pseudo
function combSum(nums, target):
    res = []

    function backtrack(remain, comb, start):
        if remain == 0:
            res.append(list(comb))
            return
        if remain < 0:
            return
        for i in range(start, len(nums)):
            comb.append(nums[i])
            backtrack(remain - nums[i], comb, i)
            comb.pop()

    backtrack(target, [], 0)
    return res
```
