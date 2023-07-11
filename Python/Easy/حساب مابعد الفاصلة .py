
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def Decimal_places(num: str) -> int:
    if '.' in num:
        x = num.split('.')
        x = x[1]
        return len(x)
    else:
        return 0