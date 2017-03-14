class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #Idea: It turns to be a loop once a number reaches 2 ** N (N >= 0)
        r = [0]
        count = 0
        for i in range(1, num + 1):
        	m = 2 ** count
        	if i == m:
        		r.append(1)
        		count += 1
        	else:
        		r.append(1 + r[i - m / 2])
        return r

class Solution_2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #Idea: Same idea as solution#1, just avoid r.append for faster execution.
        r = [0] * (num + 1)
        count = 0
        for i in range(1, num + 1):
            m = 2 ** count
            if i == m:
                r[i] = 1
                count += 1
            else:
                r[i] = (1 + r[i - m / 2])
        return r

s = Solution_2()
print s.countBits(10)