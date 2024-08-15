# Blind75: Insert Interval

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represents the start and end time of the ith interval. `intervals` is initially sorted in ascending order by `start_i`.

You are also given another interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and also `intervals` still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return `intervals` after adding `newInterval`.

**Note:** Intervals are non-overlapping if they have no common point. For example, `[1,2]` and `[3,4]` are non-overlapping, but `[1,2]` and `[2,3]` are overlapping.

**Example 1:**

-   **Input:** `intervals = [[1,3],[4,6]], newInterval = [2,5]`
-   **Output:** `[[1,6]]`

**Example 2:**

-   **Input:** `intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]`
-   **Output:** `[[1,2],[3,5],[6,7],[9,10]]`

### Constraints

-   `0 <= len(intervals) <= 1000`
-   `len(newInterval) == len(intervals[i]) == 2`
-   `0 <= start <= end <= 1000`

---

### Approach 1: Merging Intervals

-   **Time Complexity:** `O(n)` where `n` is the number of intervals
-   **Space Complexity:** `O(n)` where `n` is the number of intervals
-   **Description:** The idea is to traverse the intervals, and add all intervals that are completely before the new interval. Then, merge the new interval with any overlapping intervals. Finally, add the remaining intervals.
-   **Algorithm:**

    1. Initialize an empty list `result` to store the merged intervals.
    2. Iterate through each interval in `intervals`:
        - If the current interval ends before `newInterval` starts, add the current interval to `result`.
        - If `newInterval` ends before the current interval starts, add `newInterval` to `result` and update `newInterval` to the current interval.
        - Otherwise, merge `newInterval` with the current interval by updating the start to the minimum of both starts and the end to the maximum of both ends.
    3. After the loop, add the final `newInterval` to `result`.
    4. Return `result`.

```pseudo
function insertInterval(intervals, newInterval):
	result = initialize as empty list
	for each interval in intervals:
		if interval.end < newInterval.start:
			append interval to result
		else if newInterval.end < interval.start:
			append newInterval to result
			newInterval = interval
		else:
			newInterval.start = minimum of newInterval.start and interval.start
			newInterval.end = maximum of newInterval.end and interval.end
	append newInterval to result
	return result
```
