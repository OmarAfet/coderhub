
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

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
