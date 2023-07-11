
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def addStrNums(num1: str, num2: str) -> str:
    if not num1.isdigit() or not num2.isdigit():
        return '-1'
    else:
        x = int(num1) + int(num2)
        return str(x)