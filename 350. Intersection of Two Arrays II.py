from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c = Counter(nums1) & Counter(nums2)
        res = []
        for num in c:
            res += [num] * c[num]
        return res