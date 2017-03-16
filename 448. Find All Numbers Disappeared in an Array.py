class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #O(n) runtime, but uses extra space.
        r = []
        n = len(nums)
        nums = set(nums)
        for i in range(1, n+1):
        	if i not in nums:
        		r.append(i)
        return r

class Solution_2(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #O(n) runtime without extra space
        for num in nums:
        	nums[abs(num) - 1] = - abs(nums[abs(num) - 1])
        return [i + 1 for i in xrange(len(nums)) if nums[i] > 0]

s = Solution_2()
print s.findDisappearedNumbers([1,1])