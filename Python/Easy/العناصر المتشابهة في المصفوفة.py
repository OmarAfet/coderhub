
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def get_duplicate_elements(arr: list[int]) -> list[int]:
    x = []
    y = []
    for i in arr:
        if i in x and i not in y:
            y.append(i)
            pass
        else:
            x.append(i)
    return y