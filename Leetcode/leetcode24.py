# Solution 1 failed time complexity
# Top  k frequent element
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         ans = {}
#         if len(nums) == 1:
#             return nums
#         else:
#             for i in range(0, len(nums)):
#                 ans[nums[i]] = nums.count(nums[i])
#
#             result = dict(sorted(ans.items(), key=lambda i: i[1], reverse=True))
#             result= list(result.keys())[:k]
#             return result

#passes
class Solution(object):
    def topKFrequent(self, nums, k):
        ans = {}

        for number in nums:
            if number not in ans:
                ans[number] = 0
            ans[number] += 1

        counter = dict(sorted(ans.items(),key= lambda x: x[1], reverse=True))

        result = list(counter.keys())[:k]

        return result

s1=Solution()
nums=[3,0,1,0]
k=1
x=s1.topKFrequent(nums,k)
print(x)

# pending


