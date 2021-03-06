class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        parenthesis_positions = []
        wildcard_positions = []
        for i in xrange(len(s)):
            if s[i] == '(':
                parenthesis_positions.append(i)
            elif s[i] == '*':
                wildcard_positions.append(i)
            else:
                if parenthesis_positions:
                    parenthesis_positions.pop()
                elif wildcard_positions:
                    wildcard_positions.pop()
                else:
                    return False
        while parenthesis_positions:
            if not wildcard_positions:
                return False
            p = parenthesis_positions.pop()
            w = wildcard_positions.pop()
            if p > w:
                return False
        return True
