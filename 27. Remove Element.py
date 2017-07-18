class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                while len(nums) > 0 and nums[-1] == val:
                    del nums[-1]
                if len(nums) < i:
                    break
                print nums, nums[-1], i
                nums[i], nums[-1] = nums[-1], nums[i]
                del nums[-1]
            else:
                i += 1
        return len(nums)

s = Solution()
print s.removeElement([4], 4)