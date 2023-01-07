
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def get_duplicate_elements(arr: list[int]) -> list[int]:
    x = []
    y = []
    for i in arr:
        if i in x:
            y.append(i)
            pass
        else:
            x.append(i)
    return y