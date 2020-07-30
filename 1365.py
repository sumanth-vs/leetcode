# class Solution:
#     def smallerNumbersThanCurrent(self, nums):
#         nums.sort()
#         nums = nums[::-1]
#         g = []

#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i+1]:
#                 g.append(len(nums) - i - 1)
            
#         return g

# m = Solution()
# print(m.smallerNumbersThanCurrent([1,8,2,2,3]))
        


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        greater = [0]*len(nums)
        print(greater)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    greater[i] += 1
        return greater
    
m = Solution()
print(m.smallerNumbersThanCurrent([8,1,2,2,3]))
