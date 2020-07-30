<<<<<<< HEAD
class Solution:
    def reduceToZero(self, num):
        steps = 0
        while(num != 0):
            if num % 2 == 0:
                num = num // 2
                steps += 1
            else:
                num -= 1
                steps += 1

        return steps

reducer = Solution()
num = 8
print(reducer.reduceToZero(num))


=======
class Solution:
    def reduceToZero(self, num):
        steps = 0
        while(num != 0):
            if num % 2 == 0:
                num = num // 2
                steps += 1
            else:
                num -= 1
                steps += 1

        return steps

reducer = Solution()
num = 8
print(reducer.reduceToZero(num))
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
