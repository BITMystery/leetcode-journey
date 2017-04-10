class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Idea: Xor all 2 ** num for num in nums. The result will contains two bits equal to 1 (and others equal to 0). Then find the position of the two bits.
        #Notes: if a num is negative, reverse it first.
        #Issue: can't deal with large numbers.
        r = []
        xor = 0
        for num in nums:
        	xor ^= 2 ** abs(num)
        count = 0
        while xor:
        	if xor & 1 == 1:
        		print xor
        		l = len([nums.index(num) for num in nums if num == count])
        		if l == 1:
        			r.append(count)
        		else:
        			r.append(-count)
        		if len(r) == 2:
        			break
        	xor >>= 1
        	count += 1
        return r

class Solution_2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Idea: Xor all nums, and the result equals to the xor of the two numbers we need to find.
        #Since the two numbers are distinct, their xor result must has one bit equails to 1. Record its position.
        #Then divide nums into two groups according to whether thebit at the recorded position equails to 1.
        #The two single numbers must be in different group. Xor each group to find the single number, respectively.
        xor = 0
        for num in nums:
        	xor ^= num
        count = 1
        while True:
        	if xor & count:
        		break
        	count <<= 1
        xor_1 = xor_2 = 0
        for num in nums:
        	if num & count:
        		xor_1 ^= num
        	else:
        		xor_2 ^= num
        return [xor_1, xor_2]

s = Solution_2()
print s.singleNumber([1, 2, 1, -3, 2, 5])
        			