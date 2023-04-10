class Solution:
    def twoSum(self,nums,target):
        self.nums = []
        self.target = target
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

s1 = Solution()
nums = [2,7,11,15]
result = s1.twoSum(nums,target= 9)

print(result)


#pass