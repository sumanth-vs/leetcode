<<<<<<< HEAD
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        # Assuming max function is effiecieny
        greatestCandies = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >=greatestCandies:
                result.append(True)
            else:
                result.append(False)
        return result

kidsWithCandies = Solution()
candies = [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies.kidsWithCandies(candies, extraCandies))


# What if we do not use the max function

# TODO: Do this later

class DifferentSolution:
    def kids2(self, candies, extraCandies):
        minCandies = 0
        for i in candies:
            if i + extraCandies < minCandies:
=======
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        # Assuming max function is effiecieny
        greatestCandies = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >=greatestCandies:
                result.append(True)
            else:
                result.append(False)
        return result

kidsWithCandies = Solution()
candies = [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies.kidsWithCandies(candies, extraCandies))


# What if we do not use the max function

# TODO: Do this later

class DifferentSolution:
    def kids2(self, candies, extraCandies):
        minCandies = 0
        for i in candies:
            if i + extraCandies < minCandies:
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
