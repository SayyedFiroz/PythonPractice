string="anagram"
string1="nagarama"

def anagram(string,string1):
    if string==string1:
        return True
    else:
        string=''.join(sorted(string))
        string1=''.join(sorted(string1))

        if string==string1:
            return True
        else:
            return False

r=anagram(string,string1)
print(r)


class Solution(object):
    def isAnagram(self, s, t):
        if s==t:
            return True
        else:
            s= ''.join(sorted(s))
            t= ''.join(sorted(t))
            if s == t:
                return True
            else:
                return False

s=Solution()
r=s.isAnagram(string,string1)
print(r)