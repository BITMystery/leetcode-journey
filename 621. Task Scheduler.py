import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if None == tasks or len(tasks) == 0:
            return 0
        freq_table = collections.Counter(tasks)
        freq_list = sorted(freq_table.values(), reverse = True)
        max_freq = freq_list[0]
        ctr = 0 #number of tasks whose frequency is max_freq
        for i in xrange(len(freq_list)):
            if freq_list[i] != max_freq:
                break
            freq_list[i] = 0
            ctr += 1
        #Step 1: Arrange tasks with max_freq into chunks.
        #E.g. [A, A, A, B, B, B, C, C, D, D, E, E] -> |ABXX|ABXX|AB, chunk size = n + 1.
        res = (max_freq - 1) * (n + 1) + ctr
        #Step 2: Arrange rest tasks into unused intervals.
        #|ABCD|ABCD|AB
        #Step 3: If intervals are not enough, extend chunks
        #|ABCDE|ABCDE|AB
        unused_num = res - max_freq * ctr
        rest_num = sum(freq_list)
        return res + max(0, rest_num - unused_num)
            