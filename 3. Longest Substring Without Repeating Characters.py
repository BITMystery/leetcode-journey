class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = right = 0
        seen = set()
        while right < len(s):
            if s[right] in seen: # invalid answer
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1 # make it valid
            else: # valid answer
                seen.add(s[right])
                res = max(res, right - left + 1)
            right += 1
        return res
                        