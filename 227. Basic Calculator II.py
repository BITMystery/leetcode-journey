class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        nums = set('1234567890')
        l = []
        i = 0
        # calculate all * and /
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in nums:
                j = i + 1
                while j < len(s) and s[j] in nums:
                    j += 1
                l.append(int(s[i:j]))
                i = j
            else:
                if s[i] == '+' or s[i] == '-':
                    l.append(s[i])
                    i += 1
                else:
                    op = s[i]
                    i += 1
                    while s[i] == ' ':
                        i += 1
                    j = i + 1
                    while j < len(s) and s[j] in nums:
                        j += 1
                    num = int(s[i:j])
                    l[-1] = l[-1] * num if op == '*' else l[-1] / num
                    i = j
        res = l[0]
        i = 1
        while i < len(l):
            res = res + l[i + 1] if l[i] == '+' else res - l[i + 1]
            i += 2
        return res