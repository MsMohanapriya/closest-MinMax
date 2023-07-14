def closestMinMax(array):
    minimum = float('inf')
    maximum = float('-inf')
    RMinIndex = -1
    RMaxIndex = -1
    result = len(array)
    for i in range(len(array)):
        if array[i] < minimum:
            minimum = array[i]
        if array[i] > maximum:
            maximum = array[i]


    for i in range(len(array)):
        if array[i] == minimum:
            RMinIndex = i
            if RMaxIndex >= 0:
                result = min(result, i - RMaxIndex + 1)
        if array[i] == maximum:
            RMaxIndex = i
            if RMinIndex >= 0:
                result = min(result, i - RMinIndex + 1)

    return result

array = list(map(int, input().split()))
print(closestMinMax(array))
