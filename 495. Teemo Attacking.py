class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        for i in xrange(1, len(timeSeries)):
        	if timeSeries[i] - timeSeries[i-1] < duration:
        		total += timeSeries[i] - timeSeries[i-1]
        	else:
        		total += duration
        if timeSeries:
        	total += duration
        return total

s = Solution()
print s.findPoisonedDuration([], 10000)