class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = cows = 0
        secret, guess = list(secret), list(guess)
        counter = {}
        for d in secret:
            counter[d] = counter.get(d, 0) + 1
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            if counter.get(guess[i], 0) > 0:
                cows += 1
                counter[guess[i]] -= 1
        return str(bulls) + 'A' + str(cows - bulls) + 'B'