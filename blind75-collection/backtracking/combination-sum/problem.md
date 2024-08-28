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

---

### Approach 1: Optimized with Dynamic Programming

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

```python
def comb_sum(nums: List[int], target: int) -> List[List[int]]:
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])

    for num in nums:
        for i in range(num, target + 1):
            for comb in dp[i - num]:
                dp[i].append(comb + [num])

    return dp[target]
```
