class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        a = list(a)
        b = list(b)
        carry = 0
        for i in xrange(len(b)):
            s = int(a[-i - 1]) + int(b[-i - 1]) + carry
            carry = s / 2
            s %= 2
            a[-i - 1] = str(s)
        if carry == 0:
            return ''.join(a)
        elif len(a) == len(b):
            return '1' + ''.join(a)
        else:
            return self.addBinary(a[:len(a)-len(b)], '1') + ''.join(a[len(a)-len(b):])