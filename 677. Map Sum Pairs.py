class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}
        self.index = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key not in self.words:
            for i in xrange(len(key) + 1):
                self.index[key[:i]] = self.index.get(key[:i], 0) + val
        else:
            for i in xrange(len(key) + 1):
                self.index[key[:i]] += val - self.words[key]
        self.words[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.index.get(prefix, 0)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)