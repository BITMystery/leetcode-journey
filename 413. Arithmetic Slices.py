class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
        	return 0
        r = 0
        count = 0
        last_num = A[1]
        gap = A[1] - A[0]
        for num in A[2:]:
        	if num - last_num == gap:
        		count += 1
        	elif count:
        		r += count * (count + 1) / 2
        		gap = num - last_num
        		count = 0
        	else:
        		gap = num - last_num
        	last_num = num
        if count:
        	r += count * (count + 1) / 2
        return r

class Solution_2(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Polish the code of solution#1
        i = 2
        r = 0
        count = 0
        while i < len(A):
        	if A[i] - A[i-1] == A[i-1] - A[i-2]:
        		count += 1
        		r += count
        	else:
        		count = 0
        	i += 1
        return r

s = Solution_2()
print s.numberOfArithmeticSlices([1, 2, 3, 4, 5, 0, 2, 4])