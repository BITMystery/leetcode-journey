class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        #Classic method
        r = [-1] * len(findNums)
        index = {}
        for i in range(len(nums)):
        	index[nums[i]] = i
        for i in range(len(findNums)):
        	j = index[findNums[i]]
        	for num in nums[j+1:]:
        		if findNums[i] < num:
        			r[i] = num
        			break
        return r

class Solution_2(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        #Method using stack
        r = [-1] * len(findNums)
        index = {}
        stack = []
        for num in nums:
        	while stack and stack[-1] < num:
        		smaller_num = stack.pop()
        		index[smaller_num] = num
        	stack.append(num)
        for i in range(len(findNums)):
        	r[i] = index.get(findNums[i], -1)
        return r

s = Solution_2()
print s.nextGreaterElement([4,1,2], [1,3,4,2])