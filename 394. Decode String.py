class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        stack = [res]
        digits = set(list('123456789'))
        brackets = set(['[', ']'])
        i = 0
        while i < len(s):
            if s[i] not in digits and s[i] not in brackets:
                stack[-1] += s[i]
            elif s[i] in digits:
                stack.append('')
                while s[i] != '[':
                    stack[-1] += s[i]
                    i += 1
                stack.append('')
            elif s[i] == ']':
                string = stack.pop()
                num = int(stack.pop())
                stack[-1] += string * num
            i += 1
        return stack[-1]
        