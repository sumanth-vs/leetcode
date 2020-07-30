<<<<<<< HEAD
class Solution:
    def longestCommonPrefix(self, strs):
        mtStr = ""
        if len(strs) == 0:
            return ""
        else:
            lp = strs[0]
            for i in strs:
                if len(i) < len(lp):
                    lp = i
            print('initailly lp = ', lp)
            

            for i in range(len(strs)):
                for j in range(len(min(lp, strs[i]))):
                    if lp[j] != strs[i][j]:
                        lp = strs[i][:j]
                        break
            if len(lp) == 0:
                return mtStr
            else:
                return lp
        

lcp = Solution()
lists = ['ca', 'a']
=======
class Solution:
    def longestCommonPrefix(self, strs):
        mtStr = ""
        if len(strs) == 0:
            return ""
        else:
            lp = strs[0]
            for i in strs:
                if len(i) < len(lp):
                    lp = i
            print('initailly lp = ', lp)
            

            for i in range(len(strs)):
                for j in range(len(min(lp, strs[i]))):
                    if lp[j] != strs[i][j]:
                        lp = strs[i][:j]
                        break
            if len(lp) == 0:
                return mtStr
            else:
                return lp
        

lcp = Solution()
lists = ['ca', 'a']
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
print(lcp.longestCommonPrefix(lists))