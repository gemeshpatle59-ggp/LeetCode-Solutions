"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def isPalindrome(self, x):
        n = x
        new_num = 0
        if x < 0:
            return False
        while n > 0:
            last_digit = n % 10
            new_num = (new_num * 10) + last_digit
            n = n // 10
        
        return new_num == x

a1 = Solution()
print(a1.isPalindrome(121))