def numbers_range(number: int) -> str:
    x = ''
    for i in range(number + 1):
        x += str(i) + ' '
    return x[:-1]