def filp_even_odd(numbers: list[int]) -> list[int]:
    x = []
    for i, n in enumerate(numbers):
        x.append(n + 1 if n % 2 == 0 else n - 1)
    return x

    
    
print(filp_even_odd([73,221,52,214]))