class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        #dp[i] stands for the minimum ending num of incresing subsequence of length i + 1
        dp = []
        for num in nums:
            left, right = 0, len(dp)
            while left != right:
                mid = (left + right) / 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(dp):
                dp.append(num)
            else:
                dp[left] = num
        return len(dp)