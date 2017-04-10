class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = int(area ** 0.5)
        if L * L == area:
        	return [L, L]
        L += 1
        while area % L:
        	L += 1
        W = area / L
        return [L, W]

class Solution_2(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #Better than Solution#1. Note that loop [1, sqrt(area)] is much less than [sqrt(area), area].
        W = int(area ** 0.5)
        while area % W:
        	W -= 1
        L = area / W
        return [L, W]


s = Solution()
print s.constructRectangle(115)