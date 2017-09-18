class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        if n == 3:
            return 1
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in xrange(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i::i] = [False] * len(primes[i * i::i])
        return sum(primes)