class Solution:
    def decompressRLElist(self, nums):
        decompressed_list = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            val = nums[i+1]
            for j in range(freq):
                decompressed_list.append(val)
        return decompressed_list

m = Solution()
listt = [1,1, 2, 3]
print(m.decompressRLElist(listt))