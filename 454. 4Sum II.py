import collections

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #Idea: Transform 4Sum problem to 2Sum problem. That is, calculate all A + B results as a group X,
        #and calculate all C + D results as a group Y. Then find X + Y = 0.
        #Time complexity: O(n^2)
        X = collections.Counter(a + b for a in A for b in B)
        return sum(X[-c-d] for c in C for d in D)

s = Solution()
print s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2])