class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if sentence == '':
            return ''
        max_root_len = max([len(word) for word in dict])
        roots = set(dict)
        res = []
        words = sentence.split()
        for word in words:
            for i in xrange(min(len(word), max_root_len)):
                if word[:i + 1] in roots:
                    res.append(word[:i + 1])
                    break
            else:
                res.append(word)
        return ' '.join(res)