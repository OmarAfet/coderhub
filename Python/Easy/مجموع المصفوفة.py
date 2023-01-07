
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def calculate_sum(lst: list[int]) -> int:
    result = 0

    for i in lst:
        result += i
        if i == 7:
            return 0
        
    return result