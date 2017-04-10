class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in xrange(len(numbers)):
        	if d.get(numbers[i], 0) == 0:
        		d[numbers[i]] = [i + 1]
        	else:
        		d[numbers[i]].append(i + 1)
        for num in numbers:
        	if target - num in d:
        		if num != target - num:
        			return [d[num][0], d[target-num][0]]
        		else:
        			return [d[num][0], d[num][1]]

s = Solution()
print s.twoSum([0,0,3,4], 0)