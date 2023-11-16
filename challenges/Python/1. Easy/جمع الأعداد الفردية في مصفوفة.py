def sumOdd(arr: list[int]) -> int:
    x = []
    for i in arr:
        if i % 2 != 0:
            x.append(i)
    return sum(x)