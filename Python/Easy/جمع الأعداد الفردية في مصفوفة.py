
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def sumOdd(arr: list[int]) -> int:
    x = []
    for i in arr:
        if i % 2 != 0:
            x.append(i)
    return sum(x)