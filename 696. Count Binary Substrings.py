class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_0 = 0
        count_1 = 0
        cur = 0
        res = 0
        
        for c in s:
            if c == '0':
                if cur == 1:
                    count_0 = 1
                    cur = 0
                else:
                    count_0 += 1
                if count_1:
                    res += 1
                    count_1 -= 1
            else:
                if cur == 0:
                    count_1 = 1
                    cur = 1
                else:
                    count_1 += 1
                if count_0:
                    res += 1
                    count_0 -= 1
        return res