
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def remove_duplicate(arr: list[int]) -> list[int]:
    arrr = []
    for i in arr:
        if i not in arrr:
            arrr.append(i)

    return arrr