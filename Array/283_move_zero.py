"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

"""


num = [0,1,0,3,12]

def move(num):
    n = len(num)

    for i in range(n):
        if num[i] == 0:
            for j in range(i+1,n):
                if num[j] != 0:
                    num[i],num[j] = num[j],num[i]
                    break


move(num)
print(num)                    