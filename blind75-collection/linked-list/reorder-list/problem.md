# Blind75: Reorder List

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

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

```python
def reorder_list(head: Optional[ListNode]) -> None:
	slow, fast = head, head.next

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	second = slow.next
	prev = slow.next = None

	while second:
		tmp = second.next
		second.next = prev
		prev = second
		second = tmp

	first, second = head, prev

	while second:
		tmp1, tmp2 = first.next, second.next
		first.next = second
		second.next = tmp1
		first, second = tmp1, tmp2
```
