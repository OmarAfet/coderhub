
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def getBiggestShared(a: list[int], b: list[int]) -> int:
    x = []
    for i in a:
        for j in b:
            if i == j:
                x.append(i)
    x.sort()
    return x[-1]