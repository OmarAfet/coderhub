
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def left_digit(strParam: str) -> int:
    for char in strParam:
        if char.isdigit():
            return int(char)
    return None