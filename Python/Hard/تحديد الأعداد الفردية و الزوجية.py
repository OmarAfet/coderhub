
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

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
