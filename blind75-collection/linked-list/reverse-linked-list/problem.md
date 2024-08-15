# Blind75: Reverse Linked List

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

Given the beginning of a singly linked list `head`, reverse the list, and return the new beginning of the list.

**Example 1:**

-   **Input:** `head = [0,1,2,3]`
-   **Output:** `[3,2,1,0]`

**Example 2:**

-   **Input:** `head = []`
-   **Output:** `[]`

### Constraints

-   `0 <= The length of the list <= 1000`
-   `-1000 <= Node.val <= 1000`

---

### Approach 1: Iterative Reversal

-   **Time Complexity:** `O(n)` where `n` is the length of the list.
-   **Space Complexity:** `O(1)` as it reverses the list in place.
-   **Description:** This approach iteratively reverses the linked list by adjusting the `next` pointers of each node.
-   **Algorithm:**

    1. Start with `prev` as `null` and `curr` as `head`.
    2. Traverse the list, reversing the `next` pointer of each node to point to `prev`.
    3. After reversing the pointers, move `prev` and `curr` one step forward.
    4. Once `curr` is `null`, `prev` will be the new head of the reversed list and you can return it.

```pseudo
function reverseList(head):
	prev, curr = null, head

	while curr:
		nextNode = curr.next
		curr.next = prev
		prev = curr
		curr = nextNode

	return prev
```

---

### Approach 2: Recursive Reversal

-   **Time Complexity:** `O(n)` where `n` is the length of the list.
-   **Space Complexity:** `O(n)` due to the recursive call stack.
-   **Description:** This approach uses recursion to reverse the linked list, processing one node at a time until reaching the end of the list, then reversing the pointers as the call stack unwinds.
-   **Algorithm:**

    1. If the list is empty or has only one node, return `head`.
    2. Recursively reverse the rest of the list starting from the second node.
    3. After reversing the rest of the list, adjust the pointers so the second node points to the first node.
    4. The last node in the original list becomes the new head and you can return it.

```pseudo
function reverseList(head):
	if !head or !head.next:
		return head

	newHead = reverseList(head.next)

	head.next.next = head
	head.next = null

	return newHead
```
