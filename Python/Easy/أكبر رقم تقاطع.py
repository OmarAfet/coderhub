
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def getBiggestShared(a: list[int], b: list[int]) -> int:
    x = []
    for i in a:
        for j in b:
            if i == j:
                x.append(i)
    x.sort()
    return x[-1]