class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(s) == 1:
            return index[s[0]]
        if index[s[0]] >= index[s[1]]:
            return index[s[0]] + self.romanToInt(s[1:])
        if index[s[0]] < index[s[1]]:
            return self.romanToInt(s[1:]) - index[s[0]]