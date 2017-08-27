class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s = 0
        height = nums[-1] / 100
        path_num = [0] * (2 ** (height - 1))
        for i in xrange(height, 1, -1):
            new_path_num = [0] * (len(path_num) / 2)
            while nums[-1] / 100 == i:
                node = nums.pop()
                position = node % 100 / 10
                if path_num[position - 1] == 0:
                    path_num[position - 1] = 1
                value = node % 10
                s += value * path_num[position - 1]
                new_path_num[(position - 1) / 2] += path_num[position - 1]
            del path_num
            path_num = new_path_num
        s += nums[0] % 10 * max(path_num[0], 1)
        return s