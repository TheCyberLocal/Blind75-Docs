# Blind75: House Robber

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has. The houses are arranged in a straight line, i.e., the `i`th house is the neighbor of the `(i - 1)`th and `(i + 1)`th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

**Example 1:**

-   **Input**: `nums = [1, 1, 3, 3]`
-   **Output**: `4`
-   **Explanation**: `nums[0] + nums[2] = 1 + 3 = 4`

**Example 2:**

-   **Input**: `nums = [2, 9, 8, 3, 6]`
-   **Output**: `16`
-   **Explanation**: `nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16`

### Constraints

-   `1 <= len(nums) <= 100`
-   `0 <= nums[i] <= 100`

---

### Approach 1: Simple Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(n)`
-   **Description**: This approach uses dynamic programming to determine the maximum money that can be robbed without triggering the alarm. We maintain an array `dp` where `dp[i]` represents the maximum money that can be robbed from the first `i` houses. For each house `i`, we have two choices: either rob the current house and add its value to the maximum amount obtained from `i - 2` houses, or skip the current house and take the maximum amount from `i - 1` houses. The result will be the maximum value in the `dp` array.
-   **Algorithm**:

    1. Define `n` as `len(nums)`.
    2. Create an array `dp` where `dp[i]` represents the maximum money that can be robbed from the first `i` houses.
    3. Initialize `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.
    4. For each house `i` from 2 to `n - 1`, set `dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])`.
    5. Return `dp[n - 1]` as the result.

```python
def robHouses(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
    	dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[n - 1]
```

---

### Approach 2: Optimized Dynamic Programming

-   **Time Complexity**: `O(n)`
-   **Space Complexity**: `O(1)`
-   **Description**: This approach optimizes space by using only two variables to keep track of the maximum amounts that can be robbed up to the previous house and the house before it. Instead of using an array, we update the variables as we iterate through the list, which reduces the space complexity to O(1).
-   **Algorithm**:

    1. Initialize two variables, `p1` and `p2`, to store the maximum money that can be robbed up to the previous house and the house before it, respectively.
    2. Iterate through each house, updating the two variables as needed.
    3. Return `p1` after the loop, which contains the maximum money that can be robbed from all houses.

```pseudo
function robHouses(nums):
    p1 = 0
    p2 = 0
    for num in nums:
        p1, p2 = max(p2 + num, p1), p1
    return p1
```
