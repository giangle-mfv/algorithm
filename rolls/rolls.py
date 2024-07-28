import math
def findMissingRolls(results, missedRolls, mean):
    currentSum = sum(results)
    realSum = mean * (len(results) + missedRolls)
    missedSum = realSum - currentSum
    if missedSum <= 0:
        return [0]
    
    if (missedSum > 6*missedRolls):
        return [0]
    return generateMissedRolls(missedSum, missedRolls)

def generateMissedRolls(sum, missedRolls):
    result = []
    for i in range(missedRolls):
        next = getPossibleLargestNumber(sum, missedRolls - i)
        if (i + 1 < missedRolls):
            result.append(next)
            sum -= next
        else:
            result.append(sum)
    return result

def getPossibleLargestNumber(total, size):
    left = total - size + 1
    if (left > 6):
        return 6
    return left

input = [1,5,6]
print(findMissingRolls(input, 3, 4))
        

