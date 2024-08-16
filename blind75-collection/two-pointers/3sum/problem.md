# Blind75: 3Sum

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j`, and `k` are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

**Example 1:**

-   **Input:** `nums = [-1,0,1,2,-1,-4]`
-   **Output:** `[[-1,-1,2],[-1,0,1]]`
-   **Explanation:**
    -   `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`
    -   `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`
    -   `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`
    -   The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`.

**Example 2:**

-   **Input:** `nums = [0,1,1]`
-   **Output:** `[]`
-   **Explanation:** The only possible triplet does not sum up to `0`.

**Example 3:**

-   **Input:** `nums = [0,0,0]`
-   **Output:** `[[0,0,0]]`
-   **Explanation:** The only possible triplet sums up to `0`.

### Constraints

-   `3 <= len(nums) <= 1000`
-   `-10^5 <= nums[i] <= 10^5`

---

### Approach 1: Sorting and Two Pointers

-   **Time Complexity:** `O(n^2)`, where `n` is the length of `nums`.
-   **Space Complexity:** `O(1)`, not counting the space used to store the result.
-   **Description:**

    -   First, sort the array `nums`.
    -   Iterate through `nums` from `0 to len(nums) - 2`. For each element `nums[i]`, use two pointers: one starting from `i + 1` and the other from the end of the array.
    -   Move the pointers towards each other to find all valid triplets that sum to `0`.
    -   Skip duplicate elements to avoid adding duplicate triplets to the result.

-   **Algorithm:**

    1. Sort the array `nums`.
    2. Iterate through `nums` from `0 to len(nums) - 2`.
    3. For each `i`, set two pointers: `left` at `i + 1` and `right` at `len(nums) - 1`.
    4. While `left` is less than `right`:
        1. Calculate the sum `currentSum = nums[i] + nums[left] + nums[right]`.
        2. If `currentSum` is `0`, add the triplet to the result, then move both `left` and `right` pointers to skip duplicates.
        3. If `currentSum` is less than `0`, move the `left` pointer to the right to increase the sum.
        4. If `currentSum` is greater than `0`, move the `right` pointer to the left to decrease the sum.
    5. Return the list of triplets.

```pseudo
function threeSum(nums):
	sort(nums)
	result = []
	for i from 0 to len(nums) - 2:
		if i > 0 and nums[i] == nums[i - 1]:
			continue
		left = i + 1
		right = len(nums) - 1
		while left < right:
			currentSum = nums[i] + nums[left] + nums[right]
			if currentSum == 0:
				result.add([nums[i], nums[left], nums[right]])
				while left < right and nums[left] == nums[left + 1]:
					left += 1
				while left < right and nums[right] == nums[right - 1]:
					right -= 1
				left += 1
				right -= 1
			else if currentSum < 0:
				left += 1
			else:
				right -= 1
	return result
```
