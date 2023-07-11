
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def oddsVsEvens(num: int) -> str:
    odd_sum = 0
    even_sum = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        num //= 10
    if odd_sum > even_sum:
        return "odd"
    elif even_sum > odd_sum:
        return "even"
    else:
        return "equal"
