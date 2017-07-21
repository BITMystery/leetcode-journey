class Solution(object):
    def backtrack(self, nums, start, path, res):
        if len(path) == len(nums):
            res.append(path) #leaf
            return
        for i in xrange(start, len(nums)):
            if i > start:
                flag = 0
                for j in xrange(start, i):
                    if nums[j] == nums[i]:
                        flag = 1
                        break
                if flag:
                    continue
            nums[i], nums[start] = nums[start], nums[i]
            self.backtrack(nums, start + 1, path + [nums[start]], res)
            nums[i], nums[start] = nums[start], nums[i]
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.backtrack(nums, 0, [], res)
        return res