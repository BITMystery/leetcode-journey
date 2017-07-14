class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        index = {k: 1}
        current_sum = 0
        res = 0
        for num in nums:
            current_sum += num
            print index, current_sum
            res += index.get(current_sum, 0)
            print res
            index[current_sum] = index.get(current_sum + k, 0) + 1
        return res

s = Solution()
print s.subarraySum([1, 1, 1], 2)