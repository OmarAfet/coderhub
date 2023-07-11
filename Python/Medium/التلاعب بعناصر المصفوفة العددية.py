
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def filp_even_odd(numbers: list[int]) -> list[int]:
    x = []
    for i, n in enumerate(numbers):
        x.append(n + 1 if n % 2 == 0 else n - 1)
    return x

    
    
print(filp_even_odd([73,221,52,214]))