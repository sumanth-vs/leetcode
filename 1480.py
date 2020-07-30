<<<<<<< HEAD
class Solution:
    def runningSum(self, nums):
        runningSum = [nums[0]]
        for i in range(1, len(nums)):
            runningSum.append(runningSum[i-1] + nums[i])
        return runningSum

RunningSum = Solution()
array = [1, 2, 3, 4, 5]
=======
class Solution:
    def runningSum(self, nums):
        runningSum = [nums[0]]
        for i in range(1, len(nums)):
            runningSum.append(runningSum[i-1] + nums[i])
        return runningSum

RunningSum = Solution()
array = [1, 2, 3, 4, 5]
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
print(RunningSum.runningSum(array))