
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def match_arrays(array1: list[str], array2: list[str]) -> bool:
    x = None
    y = None
    for i in array1:
        if i in array2:
            x = True
        else:
            x = False
            break

    for i in array2:
        if i in array1:
            y = True
        else:
            y = False
            break
    return x and y
