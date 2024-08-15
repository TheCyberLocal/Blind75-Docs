# Blind75: Meeting Rooms II

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

Given an array of meeting time intervals consisting of start and end times `[[start_1,end_1],[start_2,end_2],...]` where `start_i < end_i`, find the minimum number of meeting rooms required to schedule all meetings without any conflicts.

**Example 1:**

-   **Input:** `intervals = [(0,40),(5,10),(15,20)]`
-   **Output:** `2`
-   **Explanation:**
    -   **Day 1:** `(0,40)`
    -   **Day 2:** `(5,10), (15,20)`

**Example 2:**

-   **Input:** `intervals = [(4,9)]`
-   **Output:** `1`

### Constraints

-   `0 <= len(intervals) <= 500`
-   `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

---

### Approach 1: Using Min-Heap

-   **Time Complexity:** `O(n log n)` where `n` is the number of intervals
-   **Space Complexity:** `O(n)` for the heap to store end times of intervals
-   **Description:** To determine the minimum number of rooms required, we can use a min-heap to keep track of the end times of ongoing meetings. We sort the intervals by start time, and then iterate through each interval. If the current meeting starts after the earliest ending meeting, we can reuse the room (pop from the heap and push the new end time). Otherwise, we need a new room (push the end time to the heap). The size of the heap at any point gives the minimum number of rooms required.
-   **Algorithm:**

    1. If `intervals` is empty, return `0`.
    2. Sort `intervals` by start time.
    3. Initialize a min-heap `rooms` to track meeting end times.
    4. For each interval in `intervals`:
        - If the start time of the current interval is greater than or equal to the smallest end time in the heap, reuse the room (pop the heap).
        - Push the end time of the current interval onto the heap.
    5. The size of the heap at the end of iteration is the minimum number of rooms required.

```pseudo
function minMeetingRooms(intervals):
	if len(intervals) == 0:
		return 0
	sort intervals by start time
    rooms = empty min-heap
	for interval in intervals:
		if len(rooms) > 0 and interval.start >= rooms.peek():
			rooms.pop()
		rooms.push(interval.end)
	return rooms.size
```
