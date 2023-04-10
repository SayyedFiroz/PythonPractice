class Solution(object):
    def vowelStrings(self, words, left, right):
        vowel = "aeiou"
        output = 0
        for i in range(left, right + 1):
            if words[i][0] in vowel and words[i][-1] in vowel:
                output += 1
        return output


s1 = Solution()

words = ["hey","aeo","mu","ooo","artro"]
left = 1;right = 4
result = s1.vowelStrings(words,left,right)
print("this is rrsult",result)