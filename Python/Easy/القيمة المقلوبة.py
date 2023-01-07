
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def isMirrored(num: int) -> bool:
    x = str(num)
    y = x[::-1]
    if x == y:
        return True
    else:
        return False