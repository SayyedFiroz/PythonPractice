# leetcode medium level problem

# prctice prefix sum for solving this problem
# #basic
# def prefixsum(list,idx):
#     pre=[0]*len(list)
#     pre[0]=list[0]
#     for i in range(1,len(list)):
#         pre[i]=pre[i-1]+list[i]
#
#     print(pre[idx])
#
# prefixsum([1,2,3,4],2)
# #in range
# def prefixsumrang(list:list,s:int,e:int)->int:
#     pre=[0]*len(list)
#     pre[0]=list[0]
#     for i in range(1,len(list)):
#         pre[i]=pre[i-1]+list[i]
#     rang=pre[e]-pre[s-1]
#     return rang
#
# x=prefixsumrang([1,2,3,4],2,3)
# print(x)

def allprodexcept(nums):
    prev = 1
    post = 1
    result = [1] * (len(nums))
    for i in range(0, len(nums)):
        result[i] *= prev
        prev = prev * nums[i]

    for j in range(len(nums), 0, -1):
        result[j - 1] *= post
        post = post * nums[j - 1]


allprodexcept([1, 2, 3, 4])

