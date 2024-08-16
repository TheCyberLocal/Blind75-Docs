# Blind75: Linked List Cycle

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the beginning of a linked list `head`, return `true` if there is a cycle in the linked list. Otherwise, return `false`.

A cycle exists in a linked list if at least one node in the list can be revisited by following the `next` pointer.

**Example 1:**

-   **Input:** `head = [1,2,3,4], index = 1`
-   **Output:** `true`
-   **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

-   **Input:** `head = [1,2], index = -1`
-   **Output:** `false`

### Constraints

-   `1 <= Length of the list <= 1000`
-   `-1000 <= Node.val <= 1000`
-   `index` is `-1` or a valid index in the linked list.

---

### Approach 1: Floyd's Tortoise and Hare

-   **Time Complexity:** `O(n)` where `n` is the number of nodes in the linked list.
-   **Space Complexity:** `O(1)` as no extra space is used apart from the pointers.
-   **Description:** The cycle detection can be done efficiently using Floyd's Tortoise and Hare algorithm. In this approach, two pointers are used: `slow` moves one step at a time, and `fast` moves two steps at a time. If a cycle exists, the `fast` pointer will eventually meet the `slow` pointer. If `fast` reaches the end of the list (`null`), then no cycle exists.
-   **Algorithm:**

    1. Initialize two pointers, `slow` and `fast`, to the head of the linked list.
    2. Move `slow` one step at a time and `fast` two steps at a time.
    3. If `slow` and `fast` pointers meet, return `true` indicating a cycle.
    4. If `fast` or `fast.next` becomes `null`, return `false` as there is no cycle.

```pseudo
function hasCycle(head):
	if not head:
		return false
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return true
	return false
```
