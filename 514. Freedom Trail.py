class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        index = {}
        for i in xrange(len(ring)):
            if ring[i] in index:
                index[ring[i]].append(i)
            else:
                index[ring[i]] = [i]
        
        options = [(0, 0)] # start = [(start index 1, min steps 1), ...]
        for letter in key:
            new_options = []
            for end in index[letter]:
                min_steps = float('inf')
                for start, steps in options:
                    new_steps = steps + min(abs(end - start), len(ring) - abs(end - start))
                    min_steps = min(min_steps, new_steps)
                new_options.append((end, min_steps))
            del options
            options = new_options
        
        return min([steps for start, steps in options]) + len(key)