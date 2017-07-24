class Solution(object):
    def transform(self, s, scale):
        index = {'I': 'IXCM', 'V': 'VLD'}
        return ''.join([index[s[i]][scale] for i in xrange(len(s))])
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        index = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}
        # num in digital form
        digitals = [0] * 4
        digitals[3] = num / 1000
        digitals[2] = num % 1000 / 100
        digitals[1] = num % 100 / 10
        digitals[0] = num % 10
        for i in xrange(4):
            if digitals[i] == 0:
                continue
            elif digitals[i] <= 5:
                res = self.transform(index[digitals[i]], i) + res
            elif digitals[i] <= 8:
                res = self.transform(index[5], i) + self.transform(index[digitals[i] - 5], i) + res
            else:
                res = self.transform(index[1], i) + self.transform(index[1], i + 1) + res
        return res