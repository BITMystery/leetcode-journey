class Solution(object):
    def calculate(self, nums, flag):
        if len(nums) == 1:
            return set(nums)
        if len(nums) == 2:
            a, b = nums[0], nums[1]
            if flag:
                res = set([round(a + b, 5), round(a - b, 5), round(b - a, 5), round(a * b, 5)])
            else:
                res = set([a + b, a - b, b - a, a * b])
            if a != 0:
                if flag:
                    res.add(round(float(b) / a, 5))
                else:
                    res.add(float(b) / a)
            if b != 0:
                if flag:
                    res.add(round(float(a) / b, 5))
                else:
                    res.add(float(a) / b)
            return res
        if len(nums) == 3:
            res = set()
            divide = [(0, 1, 2), (1, 0, 2), (2, 0, 1)]
            for d in divide:
                a, s = nums[d[0]], self.calculate([nums[d[1]], nums[d[2]]], 0)
                for b in s:
                    res |= self.calculate([a, b], 0)
            return res
        
        
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        divide = [([0], [1, 2, 3]), ([1], [0, 2, 3]), ([2], [0, 1, 3]), ([3], [0, 1, 2]), ([0, 1], [2, 3]), ([0, 2], [1, 3]), ([0, 3], [1, 2])]
        for d in divide:
            s1 = self.calculate([nums[i] for i in d[0]], 0)
            s2 = self.calculate([nums[i] for i in d[1]], 0)
            for a in s1:
                for b in s2:
                    s |= self.calculate([a, b], 1)
                    if 24 in s:
                        return True
        return False
            
        