class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fuzzy = {}
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.fuzzy[word] = 1
            for i in xrange(len(word)):
                fuzzy_word = word[:i] + '*' + word[i + 1:]
                self.fuzzy[fuzzy_word] = self.fuzzy.get(fuzzy_word, 0) + 1
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        flag = 1 if word in self.fuzzy else 0
        for i in xrange(len(word)):
            fuzzy_word = word[:i] + '*' + word[i + 1:]
            if flag and self.fuzzy.get(fuzzy_word, 0) > 1:
                return True
            if not flag and fuzzy_word in self.fuzzy:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)