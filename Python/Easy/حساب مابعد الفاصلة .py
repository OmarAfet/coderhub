
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def Decimal_places(num: str) -> int:
    if '.' in num:
        x = num.split('.')
        x = x[1]
        return len(x)
    else:
        return 0