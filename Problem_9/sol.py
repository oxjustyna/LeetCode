class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        n = len(x)

        for i in range(n):
            if x[i] != x[n-i -1]:
                return False
                break

        return True
