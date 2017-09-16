class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        res = []
        to_do = {}
        for letter in p:
            to_do[letter] = to_do.get(letter, 0) + 1
        for i in xrange(len(s)):
            to_do[s[i]] = to_do.get(s[i], 0) - 1
            if to_do[s[i]] == 0:
                del to_do[s[i]]
            if i > len(p) - 1:
                to_do[s[i - len(p)]] = to_do.get(s[i - len(p)], 0) + 1
                if to_do[s[i - len(p)]] == 0:
                    del to_do[s[i - len(p)]]
            if not to_do:
                res.append(i - len(p) + 1)
        return res