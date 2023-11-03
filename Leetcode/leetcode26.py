#Get Majority element

#Soution is correct failed due to time exceeded.
"""def majorityElement(nums):
    ans = {}
    for i in nums:
        ans[i] = nums.count(i)
    print(ans)
    Keymax = max(ans, key=lambda x : ans[x])
    return Keymax"""

#Solution is correct failed due to memory limit exceeded
"""
def majorityElement(nums):
    max_num=max(nums)+1
    ans = [0]*max_num
    for i in nums:
        ans[i]+=1
    return  ans.index(max(ans))"""

#Solution Passed
def majorityElement( nums):
    if len(nums) < 100:
        ans = {}
        for i in nums:
            ans[i] = nums.count(i)
        Keymax = max(ans, key=lambda x: ans[x])
        return Keymax
    else:
        max_num = max(nums) + 1
        ans = [0] * max_num
        for i in nums:
            ans[i] += 1
        return ans.index(max(ans))

nums=[1,1,3,4,4,4,2,2]
s=majorityElement(nums)
print(s)
