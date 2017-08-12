class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        l = preorder.split(',')
        stack = [1]
        for i in xrange(len(l)):
            if l[i] != '#':
                stack.append(0)
            else:
                stack[-1] += 1
                while stack and stack[-1] == 2:
                    stack.pop()
                    if not stack:
                        if i != len(l) - 1:
                            return False
                        else:
                            return True
                    stack[-1] += 1
        if stack:
            return False
        return True