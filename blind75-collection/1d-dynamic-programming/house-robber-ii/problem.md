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

### Approach 1: Divide and Conquer using House Robber I
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: We solve the problem by leveraging the solution to House Robber I. Since the first and last houses are adjacent in this problem, we can divide the problem into two scenarios: one where the first house is not robbed and the second where the last house is not robbed. We then take the maximum of these two scenarios as our result.
- **Algorithm**:
  1. If the length of `nums` is 1, return `nums[0]` because there is only one house to rob.
  2. Define a helper function `robber1` that solves House Robber I for a linear array. We'll use the simpler robber1 function for this problem.
  3. Call `robber1` twice: once excluding the last house and once excluding the first house.
  4. Return the maximum of the two results.
```pseudo
function rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    def robber1(nums):
        p1, p2 = 0, 0
        for num in nums:
            p1, p2 = max(p2 + num, p1), p1
        return p1

    case1 = robber1(nums[:n-2])
    case2 = robber1(nums[1:])

    return max(case1, case2)
```

---

### Approach 2: Handling Edge Case for Single House Separately

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
- **Description**: This approach is similar to the first one, but with a slight adjustment to handle the edge case where there is only one house. Instead of immediately returning `nums[0]` when the length of `nums` is 1, we also consider the results from `case1` and `case2`. This ensures that if there is only one house, we take the maximum of the amount in that house and the results from the two scenarios where we consider robbing from a larger subset of houses. This adjustment makes the solution more robust.
- **Algorithm**:
  1. Define a helper function `robber1` that solves House Robber I for a linear array, which returns the maximum money that can be robbed from a non-circular list of houses.
  2. Call `robber1` twice: once excluding the last house and once excluding the first house.
  3. Return the maximum of `nums[0]`, `case1`, and `case2`. This ensures that if there is only one house, its value is compared against the two cases.
```pseudo
function rob(nums):
    def robber1(nums):
        p1, p2 = 0, 0
        for num in nums:
            p1, p2 = max(p2 + num, p1), p1
        return p1

    case1 = robber1(nums[:len(nums)-2])
    case2 = robber1(nums[1:])

    return max(nums[0], case1, case2)
```
