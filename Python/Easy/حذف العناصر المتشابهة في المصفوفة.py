
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def remove_duplicate(arr: list[int]) -> list[int]:
    arrr = []
    for i in arr:
        if i not in arrr:
            arrr.append(i)

    return arrr