import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        index = {}
        for letter in magazine:
        	if index.get(letter, None) != None:
        		index[letter] += 1
        	else:
        		index[letter] = 1
        for letter in ransomNote:
        	if index.get(letter, None) > 0:
        		index[letter] -= 1
        	else:
        		return False
        return True

class Solution_2(object):
    def canConstruct(self, ransonNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #Using built-in function collections.Counter(). Solution#2 is lower than solution#1 because solution#1 returns False once detected while solution#2 detects all letters.
        return not collections.Counter(ransonNote) - collections.Counter(magazine)

s = Solution_2()
print s.canConstruct("aaabbc", "aaaabb")