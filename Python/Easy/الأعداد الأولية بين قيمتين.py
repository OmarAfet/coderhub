
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

import math
def getPrimesBetween(a: int, b: int) -> list[int]:
    if a < 2:
        a = 2
    if b < a:
        return []

    primes = []

    for num in range(a, b+1):
        is_prime = True

        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes