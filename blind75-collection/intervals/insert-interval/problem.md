# Blind75: Insert Interval

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represents the start and end time of the ith interval. `intervals` is initially sorted in ascending order by `start_i`.

You are also given another interval `new_interval = [start, end]`.

Insert `new_interval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and also `intervals` still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return `intervals` after adding `new_interval`.

**Note:** Intervals are non-overlapping if they have no common point. For example, `[1,2]` and `[3,4]` are non-overlapping, but `[1,2]` and `[2,3]` are overlapping.

**Example 1:**

-   **Input:** `intervals = [[1,3],[4,6]], new_interval = [2,5]`
-   **Output:** `[[1,6]]`

**Example 2:**

-   **Input:** `intervals = [[1,2],[3,5],[9,10]], new_interval = [6,7]`
-   **Output:** `[[1,2],[3,5],[6,7],[9,10]]`

### Constraints

-   `0 <= len(intervals) <= 1000`
-   `len(new_interval) == len(intervals[i]) == 2`
-   `0 <= start <= end <= 1000`

---

### Approach 1: Merging Intervals

-   **Time Complexity:** `O(n)` where `n` is the number of intervals
-   **Space Complexity:** `O(n)` where `n` is the number of intervals
-   **Description:** The idea is to traverse the intervals, and add all intervals that are completely before the new interval. Then, merge the new interval with any overlapping intervals. Finally, add the remaining intervals.
-   **Algorithm:**

    1. Initialize an empty list `res` to store the merged intervals.
    2. Iterate through each interval in `intervals`:
        - If the current interval ends before `new_interval` starts, add the current interval to `res`.
        - If `new_interval` ends before the current interval starts, add `new_interval` to `res` and update `new_interval` to the current interval.
        - Otherwise, merge `new_interval` with the current interval by updating the start to the minimum of both starts and the end to the maximum of both ends.
    3. After the loop, add the final `new_interval` to `res`.
    4. Return `res`.

```python
def insert_interval(
	intervals: List[List[int]],
	new_interval: List[int]
	) -> List[List[int]]:

	res = []
	for interval in intervals:
		if interval[1] < new_interval[0]:
			res.append(interval)
		elif new_interval[1] < interval[0]:
			res.append(new_interval)
			new_interval = interval
		else:
			new_interval[0] = min(new_interval[0], interval[0])
			new_interval[1] = max(new_interval[1], interval[1])

	res.append(new_interval)
	return res
```
