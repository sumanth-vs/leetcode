<<<<<<< HEAD
class Solution:
    def return_priority(self, character):
        priority = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        return priority.index(character)
    
    def return_value(self, character):
        value  = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        return value.get(character)
    
    def romanToInt(self, s: str) -> int:
        for i in s:
            priority = return_priority(i)
=======
class Solution:
    def return_priority(self, character):
        priority = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        return priority.index(character)
    
    def return_value(self, character):
        value  = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        return value.get(character)
    
    def romanToInt(self, s: str) -> int:
        for i in s:
            priority = return_priority(i)
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
            