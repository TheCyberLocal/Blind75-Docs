# Blind75: Merge K Sorted Lists

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

You are given an array of `k` linked lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all the individual linked lists.

**Example 1:**

-   **Input:** `lists = [[1,2,4],[1,3,5],[3,6]]`
-   **Output:** `[1,1,2,3,3,4,5,6]`

**Example 2:**

-   **Input:** `lists = []`
-   **Output:** `[]`

**Example 3:**

-   **Input:** `lists = [[]]`
-   **Output:** `[]`

### Constraints

-   `0 <= len(lists) <= 1000`
-   `0 <= len(lists[i]) <= 100`
-   `-1000 <= lists[i][j] <= 1000`

---

### Approach 1: Min-Heap (Priority Queue)

-   **Time Complexity:** `O(n log k)`, where `n` is the total number of nodes across all lists and `k` is the number of linked lists.
-   **Space Complexity:** `O(k)` for the merge process.
-   **Description:** This approach leverages the divide and conquer technique to efficiently merge `k` sorted linked lists. The idea is to pair up the lists and merge each pair. This process is repeated iteratively, halving the number of lists at each step until only one merged list remains. This method is efficient because it reduces the problem size by half in each iteration, leading to a logarithmic number of merge operations.
-   **Algorithm:**

    1. If the list of linked lists is empty, return `null`.
    2. While there are more than one list:
        1. Initialize an empty list `mergedLists` to store the merged results of the current iteration.
        2. For each pair of adjacent lists `l1` and `l2`:
            - Merge `l1` and `l2` using a helper function `mergeList`.
            - Append the merged list to `mergedLists`.
        3. Replace the original list of lists with `mergedLists`.
    3. Once only one list remains, return it as the final merged linked list.

```pseudo
function mergeKLists(lists):
        if !len(lists):
            return null

        while len(lists) > 1:
            mergedLists = []
            for i from 0 to len(lists) - 1 by 2's:
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else null
                mergedLists.append(mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    function mergeList(l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
```
