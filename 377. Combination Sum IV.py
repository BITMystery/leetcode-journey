class Solution(object):
    def helper(self, nums, target, results):
        res = 0
        for num in nums:
            if num > target:
                break
            if target - num not in results:
                results[target - num] = self.helper(nums, target - num, results)
            res += results[target - num]
        return res
    
    def combinationSum4(self, nums, target):
        nums.sort()
        return self.helper(nums, target, {0: 1})