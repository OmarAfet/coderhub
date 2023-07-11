
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def sum_even(arr: list[int]) -> int:
    x = []
    for i in arr:
        if i % 2 == 0:
            x.append(i)
    return sum(x)