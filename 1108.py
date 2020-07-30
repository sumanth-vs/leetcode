<<<<<<< HEAD
class Solution:
    def defangIPaddr(self, address):
        newAddr = ''
        for i in address:
            if i == '.':
                newAddr += '[.]'
            else:
                newAddr += i
        return newAddr


address = "1.1.1.1"
defang = Solution()
print(defang.defangIPaddr(address))
=======
class Solution:
    def defangIPaddr(self, address):
        newAddr = ''
        for i in address:
            if i == '.':
                newAddr += '[.]'
            else:
                newAddr += i
        return newAddr


address = "1.1.1.1"
defang = Solution()
print(defang.defangIPaddr(address))
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
        