class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for i in xrange(len(nums)-2):
        	for j in xrange(i+1, len(nums)-1):
        		pair_sum = nums[i] + nums[j]
        		lo, hi = j + 1, len(nums) - 1
        		if pair_sum <= nums[lo]:
        			continue
        		while lo != hi:
        			tmp = (lo + hi) / 2
        			if pair_sum > nums[tmp]:
        				if lo == tmp:
        					if pair_sum > nums[hi]:
        						lo = hi
        					else:
        						hi = lo
        				else:
        					lo = tmp
        			else:
        				if hi == tmp:
        					if pair_sum <= nums[lo]:
        						hi = lo
        					else:
        						lo = hi
        				else:
        					hi = tmp
        		k = lo
        		res += k - j
        return res

class Solution2(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for i in xrange(len(nums) - 1, 1, -1):
        	lo, hi = 0, i - 1
        	while lo < hi:
        		if nums[lo] + nums[hi] > nums[i]:
        			res += hi - lo
        			hi -= 1
        		else:
        			lo += 1
        return res

s = Solution2()
print s.triangleNumber([3, 19, 22, 24, 35, 82, 84])
