from collections import Counter
import sys


class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        target_counter = Counter(target)
        sticker_counters = [Counter(sticker) for sticker in stickers]
        sticker_counters_sum = sum(sticker_counters, Counter())
        
        for letter in target_counter.keys():
            if letter not in sticker_counters_sum:
                return -1
        
        dp = {}
        dp[''] = 0
        
        def helper(target, sticker_counters, dp):
            if target in dp:
                return dp[target]
            target_counter = Counter(target)
            min_num = sys.maxint
            for sticker_counter in sticker_counters:
                # Optimization: explicitly require next sticker has target[0]
                if target[0] not in sticker_counter:
                    continue  
                rest_counter = target_counter - sticker_counter
                rest = ''.join([chr(i) * rest_counter[chr(i)] for i in xrange(ord('a'), ord('z') + 1) if chr(i) in rest_counter])
                if len(target) == len(rest):
                    continue
                num = helper(rest, sticker_counters, dp) + 1
                min_num = min(min_num, num)
            dp[target] = min_num
            return min_num
        
        return helper(target, sticker_counters, dp)   