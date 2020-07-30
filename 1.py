<<<<<<< HEAD

def twoSum(nums, target):
    dicti = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in dicti:
            dicti[num] = i
        else:
            return [dicti[n], i]

        
=======

def twoSum(nums, target):
    dicti = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in dicti:
            dicti[num] = i
        else:
            return [dicti[n], i]

        
>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
print(twoSum([1, 2, 3, 4, 5, 6], 11))