class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [1] + [0] * n
        i = 0
        j = 1
        while j < n:
        	if S[i] == 1:
        		S[j] = 3 - S[j-1]
        		i += 1
        		j += 1
        	else:
        		S[j] = S[j-1]
        		S[j+1] = 3 - S[j-1]
        		i += 1
        		j += 2
        S[n] = 2
        return 2 * (n + 1) - sum(S)

s = Solution()
print s.magicalString(6)
