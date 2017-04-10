import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = collections.Counter(nums).items()
        c.sort(key = lambda x: x[1], reverse = True)
        return [c[i][0] for i in xrange(k)]

s = Solution()
print s.topKFrequent([1,1,1,2,2,3], 2)
        