
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def left_digit(strParam: str) -> int:
    for char in strParam:
        if char.isdigit():
            return int(char)
    return None