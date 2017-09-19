from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_window = []
        left = right = 0
        counter = len(t)
        t = Counter(t)
        while right < len(s):
            if s[right] in t:
                t[s[right]] -= 1
                if t[s[right]] >= 0:
                    counter -= 1
            while counter == 0: # valid ans
                if not min_window or right - left < min_window[1] - min_window[0]:
                    min_window = [left, right]
                if s[left] in t:
                    t[s[left]] += 1
                    if t[s[left]] > 0:
                        counter += 1 # make it invalid
                left += 1
            right += 1
        if not min_window:
            return ''
        return s[min_window[0]:min_window[1] + 1]