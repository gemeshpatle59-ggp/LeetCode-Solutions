"""

class Solution:
    def sortSentence(self, s: str) -> str:
        hash_map = {}
        ints = set("1234567890")
        temp = ""
        original_sen = ""
        t = 0
        space = 0
        for i in s:
            if i == " ":
                space += 1
            elif i in ints:
                hash_map[int(i)] = temp
                t += 1
                temp = ""
            else:
                temp += i

        sp = 0

        for i in range(1,t+1):
            if i in hash_map:
                original_sen += hash_map[i]
                if sp < space:
                    original_sen += " "
                    sp += 1


        return original_sen



a1 = Solution()
print(a1.sortSentence("is2 sentence4 This1 a3"))

"""

class Solution:
    def sortSentence(self, s: str) -> str:
        hash_map = {}
        ints = set("1234567890")
        temp = ""
        original_sen = ""
        t = 0
        space = 0
        for i in s:
            if i == " ":
                space += 1
            elif i in ints:
                hash_map[int(i)] = temp
                t += 1
                temp = ""
            else:
                temp += i

        sp = 0

        for i in range(1,t+1):
            if i in hash_map:
                original_sen += hash_map[i]
                if sp < space:
                    original_sen += " "
                    sp += 1


        return original_sen



a1 = Solution()
print(a1.sortSentence("is2 sentence4 This1 a3"))