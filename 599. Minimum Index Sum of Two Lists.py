class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if len(list1) < len(list2):
            list1, list2 = list2, list1
        index = {}
        for i in xrange(len(list2)):
            index[list2[i]] = i
        res = []
        min_index_sum = float('inf')
        for i in xrange(len(list1)):
            if i > min_index_sum:
                break
            j = index.get(list1[i], -1)
            if j != -1:
                index_sum = i + j
                if not res:
                    res.append(list1[i])
                    min_index_sum = i + j
                elif index_sum == min_index_sum:
                    res.append(list1[i])
                elif index_sum < min_index_sum:
                    while res:
                        res.pop()
                    res.append(list1[i])
                    min_index_sum = index_sum
        return res