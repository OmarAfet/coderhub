
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def operation(num1: int, num2: int) -> str:
    if num1 + num2 == 24:
        return "added"
    elif num1 - num2 == 24:
        return "subtracted"
    elif num1 / num2 == 24:
        return "divided"
    elif num1 * num2 == 24:
        return "multiplied"
    else:
        return "None"