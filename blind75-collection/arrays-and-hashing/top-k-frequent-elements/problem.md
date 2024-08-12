# Blind75: Top K Elements in List

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

**Example 1:**

-   **Input**:
    -   `nums = [1,2,2,3,3,3]`
    -   `k = 2`
-   **Output**: `[2,3]`

**Example 2:**

-   **Input**:
    -   `nums = [7,7]`
    -   `k = 1`
-   **Output**: `[7]`

### Constraints

-   `1 <= len(nums) <= 10^4`
-   `-1000 <= nums[i] <= 1000`
-   `1 <= k <= number of distinct elements in nums`

---

### Approach 1: Bucket Sort

-   **Time Complexity**: `O(n)` where `n` is the number of elements in `nums`.
-   **Space Complexity**: `O(n)` for storing the frequency map and the bucket array.
-   **Description**: We use bucket sort to efficiently find the top `k` frequent elements. We first count the frequency of each element and then place elements into buckets based on their frequency. Finally, we collect the top `k` frequent elements from the buckets.
-   **Algorithm**:

    1. Create a frequency map to count the occurrences of each element in `nums`.
    2. Initialize an array `buckets` where the index represents the frequency and each index stores a list of elements with that frequency.
    3. Populate the `buckets` array using the frequency map.
    4. Iterate through the `buckets` array from the highest frequency to the lowest, collecting elements until `k` elements are collected.
    5. Return the collected elements as the result.

```pseudo
function topKFrequent(nums, k):
    frequencyMap = {}
    for num in nums:
        frequencyMap[num] = frequencyMap.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in frequencyMap.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
```

---

### Approach 2: Min-Heap

-   **Time Complexity**: `O(n log k)` where `n` is the number of elements in `nums`.
-   **Space Complexity**: `O(n + k)` for storing the frequency map and the heap.
-   **Description**: We can use a min-heap to keep track of the top `k` frequent elements. By pushing elements into the heap based on their frequency and maintaining the heap size to `k`, we can efficiently find the top `k` frequent elements.

-   **Algorithm**:
    1. Create a frequency map to count the occurrences of each element in `nums`.
    2. Initialize an empty min-heap.
    3. Iterate over the frequency map and push each element along with its frequency into the heap. If the heap size exceeds `k`, pop the smallest element.
    4. After processing all elements, the heap will contain the `k` most frequent elements.
    5. Extract the elements from the heap and return them as the result.

```pseudo
function topKFrequent(nums, k):
    frequencyMap = {}
    for num in nums:
        frequencyMap[num] = frequencyMap.get(num, 0) + 1

    minHeap = []
    for num, freq in frequencyMap.items():
        heapQ.push(minHeap, (freq, num))
        if len(minHeap) > k:
            heapQ.pop(minHeap)

    return [num for freq, num in minHeap]
```
