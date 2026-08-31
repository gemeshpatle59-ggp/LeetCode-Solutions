"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 
Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

class Solution:
    def setzero(self,matrix):
        row = len(matrix)
        clom = len(matrix[0])

        row_track = [0 for _ in range(row)]
        clom_track = [0 for _ in range(clom)]

        for i in range(row):
            for j in range(clom):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    clom_track[j] = -1

        for i in range(row):
            for j in range(clom):
                if row_track[i] == -1 or clom_track[j] == -1:
                    matrix[i][j] = 0

a1 = Solution()
a1.setzero(matrix)
print(matrix)               
