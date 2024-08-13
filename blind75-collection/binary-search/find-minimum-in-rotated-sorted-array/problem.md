# Blind75: Find Minimum in Rotated Sorted Array

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an array of length `n` that was originally sorted in ascending order. It has now been rotated between 1 and `n` times. For example, the array `nums = [1,2,3,4,5,6]` might become:

-   `[3,4,5,6,1,2]` if it was rotated 4 times.
-   `[1,2,3,4,5,6]` if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array `nums` are unique, return the minimum element of this array.

A solution that runs in `O(n)` time is trivial. Can you write an algorithm that runs in `O(log n)` time?

**Example 1:**

-   **Input**: `nums = [3,4,5,6,1,2]`
-   **Output**: `1`

**Example 2:**

-   **Input**: `nums = [4,5,0,1,2,3]`
-   **Output**: `0`

**Example 3:**

-   **Input**: `nums = [4,5,6,7]`
-   **Output**: `4`

### Constraints

-   `1 <= len(nums) <= 1000`
-   `-1000 <= nums[i] <= 1000`

### Approach 1: Binary Search

-   **Time Complexity**: `O(log n)` where `n` is the number of elements in the array.
-   **Space Complexity**: `O(1)` as no additional space is required.
-   **Description**: Use binary search by comparing the middle element with the last element, decide whether the minimum is in the left or right half of the array. This is possible since we can derive that given any two indices of the array, if the left index is greater than the right, the pivot is between them; otherwise, it is not. If the pivot is between them, we know we are in a fully sorted segment, so return the leftmost index.
-   **Algorithm**:

    1.  Initialize `left` to `0` and `right` to `len(nums) - 1`.
    2.  While `left` is less than `right`:
        -   Calculate the middle index `mid = floor((left + right) / 2)`.
        -   If `nums[mid]` is greater than `nums[right]`, the minimum is in the right half, so set `left = mid + 1`.
        -   Otherwise, the minimum is in the left half, so set `right = mid`.
    3.  Return `nums[left]`, as it will point to the minimum element.

```pseudo
function findMin(nums):
	left, right = 0, len(nums) - 1

	while left < right:
		mid = floor((left + right) / 2)
		if nums[mid] > nums[right]:
			left = mid + 1
		else:
			right = mid

	return nums[left]
```
