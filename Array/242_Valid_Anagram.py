"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_map = {}

        for i in s:
            if i in hash_map:
                hash_map[i] += 1

            else:
                hash_map[i] = 1

        for j in t:
            if j in hash_map:
                hash_map[j] -= 1

        for _ , value in hash_map.items():

            if value != 0:
                return False
        return True

a1 = Solution()
print(a1.isAnagram("rat" , "cat"))