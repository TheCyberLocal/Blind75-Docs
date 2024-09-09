# Blind75: Valid Parentheses

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.

The input string `s` is valid if and only if:

1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return `True` if `s` is a valid string, and `False` otherwise.

**Example 1:**

- **Input:** `s = "[]"`
- **Output:** `True`

**Example 2:**

- **Input:** `s = "([{}])"`
- **Output:** `True`

**Example 3:**

- **Input:** `s = "[(])"`
- **Output:** `False`
- **Explanation:** The brackets are not closed in the correct order.

### Constraints

- `1 <= len(s) <= 1000`

---

### Approach 1: Stack

- **Time Complexity:** `O(n)` where `n` is the length of the string `s`.
- **Space Complexity:** `O(n)` in the worst case, for the stack that stores opening brackets.
- **Description:** The approach uses a stack to ensure that every closing bracket has a corresponding opening bracket of the same type and that they are closed in the correct order. As we iterate through the string, we push every opening bracket onto the stack. For each closing bracket, we pop from the stack and check if it matches the corresponding opening bracket. If any mismatch or unbalanced bracket is found, the string is invalid.
- **Algorithm:**

  1. Initialize an empty stack to store opening brackets.
  2. Create a mapping of closing brackets to their corresponding opening brackets.
  3. Iterate through each character in the string `s`:
     - If the character is an opening bracket, push it onto the stack.
     - If the character is a closing bracket, check if the stack is non-empty and the top of the stack is the corresponding opening bracket.
       - If true, pop the stack.
       - If false, return `False`.
  4. After the loop, return `True` if the stack is empty, indicating all brackets were matched correctly.

```python
def is_valid(s: str) -> bool:
	stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
```
