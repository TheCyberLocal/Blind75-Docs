class Solution:
    def __init__(self):
        self.res = ""
        self.res_len = 0

    def longest_palindrome(self, s: str) -> str:
        def pali_len(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > self.res_len:
                    self.res = s[left:right + 1]
                    self.res_len = right - left + 1
                left, right = left - 1, right + 1

        for i in range(len(s)):
            pali_len(i, i)       # Odd-length palindromes
            pali_len(i, i + 1)   # Even-length palindromes

        return self.res

solution = Solution()
print(solution.longest_palindrome("ababd"))
