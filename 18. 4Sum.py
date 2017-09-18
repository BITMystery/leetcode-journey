class Solution(object):
    def two_sum(self, nums, target):
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
        return res
        
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in xrange(len(nums) - 3):
            for j in xrange(i + 1, len(nums) - 2):
                comb = self.two_sum(nums[j + 1:], target - nums[i] - nums[j])
                for c in comb:
                    res.add((nums[i], nums[j], c[0], c[1]))
        return [list(ans) for ans in res]