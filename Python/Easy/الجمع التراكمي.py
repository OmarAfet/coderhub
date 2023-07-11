
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def cumulative_addition(elements_array: list[int]) -> list[int]:
    length = len(elements_array)
    sum = 0
    for i in elements_array:
        sum += i
    
    return [sum, length]