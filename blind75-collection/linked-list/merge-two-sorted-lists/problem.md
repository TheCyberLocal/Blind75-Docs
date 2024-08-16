# Blind75: Merge Two Sorted Lists

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from `list1` and `list2`.

**Example 1:**

-   **Input:** `list1 = [1,2,4]`, `list2 = [1,3,5]`
-   **Output:** `[1,1,2,3,4,5]`

**Example 2:**

-   **Input:** `list1 = []`, `list2 = [1,2]`
-   **Output:** `[1,2]`

**Example 3:**

-   **Input:** `list1 = []`, `list2 = []`
-   **Output:** `[]`

### Constraints

-   `0 <= The length of each list <= 100.`
-   `-100 <= Node.val <= 100`

---

### Approach 1: Iterative Merging

-   **Time Complexity:** `O(n + m)` where `n` and `m` are the lengths of `list1` and `list2`, respectively.
-   **Space Complexity:** `O(1)` as the solution reuses existing nodes and only allocates a few extra pointers.
-   **Description:** This approach involves iterating through both lists, comparing the current nodes, and building the new list in sorted order. We use a dummy node to simplify the merging process.
-   **Algorithm:**

    1. Initialize a dummy node to act as the start of the merged list and a `current` pointer pointing to the dummy node.
    2. While both `list1` and `list2` are not empty:
        - Compare the values of the nodes at `list1` and `list2`.
        - Attach the smaller node to `current.next` and move the corresponding pointer (`list1` or `list2`) forward.
        - Move the `current` pointer forward.
    3. After the loop, attach the remaining part of the non-empty list to `current.next`.
    4. Return the merged list starting from `dummy.next`.

```pseudo
function mergeTwoLists(list1, list2):
	dummy = new ListNode(0)
	current = dummy

	while list1 and list2:
		if list1.val <= list2.val:
			current.next = list1
			list1 = list1.next
		else:
			current.next = list2
			list2 = list2.next
		current = current.next

	current.next = list1 if list1 else list2

	return dummy.next
```
