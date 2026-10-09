"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.


"""

class Solution:
    def longestcommonprefix(self , strs):

        prefix = strs[0]

        for i in range(1,len(strs)):
            while strs[i].find(prefix) != 0:

                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix

a1 = Solution()
print(a1.longestcommonprefix(["flower" , "flow" , "flight"]))