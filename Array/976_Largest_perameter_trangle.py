"""

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106

"""

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:

        def quick_sort(nums):

            if len(nums) <= 1:
                return nums

            pivot = nums[-1]

            left = []
            right = []

            for i in range(len(nums)-1):

                if nums[i] < nums[i+1]:
                    left.append(nums[i])

                else:
                    right.append(nums[i])

            return quick_sort(left) + [pivot] + quick_sort(right)

        nums = quick_sort(nums)

        for i in range(len(nums)-2):

            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]

            if b + c > a:
                return a+ b + c

        return 0

a1 =Solution()
print(a1.largestPerimeter([2,1,2]))


