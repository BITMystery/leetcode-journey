class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r_origin = len(nums)
        c_origin = len(nums[0])
        if r * c != r_origin * c_origin:
            return nums
        res = [[0 for _ in xrange(c)] for _ in xrange(r)]
        for i in xrange(r * c):
            res[i / c][i % c] = nums[i / c_origin][i % c_origin]
        return res

s = Solution()
print s.matrixReshape([[1, 2], [3, 4]], 1, 4)