class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        moves = 0
        nums.sort()
        mid_num = nums[len(nums)/2]
        for num in nums:
        	moves += abs(num - mid_num)
        return moves

s = Solution()
print s.minMoves2([1,3,2])