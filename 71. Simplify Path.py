class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = [e for e in path.split('/') if e != '' and e != '.']
        stack = []
        for e in l:
            if e == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(e)
        return '/' + '/'.join(stack)