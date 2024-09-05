# Blind75: Remove Nth Node From End of List

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given the beginning of a linked list `head`, and an integer `n`.

Remove the nth node from the end of the list and return the beginning of the list.

**Example 1:**

-   **Input:** `head = [1,2,3,4]`, `n = 2`
-   **Output:** `[1,2,4]`

**Example 2:**

-   **Input:** `head = [5]`, `n = 1`
-   **Output:** `[]`

**Example 3:**

-   **Input:** `head = [1,2]`, `n = 2`
-   **Output:** `[2]`

### Constraints

-   The number of nodes in the list is `sz`.
-   `1 <= sz <= 30`
-   `0 <= Node.val <= 100`
-   `1 <= n <= sz`

---

### Approach 1: Two-Pointer Technique

-   **Time Complexity:** `O(sz)` where `sz` is the number of nodes in the list.
-   **Space Complexity:** `O(1)` as the solution only uses a few extra pointers.
-   **Description:** This approach utilizes a two-pointer technique, where one pointer is moved `n` steps ahead. Then, both pointers are moved simultaneously until the first pointer reaches the end of the list. This positions the second pointer at the node just before the target node, allowing for easy removal of the nth node from the end.
-   **Algorithm:**

    1. Initialize a dummy node pointing to `head` to handle edge cases where the head needs to be removed.
    2. Set two pointers, `first` and `second`, both pointing to the dummy node.
    3. Move the `first` pointer `n + 1` steps forward to maintain a gap of `n` between `first` and `second`.
    4. Move both pointers forward until `first` reaches the end of the list.
    5. The `second` pointer will now be at the node just before the target node. Update `second.next` to skip the target node.
    6. Return the list starting from `dummy.next`.

```python
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
	dummy = ListNode(0)
	dummy.next = head
	first = dummy
	second = dummy

	for _ in range(n + 1):
		first = first.next

	while first:
		first = first.next
		second = second.next

	second.next = second.next.next
	return dummy.next
```
