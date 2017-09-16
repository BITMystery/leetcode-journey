class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        pattern = list(pattern)
        if len(words) != len(pattern):
            return False
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))