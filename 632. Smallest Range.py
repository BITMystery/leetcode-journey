import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        common_range = [(nums[i][0], i, 0) for i in xrange(len(nums))] # element in heap: (value, row, offset)
        heapq.heapify(common_range)
        left = -1e5
        right = max([nums[i][0] for i in xrange(len(nums))])
        res = [left, right]
        total = sum([len(nums[i]) for i in xrange(len(nums))])
        while True:
            left, row, offset = heapq.heappop(common_range)
            if right - left < res[1] - res[0]:
                res = [left, right]
            if offset + 1 < len(nums[row]):
                heapq.heappush(common_range, (nums[row][offset + 1], row, offset + 1))
                right = max(right, nums[row][offset + 1])
            else:
                break
        return res