# Blind75: Reorder List

### [⇦ Back to Problem Index](../../index.md)

## Problem Statement

You are given the head of a singly linked list. Reorder the nodes of the linked list in the following pattern:

For a list of length `n`, the positions should be reordered as:

`[0, n-1, 1, n-2, 2, n-3, ...]`

**Example 1:**

-   **Input:** `head = [2,4,6,8]`
-   **Output:** `[2,8,4,6]`

**Example 2:**

-   **Input:** `head = [2,4,6,8,10]`
-   **Output:** `[2,10,4,8,6]`

### Constraints

-   `1 <= Length of the list <= 1000`
-   `1 <= Node.val <= 1000`

---

### Approach 1: Splitting and Reversing the Second Half

-   **Time Complexity:** `O(n)` where `n` is the length of the list.
-   **Space Complexity:** `O(1)` as it modifies the list in place.
-   **Description:** This approach divides the list into two halves, reverses the second half, and then merges the two halves by alternating nodes from each half.
-   **Algorithm:**

    1. Use the slow and fast pointer technique to find the middle of the linked list.
    2. Divide the list into two halves, where the first half starts at the head, and the second half starts at the node after the middle.
    3. Reverse the second half of the list.
    4. Merge the two halves by alternating nodes from the first and second halves.

```pseudo
function reorderList(head):
	if not head or not head.next:
		return

	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	firstHalf = head
	secondHalf = slow.next
	slow.next = null

	prev = null
	while not secondHalf:
		nextNode = secondHalf.next
		secondHalf.next = prev
		prev = secondHalf
		secondHalf = nextNode

	secondHalf = prev

	while not secondHalf:
		temp1 = firstHalf.next
		temp2 = secondHalf.next

		firstHalf.next = secondHalf
		secondHalf.next = temp1

		firstHalf = temp1
		secondHalf = temp2
```
