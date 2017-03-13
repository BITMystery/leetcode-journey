class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = []
        line1 = 'qwertyuiop'
        line2 = 'asdfghjkl'
        line3 = 'zxcvbnm'
        D = {}
        for letter in line1:
        	D[letter] = 1
        for letter in line2:
        	D[letter] = 2
        for letter in line3:
        	D[letter] = 3
        for word in words:
        	lower_word = word.lower()
        	flag = 1
        	for letter in lower_word[1:]:
        		if D[letter] != D[lower_word[0]]:
        			flag = 0
        			break
        	if flag:
        		r.append(word)
        return r

class Solution_2(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = []
        check_list = [2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3]
        for word in words:
        	lower_word = word.lower()
        	flag = 1
        	for letter in lower_word[1:]:
        		if check_list[ord(letter) - 97] != check_list[ord(lower_word[0]) - 97]:
        			flag = 0
        			break
        	if flag:
        		r.append(word)
        return r

s = Solution_2()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])
