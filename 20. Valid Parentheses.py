class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack == []:
                    return False
                pair = stack.pop() + c
                if pair != '()' and pair != '[]' and pair != '{}':
                    return False
        return True if stack == [] else False