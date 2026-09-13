"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        num = 0

        while n > 0:
            last_digit = n % 10
            num = (num * 10) + last_digit
            n = n // 10

        if x < 0:
            num = -num

        if num < -2147483648 or num > 2147483647:
            return 0

        return num
a1 = Solution()
print(a1.reverse(987))