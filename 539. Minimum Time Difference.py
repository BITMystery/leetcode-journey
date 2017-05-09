class Solution(object):
    def getDifference(self, time1, time2):
    	time1 = time1.split(':')
    	time2 = time2.split(':')
    	minutes1 = int(time1[0]) * 60 + int(time1[1])
    	minutes2 = int(time2[0]) * 60 + int(time2[1])
    	return min(minutes2 - minutes1, 1440 + minutes1 - minutes2)
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints.sort()
        res = min(self.getDifference(timePoints[i], timePoints[i+1]) for i in xrange(len(timePoints) - 1))
        return min(res, self.getDifference(timePoints[0], timePoints[-1]))

s = Solution()
print s.findMinDifference(["12:12","00:13"])