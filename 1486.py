class Solution:
    def xorOperation(self, n, start):
        nums = [x for x in range(start, start+((n-1)*2)+1, 2)]
        # print('nums = ', nums)
        xorred = nums[0]
        for i in range(1, len(nums)):
            xorred = xorred ^ nums[i]
        return xorred


xo = Solution()
print(xo.xorOperation(1, 7))
        