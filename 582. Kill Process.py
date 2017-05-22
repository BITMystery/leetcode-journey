class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = {}
        for i in xrange(len(ppid)):
            if ppid[i] in d:
                d[ppid[i]] += [pid[i]]
            else:
                d[ppid[i]] = [pid[i]]
        res = []
        stack = [kill]
        while stack:
            k = stack.pop()
            res += [k]
            if k in d:
                stack += d[k]
        return res

s = Solution()
print s.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)