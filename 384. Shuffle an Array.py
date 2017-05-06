import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = self.nums[:]
        random.shuffle(nums)
        return nums
        


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
print obj.reset()
print obj.shuffle()
print obj.reset()