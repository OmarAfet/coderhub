import math
def array_root(arr: list[float]) -> list[float]:
    result = []
    for i in arr:
        result.append(math.sqrt(i))
        
    return result