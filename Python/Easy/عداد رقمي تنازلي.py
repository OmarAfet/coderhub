
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def countDown(number: int) -> str:
    x = ''
    for i in range(number, -1, -1):
        x += str(i) + ' '
    x = x[:-1]
    return x