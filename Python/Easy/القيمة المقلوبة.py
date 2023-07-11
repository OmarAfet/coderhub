
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def isMirrored(num: int) -> bool:
    x = str(num)
    y = x[::-1]
    if x == y:
        return True
    else:
        return False