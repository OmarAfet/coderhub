
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def cumulative_addition(elements_array: list[int]) -> list[int]:
    length = len(elements_array)
    sum = 0
    for i in elements_array:
        sum += i
    
    return [sum, length]