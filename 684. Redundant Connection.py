class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        union_mark = ''.join(map(unichr, range(n + 1)))
        for u, v in edges:
            if union_mark[u] == union_mark[v]:
                return [u, v]
            new_union_mark = union_mark.replace(union_mark[u], union_mark[v])
            del union_mark
            union_mark = new_union_mark
        return None
