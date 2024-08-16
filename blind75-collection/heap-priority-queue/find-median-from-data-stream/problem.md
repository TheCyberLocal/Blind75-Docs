# Blind75: Find Median in a Data Stream

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

Implement the `MedianFinder` class:

-   `MedianFinder()` initializes the `MedianFinder` object.
-   `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
-   `double findMedian()` returns the median of all elements so far.

**Example 1:**

-   **Input:** `["MedianFinder", "addNum", "1", "findMedian", "addNum", "3", "findMedian", "addNum", "2", "findMedian"]`
-   **Output:** `[null, null, 1.0, null, 2.0, null, 2.0]`
-   **Explanation:**
    -   `MedianFinder medianFinder = new MedianFinder();`
    -   `medianFinder.addNum(1);` // arr = [1]
    -   `medianFinder.findMedian();` // return 1.0
    -   `medianFinder.addNum(3);` // arr = [1, 3]
    -   `medianFinder.findMedian();` // return 2.0
    -   `medianFinder.addNum(2);` // arr = [1, 2, 3]
    -   `medianFinder.findMedian();` // return 2.0

### Constraints

-   `-10^5 <= num <= 10^5`
-   `findMedian` will only be called after adding at least one integer to the data structure.

---

### Approach 1: Two Heaps

-   **Time Complexity:** `O(log n)` for `addNum` and `O(1)` for `findMedian`
-   **Space Complexity:** `O(n)`
-   **Description:** The idea is to maintain two heaps: a max-heap for the lower half of numbers and a min-heap for the upper half. The max-heap stores the smaller half of the elements, and the min-heap stores the larger half. The median can then be easily found by looking at the top elements of the heaps.

-   **Algorithm:**

    1. Initialize two heaps:
        - A max-heap `maxHeap` to store the smaller half of the numbers.
        - A min-heap `minHeap` to store the larger half of the numbers.
    2. When adding a number:
        - If `maxHeap` is empty or `num` is less than or equal to the top of `maxHeap`, push `num` into `maxHeap`.
        - Otherwise, push `num` into `minHeap`.
        - Balance the heaps so that `maxHeap` has at most one more element than `minHeap`.
    3. When finding the median:
        - If `maxHeap` has more elements, return its top element.
        - If both heaps have the same number of elements, return the average of the top elements of both heaps.

```pseudo
class MedianFinder:
	maxHeap = initialize as an empty max-heap
	minHeap = initialize as an empty min-heap

	function addNum(num):
		if maxHeap is empty or num <= maxHeap.peek():
			maxHeap.push(num)
		else:
			minHeap.push(num)
		if maxHeap.size > minHeap.size + 1:
			minHeap.push(maxHeap.pop())
		else if minHeap.size > maxHeap.size:
			maxHeap.push(minHeap.pop())

	function findMedian():
		if maxHeap.size > minHeap.size:
			return maxHeap.peek()
		else:
			return (maxHeap.peek() + minHeap.peek()) / 2
```

---

### Approach 2: Insertion Sort with Array

-   **Time Complexity:** `O(n)` for `addNum` and `O(1)` for `findMedian`
-   **Space Complexity:** `O(n)`
-   **Description:** This approach keeps an array sorted as numbers are added. The median is then found by indexing into the array.

-   **Algorithm:**

    1. Maintain a sorted list `sortedNums` of numbers.
    2. When adding a number, insert it into the correct position in `sortedNums` to maintain the order.
    3. When finding the median:
        - If the size of `sortedNums` is odd, return the middle element.
        - If the size of `sortedNums` is even, return the average of the two middle elements.

```pseudo
class MedianFinder:
	sortedNums = initialize as an empty list

	function addNum(num):
		insert `num` into `sortedNums` maintaining sorted order

	function findMedian():
		n = len(sortedNums)
		if n % 2 == 1:
			return sortedNums[n // 2]
		else:
			return (sortedNums[n // 2] + sortedNums[n // 2 - 1]) / 2
```
