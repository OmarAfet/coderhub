def calculate_sum(lst: list[int]) -> int:
    result = 0

    for i in lst:
        result += i
        if i == 7:
            return 0
        
    return result