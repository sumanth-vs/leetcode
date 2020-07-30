<<<<<<< HEAD
# class Solution:
        
#     #PUSH
#     def push(stk, tos, val):
#         tos += 1
#         stk[tos] = val
#         return stk, tos
        
#     #POP
#     def pop(stk, tos):
#         val = stk[tos]
#         tos -= 1
#         return stk, tos
    
#     # LOGIC
#     def isValid(self, s: str) -> bool:
        
#         stk = ['']*len(s)
#         tos = -1
        
        
#         for i in s:
#             if i == '(' or i == '[' or i =='{':
#                 stk, tos = Solution.push(stk, tos, i)
#             else:
#                 ele = stk[tos]
#                 if (ele == '(' and i == ')') or (ele == '[' and i == ']') or (ele == '{' and i == '}'):
#                     stk, tos = Solution.pop(stk, tos)
        
#         if tos == -1:
#             return True
#         else:
#             return False


# m = Solution()
# print(m.isValid('}'))




# CLEAN AND ELEGENT SOLUTION:


class Solution:
    def isValid(self, s: str) -> bool:

        dict = {
            
            '(': ')', 
            '[': ']', 
            '{': '}'
        }

        stack = []

        for bracket in s:
            if bracket in dict:
                stack.append(bracket)
            else:
                if dict[stack.pop] != bracket:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
=======
class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        tos = stck.top()

        for i in s:
            tos = stck.top()
            if i == '(' or i == '[' or i == '{':
                stck.push()
            else:
                if i == ')' and stck[tos] == '(':
                    stck.pop()
                elif i == ']' and stck[tos] == '[':
                    stck.pop(tos)
                elif i == '}' and stck[tos] == '{':
                    stck.pop(tos)
        if len(stck) == 0 and tos == 0:
            return True
        else:
            return False

string = '()[]'
isValidObj = Solution()
print(isValidObj.isValid(string))
        
        
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
