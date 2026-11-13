"""
You are given two strings s1 and s2 of the same length.

A mismatched segment is a maximal contiguous range of indices where the characters of s1 and s2 differ at every index.

Return a 2D array containing [sub1, sub2] for each mismatched segment, where sub1 and sub2 are the corresponding substrings from s1 and s2, respectively. Return the segments in increasing order of their starting indices. If there are no mismatched segments, return an empty array.

 

Example 1:

Input: s1 = "earth", s2 = "empty"

Output: [["ar","mp"],["h","y"]]

Explanation:

The characters at indices 1 and 2 differ, forming the mismatched segment ["ar","mp"].
The characters at index 4 differ, forming the mismatched segment ["h","y"].
Example 2:

Input: s1 = "action", s2 = "nation"

Output: [["ac","na"]]

Explanation:

The characters at indices 0 and 1 differ, forming the mismatched segment ["ac","na"]. All remaining characters are equal in both strings.

Example 3:

Input: s1 = "hot", s2 = "hot"

Output: []

Explanation:

The two strings are identical, so there are no mismatched segments.

 

Constraints:

1 <= s1.length == s2.length <= 100
s1 and s2 consist of lowercase English letters.

"""

class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        result = []
        i = 0
        n = len(s1)

        while i < n:

            if s1[i] != s2[i]:

                start = i

                while i < n and s1[i] != s2[i]:
                    i += 1

                sub1 = s1[start:i]
                sub2 = s2[start:i]

                result.append([sub1, sub2])

            else:
                i += 1

        return result

a1 = Solution()
print(a1.findMismatchedSegments("earth", "empty"))