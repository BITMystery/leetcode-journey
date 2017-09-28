class Solution(object):
    next_closest_time = ''
    min_gap = 1441
    
    def is_valid_time(self, time):
        if time[0]*10 + time[1] >= 24 or time[2]*10 + time[3] >= 60:
            return False
        return True
    
    def dfs(self, time, digits, path):
        if len(path) == 4:
            if not self.is_valid_time(path):
                return None
            new_time = (path[0]*10 + path[1]) * 60 + path[2]*10 + path[3]
            gap = new_time - time if new_time > time else 1440 - (time-new_time) 
            if gap < self.min_gap:
                self.min_gap = gap
                h1, h2, m1, m2 = str(path[0]), str(path[1]), str(path[2]), str(path[3])
                self.next_closest_time = '%s%s:%s%s' % (h1, h2, m1, m2)
            return None
        for d in digits:
            self.dfs(time, digits, path + [d])
        return None
        
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h1, h2, m1, m2 = int(time[0]), int(time[1]), int(time[3]), int(time[4])
        digits = set([h1, h2, m1, m2])
        time = (h1*10 + h2) * 60 + m1*10 + m2
        self.dfs(time, digits, [])
        return self.next_closest_time