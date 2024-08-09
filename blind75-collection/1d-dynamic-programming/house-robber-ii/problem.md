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

- `1 <= len(nums) <= 100`
- `0 <= nums[i] <= 100`

---

### Approach 1: Simple Dynamic Programming

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
- **Description**: This approach uses dynamic programming to determine the maximum money that can be robbed without triggering the alarm. We maintain an array `dp` where `dp[i]` represents the maximum money that can be robbed from the first `i` houses. For each house `i`, we have two choices: either rob the current house and add its value to the maximum amount obtained from `i-2` houses, or skip the current house and take the maximum amount from `i-1` houses. The result will be the maximum value in the `dp` array.
- **Algorithm**:
  1. Define `n` as the length of `nums`.
  2. Create an array `dp` where `dp[i]` represents the maximum money that can be robbed from the first `i` houses.
  3. Initialize `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.
  4. For each house `i` from 2 to `n-1`, set `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.
  5. Return `dp[n-1]` as the result.

```pseudo
function rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = array of size n initialized to 0
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i from 2 to (n - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[n - 1]
```

---

### Approach 2: Optimized Dynamic Programming

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: This approach optimizes space by using only two variables to keep track of the maximum amounts that can be robbed up to the previous house and the house before it. Instead of using an array, we update the variables as we iterate through the list, which reduces the space complexity to O(1).
- **Algorithm**:
  1. Initialize two variables, `p1` and `p2`, to store the maximum money that can be robbed up to the previous house and the house before it, respectively.
  2. Iterate through each house, updating the two variables as needed.
  3. Return `p1` after the loop, which contains the maximum money that can be robbed from all houses.

```pseudo
function rob(nums):
    p1, p2 = 0, 0
    for num in nums:
        p1, p2 = max(p2 + num, p1), p1
    return p1
```










### Approach 1: Dynamic Programming with Two Passes

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: The problem is a variation of the House Robber problem where houses are arranged in a circle. Where `n` is the length of `nums`, the key insight is to split the problem into two scenarios: one where you consider robbing houses from index `0` to `n-2` (ignoring the last house) and the other from index `1` to `n-1` (ignoring the first house). The maximum value from these two scenarios will be the answer.
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
