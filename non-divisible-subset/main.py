def nonDivisibleSubset(k, s):
    mapNumberToAvoid = {}
    mapNumberToCount = {}
    resultList = []
    avoidList = []
    for n in s:
        avoid = countDivisableTimes(n, s, k)
        mapNumberToAvoid[n] = avoid
        mapNumberToCount[n] = len(avoid)
        
    sorted = quickSort(s, mapNumberToCount)
    
    for n in sorted:
        print(n)
        if not n in avoidList:
            resultList.append(n)
            avoidList.extend(mapNumberToAvoid[n])
    return len(resultList)

def quickSort(arr, mapNumberToCount):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    
    # Partition the array into three parts: less than pivot, equal to pivot, and greater than pivot
    left = [x for x in arr[:-1] if mapNumberToCount[x] < mapNumberToCount[pivot]]
    equal = [x for x in arr if mapNumberToCount[x] == mapNumberToCount[pivot]]
    right = [x for x in arr[:-1] if mapNumberToCount[x] > mapNumberToCount[pivot]]
    # Recursively apply quick_sort to the less_than_pivot and greater_than_pivot arrays
    return quickSort(left, mapNumberToCount) + equal + quickSort(right, mapNumberToCount)
    
def countDivisableTimes(number, checkList, k):
    avoid = []
    for i in checkList:
        if number == i:
            continue
        if (number + i) % k == 0:
            avoid.append(i)
    return avoid