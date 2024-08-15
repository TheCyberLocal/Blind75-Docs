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

-   `0 <= lists.length <= 1000`
-   `0 <= lists[i].length <= 100`
-   `-1000 <= lists[i][j] <= 1000`

---

### Approach 1: Min-Heap (Priority Queue)

-   **Time Complexity:** `O(n log k)` where `n` is the total number of nodes across all lists and `k` is the number of linked lists.
-   **Space Complexity:** `O(k)` for storing nodes in the heap.
-   **Description:** We can efficiently merge the k sorted lists using a min-heap (priority queue). The min-heap helps to keep track of the smallest element among the k lists. We keep adding the smallest element to the result list until all nodes are merged.
-   **Algorithm:**

    1. Initialize an empty min-heap.
    2. Insert the head of each linked list into the heap.
    3. Extract the smallest element from the heap and add it to the merged linked list.
    4. If the extracted node has a next node, insert it into the heap.
    5. Repeat steps 3-4 until the heap is empty.

```pseudo
function mergeKLists(lists):
        if len(lists) == 0:
            return none

        while len(lists) > 1:
            mergedLists = []
            for i from 0 to len(lists) - 1 by 2's:
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else none
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
