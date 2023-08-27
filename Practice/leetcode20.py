class Solution(object):
    def removeDuplicates(self,nums):
       self.nums=nums
       self.expectedNums=0
       i=1
       while i<len(self.nums):
           if self.nums[i]==self.nums[i-1]:
               self.nums.pop(i)
           else:
               i+=1

       self.expectedNums=len(self.nums)

       return self.expectedNums



nums=[1,1,1,2,6,7]
s1=Solution()
r=s1.removeDuplicates(nums)
print(r)





