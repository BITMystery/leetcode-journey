class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        letters = set(s)
        i = len(s) - 1
        while letters:
            if s[i] in letters:
                letters.remove(s[i])
            i -= 1
        min_letter, min_index = 'z', -1
        for j in xrange(i + 2):
            if s[j] < min_letter:
                min_letter = s[j]
                min_index = j
        return min_letter + self.removeDuplicateLetters(s[min_index + 1:].replace(min_letter, ''))