
def isValid(s):
    stack=[]
    op = dict(('()', '[]', '{}'))
    for i in s:
        if i in '({[':
            stack.append(i)
        elif len(stack)==0 or i !=op[stack.pop()]:
            return False

    return len(stack) ==0


s="{[]}"
result = isValid(s)
print(result)


# created by own passed 70 test case but 23 failed



