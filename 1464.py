class Solution:
    def maxProduct(self, a):
        
        max_ele = max(a)
        max_ele_ind = a.index(max_ele)
        max_ele = a.pop(max_ele_ind)
        max_ele_2 = max(a)

        return (max_ele-1) * (max_ele_2-1)


m = Solution()
print(m.maxProduct(
[1,5,4,5]))