"""def romanToInt(s):
    roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    n = len(s)

    num = roman_int[s[n - 1]]

    for i in range(n - 2, -1, -1):

        if roman_int[s[i]] >= roman_int[s[i + 1]]:
            num += roman_int[s[i]]
        else:
            num -= roman_int[s[i]]

    print(num)


romanToInt("VIV")
"""


class Solution(object):
    def romanToInt(self, s):
        self.s = ''

        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        n = len(s)

        num = roman_map[s[n - 1]]

        for i in range(n - 2, -1, -1):
            if roman_map[s[i]] >= roman_map[s[i + 1]]:
                num += roman_map[s[i]]
            else:
                num -= roman_map[s[i]]

        return num


s1 = Solution()
num = s1.romanToInt(s="VIV")
print(num)