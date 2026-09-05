"""

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
 



"""

class Solution:
    def detectCapitalUse(self, word):

        is_uppercase = 0
        is_lowercase = 0
        is_capital = False

        for i in word:
            if 65 <= ord(i) <= 90:
                is_uppercase += 1

            elif 97 <= ord(i) <= 122:
                is_lowercase += 1

        for j in word[1:]:
            if 65 <= ord(word[0]) <= 90 and 97 <= ord(j) <= 122:
                is_capital = True
            else:
                is_capital = False
                break

        if is_uppercase == len(word) or is_lowercase == len(word) or is_capital :
            return True
        else:
            return False

a1 = Solution()

print(a1.detectCapitalUse("LLL"))
