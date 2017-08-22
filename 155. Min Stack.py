class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_val == None or x < self.min_val:
            self.min_val = x
        

    def pop(self):
        """
        :rtype: void
        """
        val = self.stack.pop()
        if val == self.min_val:
            self.min_val = None
            for val in self.stack:
                if self.min_val == None or val < self.min_val:
                    self.min_val = val
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()