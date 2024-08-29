# Blind75: Search in Rotated Sorted Array

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an array of length `n` that was originally sorted in ascending order. It has now been rotated between 1 and `n` times. For example, the array `nums = [1,2,3,4,5,6]` might become:

-   `[3,4,5,6,1,2]` if it was rotated 4 times.
-   `[1,2,3,4,5,6]` if it was rotated 6 times.

Given the rotated sorted array `nums` and an integer `target`, return the index of `target` within `nums`, or `-1` if it is not present.

You may assume all elements in the sorted rotated array `nums` are unique.

A solution that runs in `O(n)` time is trivial. Can you write an algorithm that runs in `O(log n)` time?

**Example 1:**

-   **Input**: `nums = [3,4,5,6,1,2]`, `target = 1`
-   **Output**: `4`

**Example 2:**

-   **Input**: `nums = [3,5,6,0,1,2]`, `target = 4`
-   **Output**: `-1`

### Constraints

-   `1 <= len(nums) <= 1000`
-   `-1000 <= nums[i] <= 1000`
-   `-1000 <= target <= 1000`

---

### Approach 1: Binary Search

-   **Time Complexity**: `O(log n)` where `n` is the number of elements in the array.
-   **Space Complexity**: `O(1)`
-   **Description**: Utilize binary search by identifying which part of the array (left or right) is sorted. Check if the `target` is within the sorted range; if so, adjust the search to that range, otherwise search in the other half.
-   **Algorithm**:

    1.  Initialize `left` to `0` and `right` to `len(nums) - 1`.
    2.  While `left` is less than or equal to `right`:
        -   Calculate the middle index `mid = (left + right) // 2`.
        -   If `nums[mid]` equals `target`, return `mid`.
        -   If `nums[left]` to `nums[mid]` is sorted:
            -   If `target` is within this range, set `right = mid - 1`.
            -   Otherwise, set `left = mid + 1`.
        -   Otherwise, the `mid` to `right` part is sorted:
            -   If `target` is within this range, set `left = mid + 1`.
            -   Otherwise, set `right = mid - 1`.
    3.  If the loop ends without finding the `target`, return `-1`.

```python
def search(nums: List[int], target: int) -> int:
	left, right = 0, len(nums) - 1

	while left <= right:
		mid = (left + right) // 2

		if nums[mid] == target:
			return mid

		if nums[left] <= nums[mid]:
			if nums[left] <= target < nums[mid]:
				right = mid - 1
			else:
				left = mid + 1
		else:
			if nums[mid] < target <= nums[right]:
				left = mid + 1
			else:
				right = mid - 1

	return -1
```
