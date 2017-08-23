class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        final_len = len(num) - k
        for d in num:
            while k and stack and d < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(d)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int(''.join(stack)))