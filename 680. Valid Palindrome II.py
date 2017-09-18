class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                delete_left = s[left + 1:right + 1]
                delete_right = s[left:right]
                if delete_left != delete_left[::-1] and delete_right != delete_right[::-1]:
                    return False
                return True
            left += 1
            right -= 1
        return True