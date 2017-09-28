class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        mark = ''.join(map(unichr, range(n + 1)))
        for u, v in edges:
            if mark[u] == mark[v]:
                return [u, v]
            new_mark = mark.replace(mark[u], mark[v])
            del mark
            mark = new_mark
        return None