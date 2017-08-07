class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        for log in logs:
            function_id, start_or_end, timestamp = log.split(':')
            function_id = int(function_id)
            timestamp = int(timestamp)
            if start_or_end[0] == 's':
                stack.append([function_id, timestamp, 0])
            else:
                item = stack.pop()
                res[item[0]] += timestamp - item[1] - item[2] + 1
                if stack:
                    stack[-1][2] += timestamp - item[1] + 1
        return res