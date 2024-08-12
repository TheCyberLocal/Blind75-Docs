# Blind75: Top K Frequent Elements

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
    count = {}
    for num in nums:
        if count[num]:
            count[num] += 1
        else:
            count[num] = 1

    buckets = array of size len(nums) initialized to []
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for i len(buckets) - 1 to 0:
        for num in buckets[i - 1]:
            result.append(num)
            if len(result) == k:
                return result
```
