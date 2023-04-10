# leet code
# two sums
# input :list =[2,7,8,5] and target = 9 ,output =[0,1]

class Solution:
    def two_sums(*x,target):
        nums =[]
        result =[]
        for i in x:
            nums.append(i)
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target :
                    result.append(i)
                    result.append(j)
                    print(result)





s1 = Solution()
s1.two_sums(2,7,8,5,target=9)


