class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        pairs.sort(key = lambda x: x[1])
        tail = pairs[0][1]
        res = 1
        for pair in pairs[1:]:
            if pair[0] > tail:
                tail = pair[1]
                res += 1
        return res