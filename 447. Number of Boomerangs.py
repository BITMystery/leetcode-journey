import collections

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for x1, y1 in points:
            c = collections.Counter([(x1 - x2) ** 2 + (y1 - y2) ** 2 for x2, y2 in points])
            for n in c.values():
                res += n * (n - 1)
            del c
        return res