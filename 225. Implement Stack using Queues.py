import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue.Queue()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        l = self.q.qsize()
        for _ in xrange(l - 1):
            v = self.q.get()
            self.q.put(v)
        return self.q.get()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        l = self.q.qsize()
        v = 0
        for _ in xrange(l):
            v = self.q.get()
            self.q.put(v)
        return v
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()