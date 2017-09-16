class Solution(object): #O(n) time O(n) space
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #papers[i] = m means there are m papers with citation i
        papers = [0] * (len(citations) + 1)
        n = len(citations)
        for c in citations:
            papers[c if c <= n else n] += 1
        h_index = n
        count = 0
        for p in papers[::-1]:
            count += p
            if count >= h_index:
                return h_index
            h_index -= 1

class Solution(object): #O(nlogn) time O(1) space
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        h_index = 0
        for i in xrange(len(citations)):
            if citations[i] <= i:
                break
            h_index += 1
        return h_index