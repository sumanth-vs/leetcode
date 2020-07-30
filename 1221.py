class Solution:
    def balancedStringSplit(self, s):
        
        l = 0
        r = 0
        count = 0

        for i in s:
            if i == 'L':
                l+=1
            if i == 'R':
                r+=1
            if l == r and l > 0:
                count += 1
                l = 0
                r = 0
                
        return count


m = Solution()
print(m.balancedStringSplit('LRLRLR'))