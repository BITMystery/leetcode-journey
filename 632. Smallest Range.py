import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        window = [(nums[i][0], i, 0) for i in xrange(len(nums))]
        heapq.heapify(window)
        smallest = min([nums[i][0] for i in xrange(len(nums))])
        largest = max([nums[i][0] for i in xrange(len(nums))])
        res = smallest, largest
        while True:
            smallest, row, offset = heapq.heappop(window)
            if offset + 1 == len(nums[row]):
                break
            heapq.heappush(window, (nums[row][offset + 1], row, offset + 1))
            smallest = window[0][0]
            largest = max(largest, nums[row][offset + 1])
            if largest - smallest < res[1] - res[0]:
                res = smallest, largest
        return res
