class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = [str(i) for i in range(1, n + 1)]
        i = 3
        while(i <= n):
        	r[i - 1] = 'Fizz'
        	i += 3
        i = 5
        while(i <= n):
        	if i % 3 == 0:
        		r[i - 1] += 'Buzz'
        	else:
        		r[i - 1] = 'Buzz'
        	i += 5
        return r

class Solution_2(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #Cleaner than solution#1, but slower!
        r = ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range (1, n + 1)]
        return r


s = Solution_2()
print s.fizzBuzz(15)