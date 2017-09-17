from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        tasks = Counter(p)
        res = []
        for i in xrange(len(s)):
            tasks[s[i]] -= 1
            if tasks[s[i]] == 0:
                del tasks[s[i]]
            if i - len(p) >= 0:
                tasks[s[i - len(p)]] += 1
                if tasks[s[i - len(p)]] == 0:
                    del tasks[s[i - len(p)]]
            if not tasks:
                res.append(i - len(p) + 1)
        return res
