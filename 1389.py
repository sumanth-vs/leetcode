
def insertAtPosition(ind, val, target):
    target.append(0)

    for i in range(len(target)-2, ind-1, -1):
        target[i+1] = target[i]
    
    target[ind] = val

    return target



def createTargetArray(index, nums):
    target = [-1]*len(nums)

    for i in range(len(nums)):
        ind = index[i]

        if target[ind] == -1:
            target[ind] = nums[i]
        else:
            target =  insertAtPosition(index[i], nums[i], target)
        




    

nums = [0,1,2,3,4]
index = [0,1,2,2,1]

print(createTargetArray(nums, index))





