class Solution(object): #one-pass
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i in xrange(len(nums)):
            if nums[i] in index:
                return [index[nums[i]], i]
            index[target - nums[i]] = i

class Solution_2(object): #two-pass
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i in xrange(len(nums)):
            if nums[i] in index:
                index[nums[i]].append(i)
            else:
                index[nums[i]] = [i]
        for i in xrange(len(nums)):
            if nums[i] * 2 == target:
                if len(index[nums[i]]) > 1:
                    return index[nums[i]]
            else:
                if target - nums[i] in index:
                    return [i, index[target - nums[i]][0]]