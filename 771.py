class Solution:
    def numJewelsInStones(self, J, S):
        j = list(J.strip())
        count = 0

        for i in S:
            if i in j:
                count += 1
        return count
    
num = Solution()
print(num.numJewelsInStones('aA', 'aAAbbbbba'))


