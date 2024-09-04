# Blind75: Merge Intervals

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

**Note:** Intervals are non-overlapping if they have no common point. For example, `[1, 2]` and `[3, 4]` are non-overlapping, but `[1, 2]` and `[2, 3]` are overlapping.

**Example 1:**

-   **Input:** `intervals = [[1,3],[1,5],[6,7]]`
-   **Output:** `[[1,5],[6,7]]`

**Example 2:**

-   **Input:** `intervals = [[1,2],[2,3]]`
-   **Output:** `[[1,3]]`

### Constraints

-   `1 <= len(intervals) <= 1000`
-   `len(intervals[i]) == 2`
-   `0 <= start <= end <= 1000`

---

### Approach 1: Sorting and Merging

-   **Time Complexity:** `O(n log n)` where `n` is the number of intervals.
-   **Space Complexity:** `O(n)` for the merged intervals.
-   **Description:** To merge overlapping intervals, we first sort the intervals based on their start times. Then, iterate through the sorted intervals and merge them if they overlap. This approach guarantees that overlapping intervals are adjacent, making it easier to merge them in one pass.
-   **Algorithm:**

    1. Sort `intervals` based on start times.
    2. Initialize an empty list `merged`.
    3. For each interval in `intervals`:
        - If `merged` is empty or the current interval does not overlap with the last interval in `merged`, add the current interval to `merged`.
        - Otherwise, merge the current interval with the last interval in `merged` by updating the end time.
    4. Return `merged`.

```python
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
	intervals.sort(key=lambda pair: pair[0])
	merged = [intervals[0]]

	for interval in intervals:
		if not merged or interval[0] > merged[-1][1]:
			merged.append(interval)
		else:
			merged[-1][1] = max(merged[-1][1], interval[1])

	return merged
```
