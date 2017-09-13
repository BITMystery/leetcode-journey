class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #dp[i] stands for the (min tail of LIS of length i + 1, num of LIS with min tail)
        dp = [[(nums[0], 1)]]
        for num in nums[1:]:
            if num > dp[-1][-1][0]:
                m = 0
                for (min_tail, n) in dp[-1][::-1]:
                    if num > min_tail:
                        m += n
                    else:
                        break
                dp.append([(num, m)])
            else:
                left, right = 0, len(dp) - 1
                while left != right:
                    mid = (left + right) / 2
                    if num > dp[mid][-1][0]:
                        left = mid + 1
                    else:
                        right = mid
                if left == 0:
                    dp[left].append((num, 1))
                else:
                    m = 0
                    for (min_tail, n) in dp[left - 1][::-1]:
                        if num > min_tail:
                            m += n
                        else:
                            break
                    dp[left].append((num, m))
        return sum([n for (min_tail, n) in dp[-1]])
                