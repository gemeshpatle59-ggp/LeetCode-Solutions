"""

You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

Example 2:

Input: nums = [2,0,1]

Output: [0,1,2]

Explanation:

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

"""

class Solution:
    def sortcolour(self , nums):

        zero = 0
        one = 0
        two = 0

        for num in nums:
            if num == 0:
                zero += 1

            elif num == 1:
                one += 1

            else:
                two += 1

        i = 0

        for _ in range(zero):
            nums[i] = 0
            i += 1

        for _ in range(one):
            nums[i] = 1
            i += 1

        for _ in range(two):
            nums[i] = 2
            i += 1

nums = [2,0,2,1,1,0]

a1 = Solution()
a1.sortcolour(nums)

print(nums)