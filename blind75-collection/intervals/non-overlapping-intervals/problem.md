# Blind75: Non-overlapping Intervals

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

**Note:** Intervals are non-overlapping even if they have a common point. For example, `[1, 3]` and `[2, 4]` are overlapping, but `[1, 2]` and `[2, 3]` are non-overlapping.

**Example 1:**

-   **Input:** `intervals = [[1,2],[2,4],[1,4]]`
-   **Output:** `1`
-   **Explanation:** After `[1,4]` is removed, the rest of the intervals are non-overlapping.

**Example 2:**

-   **Input:** `intervals = [[1,2],[2,4]]`
-   **Output:** `0`

### Constraints

-   `1 <= len(intervals) <= 1000`
-   `len(intervals[i]) == 2`
-   `-1000 <= start_i < end_i <= 1000`

---

### Approach 1: Greedy Interval Selection

-   **Time Complexity:** `O(n log n)` where `n` is the number of intervals.
-   **Space Complexity:** `O(1)` if sorting in place, otherwise `O(n)` for the sorted intervals.
-   **Description:** To minimize the number of intervals removed, we can employ a greedy strategy. Sort the intervals by their end times and iteratively select the interval with the earliest end time that doesn't overlap with the previously selected interval. Any interval that overlaps with the current one is removed.
-   **Algorithm:**

    1. Sort `intervals` by end times.
    2. Initialize `prev_end` with the end time of the first interval and `removal_count` as `0`.
    3. For each interval starting from the second one:
        - If the start time of the current interval is less than `prev_end`, increment `removal_count`.
        - Otherwise, update `prev_end` to the end time of the current interval.
    4. Return `removal_count`.

```python
def erase_overlap_intervals(intervals: List[List[int]]) -> int:
	intervals.sort(key=lambda x: x[1])

	removal_count = 0
	prev_end = intervals[0][1]

	for start, end in intervals[1:]:
		if start < prev_end:
			removal_count += 1
		else:
			prev_end = end

	return removal_count
```
