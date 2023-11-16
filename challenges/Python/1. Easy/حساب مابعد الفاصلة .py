def Decimal_places(num: str) -> int:
    if '.' in num:
        x = num.split('.')
        x = x[1]
        return len(x)
    else:
        return 0