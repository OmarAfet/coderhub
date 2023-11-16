def left_digit(strParam: str) -> int:
    for char in strParam:
        if char.isdigit():
            return int(char)
    return None