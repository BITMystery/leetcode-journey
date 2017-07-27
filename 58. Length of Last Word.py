class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = len(s) - 1
        # skip tail space(s) if any
        while i >= 0 and s[i] == ' ':
                i -= 1
        # scan the last word
        while i >= 0 and s[i] != ' ':
            res += 1
            i -= 1
        return res