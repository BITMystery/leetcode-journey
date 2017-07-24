class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        [p, q] = a.split('+')
        [r, s] = b.split('+')
        p = int(p)
        q = int(q[: len(q) - 1])
        r = int(r)
        s = int(s[: len(s) - 1])
        x = p * r - q * s
        y = r * q + p * s
        return str(x) + '+' + str(y) + 'i'