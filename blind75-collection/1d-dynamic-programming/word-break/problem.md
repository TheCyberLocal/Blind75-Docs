# Blind75: Word Break

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

**Example 1:**

- **Input**: `s = "neetcode"`, `wordDict = ["neet","code"]`
- **Output**: `true`
- **Explanation**: Return `true` because `"neetcode"` can be split into `"neet"` and `"code"`.

**Example 2:**

- **Input**: `s = "applepenapple"`, `wordDict = ["apple","pen","ape"]`
- **Output**: `true`
- **Explanation**: Return `true` because `"applepenapple"` can be split into `"apple"`, `"pen"`, and `"apple"`. Notice that we can reuse words and also not use all the words.

**Example 3:**

- **Input**: `s = "catsincars"`, `wordDict = ["cats","cat","sin","in","car"]`
- **Output**: `false`

### Constraints

- `1 <= len(s) <= 200`
- `1 <= len(wordDict) <= 100`
- `1 <= len(wordDict[i]) <= 20`
- `s` and `wordDict[i]` consist of only lowercase letters.

---

### Approach 1: Dynamic Programming

- **Time Complexity**: `O(n * m * o)` where `n` is `len(s)`, `m` is `len(wordDict)`, and `o` is the average word length in the dictionary.
- **Space Complexity**: `O(n)` where `n` is `len(s)`.
- **Description**: This approach uses dynamic programming to determine whether the string can be segmented into words from the dictionary. The idea is to use a boolean array `dp` where `dp[i]` is `true` if the substring `s[0:i]` can be segmented into words from `wordDict`. The array is initialized with `dp[0] = true`, representing the empty string. Then, for each substring, we check if there is a word in the dictionary that ends at the current position and if the remaining part of the substring can be segmented as well.
- **Algorithm**:

  1. Initialize a boolean array `dp` of size `n+1` where `n` is the length of the string `s`. Set `dp[0] = true` because the empty string is always valid.
  2. Iterate over the string from index `1` to `n`.
  3. For each index `i`, check all possible substrings `s[j:i]` where `0 <= j < i`. If `s[j:i]` is in `wordDict` and `dp[j]` is `true`, then set `dp[i] = true`.
  4. Return `dp[n]` as the result.

  ```pseudo
  function wordBreak(s, wordDict):
    dp = array of size len(s) + 1 initialized to false
    dp[0] = true

    for i from 1 to len(s):
        for j from 0 to i:
            if dp[j] and s[j:i] in wordDict:
                dp[i] = true
                break

    return dp[len(s)]
  ```

---

### Approach 2: Dynamic Programming with Reversed Iteration

- **Time Complexity**: `O(n * m * o)` where `n` is `len(s)`, `m` is `len(wordDict)`, and `o` is the average word length in the dictionary.
- **Space Complexity**: `O(n)` where `n` is `len(s)`.
- **Description**: This approach uses dynamic programming to solve the problem by iterating through the string `s` in reverse order. The `dp` array keeps track of whether the substring starting from a given index `i` to the end of the string can be segmented into words from the dictionary. Starting from the end of the string (`dp[len(s)]`), which is initialized to `true`, the algorithm checks each word in the dictionary to see if it matches the substring starting at `i`. If a match is found and the remaining substring (from the end of the matched word onward) can be segmented (`dp[i + len(word)]` is `true`), then `dp[i]` is set to `true`. The process continues until the start of the string, and the result is `dp[0]`, which indicates whether the entire string can be segmented.
- **Algorithm**:

  1. Initialize a boolean array `dp` of size `len(s) + 1` to `false`, and set `dp[len(s)] = true`.
  2. Iterate over the string `s` from the second last index to `0`.
  3. For each index `i`, check each word in `wordDict`:
     - If the substring `s[i:i+len(word)]` matches the word and `i + len(word) <= len(s)`, set `dp[i] = dp[i + len(word)]`.
     - If `dp[i]` is `true`, break the inner loop as no further checks are needed.
  4. Return `dp[0]` as the final result, indicating whether the entire string can be segmented into words from `wordDict`.

```pseudo
function wordBreak(s, wordDict):
    dp = array of size len(s) + 1 initialized to false
    dp[len(s)] = true

    for i from (len(s) - 1) to 0:
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break

    return dp[0]
```
