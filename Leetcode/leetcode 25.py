def plusOne(digits):
    string = ""
    for i in digits:
        string +=str(i)

    string=str(int(string)+1)
    ans=[]
    for i in string:
        ans.append(int(i))
    print(ans)


plusOne(digits=[1, 2, 3])
