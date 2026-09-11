"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1

            if cut1 > 0:
                left1 = nums1[cut1 - 1]
            else:
                left1 = float("-inf")

            if cut1 < m:
                right1 = nums1[cut1]
            else:
                right1 = float("inf")

            if cut2 > 0:
                left2 = nums2[cut2 - 1]
            else:
                left2 = float("-inf")

            if cut2 < n:
                right2 = nums2[cut2]
            else:
                right2 = float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                right = cut1 - 1

            else:
                left = cut1 + 1

a1 = Solution()
print(a1.findMedianSortedArrays([1,2] , [2]))