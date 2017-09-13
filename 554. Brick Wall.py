import collections

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges = []
        for i in xrange(len(wall)):
            edge = 0
            for j in xrange(len(wall[i]) - 1):
                edge += wall[i][j]
                edges.append(edge)
        c = collections.Counter(edges)
        if len(c) == 0:
            return len(wall)
        return len(wall) - max(c.values())