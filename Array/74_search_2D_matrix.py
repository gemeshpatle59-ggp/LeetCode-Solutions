"""

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""

class Solution:
    def searchMatrix(self, matrix , target):

        l = 0
        r = len(matrix) - 1

        # Find the correct row
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break

            elif target < matrix[mid][0]:
                r = mid - 1

            else:
                l = mid + 1

        if l > r:
            return False

        # Binary search inside the row
        row = matrix[mid]

        l = 0
        r = len(row) - 1

        while l <= r:
            mid2 = (l + r) // 2

            if row[mid2] == target:
                return True

            elif row[mid2] < target:
                l = mid2 + 1

            else:
                r = mid2 - 1

        return False

a1 = Solution()
print(a1.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))