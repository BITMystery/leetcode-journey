class Solution(object):
    def helper(self, nums, start, end, index):
        if start == end:
            player1 = nums[start]
            player2 = 0
            index[(start, end)] = (player1, player2)
            return (player1, player2)
        
        #player1 fisrt picks nums[start]
        if (start + 1, end) in index:
            score1 = nums[start] + index[(start + 1, end)][1]
        else:
            score1 = nums[start] + self.helper(nums, start + 1, end, index)[1]
        
        #player1 first picks nums[end]
        if (start, end - 1) in index:
            score2 = nums[end] + index[(start, end - 1)][1]
        else:
            score2 = nums[end] + self.helper(nums, start, end - 1, index)[1]
        
        s = sum(index[(start + 1, end)]) + nums[start]
        player1 = max(score1, score2)
        player2 = s - player1
        index[(start, end)] = (player1, player2)
        return (player1, player2)
        
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = {}
        (player1, player2) = self.helper(nums, 0, len(nums) - 1, index)
        return True if player1 >= player2 else False