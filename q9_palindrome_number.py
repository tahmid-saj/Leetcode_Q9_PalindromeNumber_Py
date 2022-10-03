class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        rev = 0
        tmp_x = x
        
        while tmp_x > 0:
            rev = rev * 10
            rev += tmp_x % 10
            tmp_x /= 10
        
        if x != rev:
            return False
        
        return True