import collections

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        flag = any([c[letter] % 2 == 1 for letter in c]) # there is a letter appears odd times
        res = 0
        for letter in c:
            res += c[letter] if c[letter] % 2 == 0 else c[letter] - 1
        return res + 1 if flag else res