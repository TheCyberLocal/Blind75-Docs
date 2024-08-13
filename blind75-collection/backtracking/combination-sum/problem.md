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

### Approach 1: Recursive Backtracking

-   **Time Complexity**: `O(2^(target / min(n)))` where `n` is the length of `nums` and `target` is the target sum.
-   **Space Complexity**: `O(target / min(n))` for the recursion stack.
-   **Description**: Recursively explore all possible combinations of `nums` that sum to `target` by either including or excluding each element. Track the current combination and sum, backtracking when necessary.
-   **Algorithm**:

    1. Initialize an empty list `res` to store results.
    2. Define a recursive function `dfs(remain, comb, start)`:
        - If `remain` is `0`, add a copy of `comb` to `res`.
        - If `remain` is less than `0`, return.
        - Iterate over the elements in `nums` starting from index `start`:
            - Append `nums[i]` to `comb`.
            - Recur with `remain - nums[i]`, the updated `comb`, and the current index `i`.
            - Backtrack by removing the last element added to `comb`.
    3. Start the recursion with `dfs(target, [], 0)`.
    4. Return `res`.

```pseudo
function combSum(nums, target):
    res = []

    function dfs(remain, comb, start):
        if remain == 0:
            res.append(list(comb))
            return
        if remain < 0:
            return
        for i in range(start, len(nums)):
            comb.append(nums[i])
            dfs(remain - nums[i], comb, i)
            comb.pop()

    dfs(target, [], 0)
    return res
```

---

### Approach 2: Optimized with Dynamic Programming

-   **Time Complexity**: `O(n * target)` where `n` is the length of `nums` and `target` is the target sum.
-   **Space Complexity**: `O(n * target)` for the memoization table.
-   **Description**: This approach leverages dynamic programming to store intermediate results in a memoization table, `dp`, where `dp[i]` holds all combinations that sum to `i`. We iteratively build up the solution for each target sum from `1` to `target`, using previous results to avoid redundant calculations.
-   **Algorithm**:

    1. Initialize a list `dp` of size `target + 1`, where each element is an empty list to store combinations.
    2. Set `dp[0]` to contain an empty list since there's one way to make a sum of `0` (by choosing nothing).
    3. Iterate over each element `num` in `nums`.
        - For each `i` from `num` to `target`:
            - For each combination `comb` in `dp[i - num]`, append `comb + [num]` to `dp[i]`.
    4. The result will be in `dp[target]`, containing all combinations that sum to `target`.

```pseudo
function combSum(nums, target):
    dp = array of size target + 1 initialized to []
    dp[0].append([])

    for num in nums:
        for i from num to target:
            for comb in dp[i - num]:
                dp[i].append(comb + [num])

    return dp[target]
```
