import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.index = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.values.append(val)
        if val not in self.index:
            self.index[val] = [len(self.values) - 1]
            return True
        self.index[val].append(len(self.values) - 1)
        return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        if self.index[val][-1] != len(self.values) - 1:
            self.values[self.index[val][-1]], self.values[-1] = self.values[-1], self.values[self.index[val][-1]]
            self.index[self.values[self.index[val][-1]]][-1] = self.index[val][-1]
        del self.values[-1]
        del self.index[val][-1]
        if len(self.index[val]) == 0:
            del self.index[val]
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if len(self.values) == 0:
            return False
        return self.values[random.randint(0, len(self.values) - 1)]


obj = RandomizedCollection()
obj.insert(1)
print obj.values, obj.index
obj.insert(1)
print obj.values, obj.index
obj.insert(2)
print obj.values, obj.index
obj.insert(2)
print obj.values, obj.index
obj.insert(2)
print obj.values, obj.index
obj.remove(1)
print obj.values, obj.index
obj.remove(1)
print obj.values, obj.index
obj.remove(2)
print obj.values, obj.index
obj.insert(1)
print obj.values, obj.index
obj.remove(2)