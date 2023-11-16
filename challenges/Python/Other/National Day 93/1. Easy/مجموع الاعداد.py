def sum_numbers(num: int, s: str) -> int:
    sum = 0
    if s == 'زوجي':
        for i in range(1, num + 1):
            if i % 2 == 0:
                sum += i
    elif s == 'فردي':
        for i in range(1, num + 1):
            if i % 2 != 0:
                sum += i
    return sum
