"""

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        hash_map = {}
        ans = set()

        for i in range(len(nums1)):
            if nums1[1] in hash_map:
                hash_map[nums1[i]] += 1

            else:
                hash_map[nums1[i]] = 1

        for j in range(len(nums2)):
            if nums2[j] in hash_map:
                ans.add(nums2[j])


        return list(ans)

a1 = Solution()
print(a1.intersection([1,2,2,1] , [2,2]))
