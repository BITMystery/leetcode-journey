class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        r = 0
        i = j = 0
        while i < len(g) and j < len(s):
        	if g[i] <= s[j]:
        		i += 1
        		j += 1
        		r += 1
        	else:
        		j += 1
        return r

s = Solution()
print s.findContentChildren([1,2,3], [1,1])