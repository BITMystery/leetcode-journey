class Solution(object):
    def say(self, s):
        res = ''
        i = 0
        while i < len(s):
            c = s[i]
            left = i
            right = i + 1
            while right < len(s) and s[right] == c:
                right += 1
            res += str(right - left) + c
            i = right
        return res

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in xrange(n - 1):
            s = self.say(s)
        return s

s = Solution()
print s.countAndSay(50)