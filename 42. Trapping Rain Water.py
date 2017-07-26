class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height) - 1
        max_left = max_right = 0
        while left <= right:
            if max_left <= max_right:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1
        return res