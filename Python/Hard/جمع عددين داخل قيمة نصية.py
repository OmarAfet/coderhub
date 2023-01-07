
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def addStrNums(num1: str, num2: str) -> str:
    if not num1.isdigit() or not num2.isdigit():
        return '-1'
    else:
        x = int(num1) + int(num2)
        return str(x)