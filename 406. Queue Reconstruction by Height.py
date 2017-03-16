class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #Idea: Greedy. Process tallest guy (if with same height then sort by k), then 2nd tallest guy, ....
        #Note that inserting a shorter guy won't affect the correctness of insertions of other taller guys, not vise versa. That's why we start from the tallest guy.
        #This solution using linked list to handle insertions.
        r = []
        if not people:
        	return r
        people.sort(key = lambda x: (x[0], -x[1]), reverse = True)
        people[0] = [people[0][0], people[0][1], None]
        head = 0
        for i in xrange(1, len(people)):
        	[h, k] = people[i]
        	if k == 0:
        		people[i] = [h, k, head]
        		head = i
        	else:
        		p = head
        		for j in xrange(k-1):
        			p = people[p][2]
        		people[i] = [people[i][0], people[i][1], people[p][2]]
        		people[p][2] = i
        p = head
        while p != None:
        	r.append(people[p][:2])
        	p = people[p][2]
        return r

class Solution_2(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #Same idea with solution#1, but uses list insert() to do insertions.
        r = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for guy in people:
        	r.insert(guy[1], guy)
        return r

s = Solution_2()
print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])