
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def countDown(number: int) -> str:
    x = ''
    for i in range(number, -1, -1):
        x += str(i) + ' '
    x = x[:-1]
    return x