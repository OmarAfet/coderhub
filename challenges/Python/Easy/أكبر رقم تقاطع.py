def getBiggestShared(a: list[int], b: list[int]) -> int:
    x = []
    for i in a:
        for j in b:
            if i == j:
                x.append(i)
    x.sort()
    return x[-1]