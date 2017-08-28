class Solution(object): 
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        index = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for num in nums[1:]:
            tmp_index = {}
            for s in index:
                tmp_index[s + num] = index[s] + tmp_index.get(s + num, 0)
                tmp_index[s - num] = index[s] + tmp_index.get(s - num, 0)
            del index
            index = tmp_index
        return index.get(S, 0)

class Solutio_2(object): #TLE solution
    def backtrack(self, nums, target, start, sums):
        if start == len(nums) - 1:
            if nums[-1] == target == 0:
                return 2 #good leaf
            elif nums[-1] == target or nums[-1] == -target:
                return 1 #good leaf
            else:
                return 0 #bad leaf
        if target % 2 == 1 and sums[start] % 2 == 0:
            return 0 #prune according to odd/even
        if target < -sums[start] or target > sums[start]:
            return 0 #prune according to range
        positive = self.backtrack(nums, target - nums[start], start + 1, sums)
        negative = self.backtrack(nums, target + nums[start], start + 1, sums)
        return positive + negative
    
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nums.sort(key = lambda x: x % 2, reverse = True)
        sums = [0] * len(nums)
        cur_sum = 0
        for i in xrange(len(nums) - 1, -1, -1):
            cur_sum += nums[i]
            sums[i] = cur_sum
        return self.backtrack(nums, S, 0, sums)