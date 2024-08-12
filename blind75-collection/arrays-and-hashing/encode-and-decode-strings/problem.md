# Blind75: Encode and Decode Strings

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Implement both `encode` and `decode` methods.

**Example 1:**

-   **Input**:
    -   `["neet","code","love","you"]`
-   **Output**:
    -   `["neet","code","love","you"]`

**Example 2:**

-   **Input**:
    -   `["we","say",":","yes"]`
-   **Output**:
    -   `["we","say",":","yes"]`

### Constraints

-   `0 <= len(strs) < 100`
-   `0 <= len(strs[i]) < 200`
-   `strs[i]` contains only UTF-8 characters.

---

### Approach 1: Length-Prefix Encoding

-   **Time Complexity**: `O(n)` for both encoding and decoding where `n` is the total number of characters across all strings.
-   **Space Complexity**: `O(n)` for storing the encoded and decoded strings.
-   **Description**: We use a length-prefix encoding scheme where each string is encoded as the length of the string followed by a special delimiter and then the string itself. The delimiter is avoids confusion when an encoded string begins with an integer. During decoding, we read the length, extract the corresponding string, and continue until the entire encoded string is processed.
-   **Algorithm**:

    **Encoding**:

    1. Initialize an empty encoded string `cipher`.
    2. For each string `s` in the input list, append the length of `s`, a delimiter (e.g., `'#'`), and `s` itself to `cipher`.
    3. Return `cipher`.

    **Decoding**:

    1. Initialize an empty list `strs`.
    2. Iterate over `cipher`, reading the length prefix and the corresponding string.
    3. Extract the string based on the length, append it to `strs`, and continue until the entire string is decoded.
    4. Return `strs`.

```pseudo
function encode(strs):
    cipher = ""
    for s in strs:
        cipher += str(len(s)) + "#" + s
    return cipher

function decode(cipher):
    strs = []
    i = 0

    while i < len(cipher):
        j = i
        while cipher[j] != "#":
            j += 1
        length = int(cipher[i:j])
        strs.append(cipher[j + 1:j + 1 + length])
        i = j + 1 + length
    return strs
```
