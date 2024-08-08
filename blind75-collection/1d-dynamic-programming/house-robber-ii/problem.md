# Blind75: House Robber II

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has. The houses are arranged in a circle, meaning the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

**Example 1:**

- **Input**: `nums = [3,4,3]`
- **Output**: `4`
- **Explanation**: You cannot rob `nums[0] + nums[2] = 6` because `nums[0]` and `nums[2]` are adjacent houses. The maximum you can rob is `nums[1] = 4`.

**Example 2:**

- **Input**: `nums = [2,9,8,3,6]`
- **Output**: `15`
- **Explanation**: You cannot rob `nums[0] + nums[2] + nums[4] = 16` because `nums[0]` and `nums[4]` are adjacent houses. The maximum you can rob is `nums[1] + nums[4] = 15`.

### Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

---

### Approach 1: Dynamic Programming with Two Passes

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: The problem is a variation of the House Robber problem where houses are arranged in a circle. The key insight is to split the problem into two scenarios: one where you consider robbing houses from index `0` to `n-2` (ignoring the last house) and the other from index `1` to `n-1` (ignoring the first house). The maximum value from these two scenarios will be the answer.
- **Algorithm**:

  1. Define a helper function `rob_linear` to calculate the maximum amount for a linear arrangement of houses.
  2. Compute the maximum value between robbing from `nums[0]` to `nums[n-2]` and robbing from `nums[1]` to `nums[n-1]`.
  3. Return the maximum of these two results.

  ```pseudo
  function rob(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums, 0, len(nums) - 2), rob_linear(nums, 1, len(nums) - 1))

  function rob_linear(nums, start, end):
    prev2 = 0
    prev1 = 0
    for i from start to end:
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    return prev1
  ```
