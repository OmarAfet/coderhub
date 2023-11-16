def sub_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    maxLength = 0
    if len(arr1) > len(arr2):
        maxLength = len(arr1)
    else:
        maxLength = len(arr2)
        
    result = []
    for i in range(0, maxLength):
        result.append(arr2[i] - arr1[i])
                      
    return result