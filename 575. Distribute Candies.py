class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy_set = set(candies)
        return min(len(candies) / 2, len(candy_set))