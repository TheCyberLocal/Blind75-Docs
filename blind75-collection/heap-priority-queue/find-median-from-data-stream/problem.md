# Blind75: Find Median in a Data Stream

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

Implement the `MedianFinder` class:

-   `MedianFinder()` initializes the `MedianFinder` object.
-   `void add_num(int num)` adds the integer `num` from the data stream to the data structure.
-   `double find_median()` returns the median of all elements so far.

**Example 1:**

-   **Input:** `["MedianFinder", "add_num", "1", "find_median", "add_num", "3", "find_median", "add_num", "2", "find_median"]`
-   **Output:** `[None, None, 1.0, None, 2.0, None, 2.0]`
-   **Explanation:**
    -   `MedianFinder median_finder = new MedianFinder();`
    -   `median_finder.add_num(1);` // arr = [1]
    -   `median_finder.find_median();` // return 1.0
    -   `median_finder.add_num(3);` // arr = [1, 3]
    -   `median_finder.find_median();` // return 2.0
    -   `median_finder.add_num(2);` // arr = [1, 2, 3]
    -   `median_finder.find_median();` // return 2.0

### Constraints

-   `-10^5 <= num <= 10^5`
-   `find_median` will only be called after adding at least one integer to the data structure.

---

### Approach 1: Two Heaps

-   **Time Complexity:** `O(log n)` for `add_num` and `O(1)` for `find_median`
-   **Space Complexity:** `O(n)`
-   **Description:** The idea is to maintain two heaps: a max-heap for the lower half of numbers and a min-heap for the upper half. The max-heap stores the smaller half of the elements, and the min-heap stores the larger half. The median can then be easily found by looking at the top elements of the heaps.
-   **Algorithm:**

    1.  **Initialize two heaps**:
        -   A max-heap `max_heap` (implemented as an inverted min-heap) to store the smaller half of the numbers.
        -   A min-heap `min_heap` to store the larger half of the numbers.
    2.  **When adding a number**:
        -   If `max_heap` is empty or `num` is less than or equal to the top of `max_heap` (inverted value), push `-num` into `max_heap` (to maintain max-heap property using `heapq`).
        -   Otherwise, push `num` into `min_heap`.
        -   Balance the heaps:
            -   If the top of `max_heap` (inverted value) is greater than the top of `min_heap`, move the top element from `max_heap` to `min_heap`.
            -   If `max_heap` has more than one extra element compared to `min_heap`, move the top element from `max_heap` to `min_heap`.
            -   If `min_heap` has more elements than `max_heap`, move the top element from `min_heap` to `max_heap`.
    3.  **When finding the median**:
        -   If `max_heap` has more elements, return the top element of `max_heap` (inverted value).
        -   If both heaps have the same number of elements, return the average of the top elements of `max_heap` (inverted value) and `min_heap`.

```python
class MedianFinder:
    def __init__(self) -> None:
        self.max_heap = []
        self.min_heap = []

    def add_num(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
```

---

### Approach 2: Insertion Sort with Array

-   **Time Complexity:** `O(n)` for `add_num` and `O(1)` for `find_median`
-   **Space Complexity:** `O(n)`
-   **Description:** This approach keeps an array sorted as numbers are added. The median is then found by indexing into the array.
-   **Algorithm:**

    1.  **Initialize**:
        -   Maintain a sorted list `sorted_nums` to store the numbers in sorted order.
    2.  **When adding a number**:
        -   If `sorted_nums` is empty, append the number to `sorted_nums`.
        -   Otherwise, iterate through `sorted_nums` to find the correct position to insert the number:
            -   If the number is less than the current element in `sorted_nums`, insert the number at that position.
            -   If the number is greater than all elements in `sorted_nums`, append the number to the end of the list.
    3.  **When finding the median**:
        -   Calculate the length `n` of `sorted_nums`.
        -   If `n` is odd, return the middle element of `sorted_nums`.
        -   If `n` is even, return the average of the two middle elements of `sorted_nums`.

```python
class MedianFinder:
    def __init__(self) -> None:
        self.sorted_nums = []

    def add_num(self, num: int) -> None:
        if not self.sorted_nums:
            self.sorted_nums.append(num)
        else:
            for i in range(len(self.sorted_nums)):
                if num < self.sorted_nums[i]:
                    self.sorted_nums.insert(i, num)
                    break
            else:
                self.sorted_nums.append(num)

    def find_median(self) -> float:
        n = len(self.sorted_nums)
        if n % 2 == 1:
            return self.sorted_nums[n // 2]
        else:
            return (self.sorted_nums[n // 2] + self.sorted_nums[n // 2 - 1]) / 2
```
