class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        i = 0
        flag = False
        while strs:
            for j in xrange(len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    flag = True
                    break
            if flag:
                break
            res += strs[0][i]
            i += 1
        return res
        
        