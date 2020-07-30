<<<<<<< HEAD
class Solution:
    def shuffle(self, nums, n):
        shuffArr = []
        for i in range(len(nums)-n):
            shuffArr.append(nums[i])
            shuffArr.append(nums[i+n])
        return shuffArr

Shuffle = Solution()
nums = [2,5,1,3,4,7]
n = 3

=======
class Solution:
    def shuffle(self, nums, n):
        shuffArr = []
        for i in range(len(nums)-n):
            shuffArr.append(nums[i])
            shuffArr.append(nums[i+n])
        return shuffArr

Shuffle = Solution()
nums = [2,5,1,3,4,7]
n = 3

>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
print(Shuffle.shuffle(nums, n))