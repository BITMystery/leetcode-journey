class Solution(object):
    def combineList(self, l, k):
    	res = []
    	if k == 1:
    		for num in l:
    			res.append([num])
    	else:
    		for i in xrange(len(l)-k+1):
    			sub_res = self.combineList(l[i+1:], k-1)
    			for r in sub_res:
    				res.append([l[i]] + r)
    	return res
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0 or k <= 0 or n < k:
    		return []
        return self.combineList([i for i in xrange(1, n+1)], k)

s = Solution()
print s.combine(5, 3)