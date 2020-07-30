class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_num = ''
        decimal_num = 0
    
        while head != None:
            binary_num += str(head.val)
            head = head.next
            
        print(binary_num)
        
        binary_num = binary_num[::-1]
        
        for i in range(len(binary_num)):
            if binary_num[i] == '1':
                decimal_num += pow(2, i)
                
        return decimal_num


getDecimal = Solution()
print(getDecimal.getDecimalValue())