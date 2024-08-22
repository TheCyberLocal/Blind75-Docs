# Blind75: Word Break

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s` and a dictionary of strings `word_dict`, return `True` if `s` can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

**Example 1:**

-   **Input**: `s = "neetcode"`, `word_dict = ["neet","code"]`
-   **Output**: `True`
-   **Explanation**: Return `True` because `"neetcode"` can be split into `"neet"` and `"code"`.

**Example 2:**

-   **Input**: `s = "applepenapple"`, `word_dict = ["apple","pen","ape"]`
-   **Output**: `True`
-   **Explanation**: Return `True` because `"applepenapple"` can be split into `"apple"`, `"pen"`, and `"apple"`. Notice that we can reuse words and also not use all the words.

**Example 3:**

-   **Input**: `s = "catsincars"`, `word_dict = ["cats","cat","sin","in","car"]`
-   **Output**: `False`

### Constraints

-   `1 <= len(s) <= 200`
-   `1 <= len(word_dict) <= 100`
-   `1 <= len(word_dict[i]) <= 20`
-   `s` and `word_dict[i]` consist only of lowercase letters.

---

### Approach 1: Dynamic Programming

-   **Time Complexity**: `O(n * m)` where `n` is `len(s)` and `m` is the total number of characters in `word_dict`.
-   **Space Complexity**: `O(n)` where `n` is `len(s)`.
-   **Description**: This approach uses dynamic programming to determine whether the string can be segmented into words from the dictionary. The idea is to use a boolean array `dp` where `dp[i]` is `True` if the substring `s[0:i]` can be segmented into words from `word_dict`. The array is initialized with `dp[0] = True`, representing the empty string. Then, for each substring, we check if there is a word in the dictionary that ends at the current position and if the remaining part of the substring can be segmented as well.
-   **Algorithm**:

    1. Initialize a boolean array `dp` of size `n + 1` where `n` is the length of the string `s`. Set `dp[0] = True` because the empty string is always valid.
    2. Iterate over the string from index `1` to `n`.
    3. For each index `i`, check all possible substrings `s[j:i]` where `0 <= j < i`. If `s[j:i]` is in `word_dict` and `dp[j]` is `True`, then set `dp[i] = True`.
    4. Return `dp[n]` as the result.

```python
def word_break(s: str, word_dict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n + 1):
        for j in range(i + 1):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]
```
