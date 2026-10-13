"""

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

"""

class Solution:
    def findDisappearedNumber(self , nums):

        hash_set = set()
        ans = []

        for i in nums:
            hash_set.add(i)


        for j in range(1 , len(nums)+1):
            if j not in hash_set:
                ans.append(j)

        return ans

a1 = Solution()
print(a1.findDisappearedNumber([4,3,2,7,8,2,3,1]))