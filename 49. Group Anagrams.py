class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        row = 0
        index = {}
        res = []
        for word in strs:
            s = ''.join(sorted(word))
            if s not in index:
                index[s] = row
                res.append([word])
                row += 1
            else:
                res[index[s]].append(word)
        return res
        