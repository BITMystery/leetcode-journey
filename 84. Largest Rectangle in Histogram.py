class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        i = 0
        while i < len(heights):
            if stack == [] or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                j = stack.pop()
                height = heights[j]
                width = i if stack == [] else i - stack[-1] - 1
                area = height * width
                res = max(res, area)
        while stack:
            j = stack.pop()
            height = heights[j]
            width = i if stack == [] else i - stack[-1] - 1
            area = height * width
            res = max(res, area)
        return res