class Solution:
    def subtractProductAndSum(self, n):
        sum_of_digits = 0
        product_of_digits = 1

        while(n != 0):
            digit = n % 10
            sum_of_digits += digit
            product_of_digits *= digit
            n //= 10
        return product_of_digits - sum_of_digits

m = Solution()
print(m.subtractProductAndSum(234))