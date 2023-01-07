
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def unique(arr: list[int]) -> list[int]:
    numbers = {}
    
    for i in arr:
        if i in numbers:
            numbers[i] += 1
        else:
            numbers[i] = 1
            
    result = []
    for key, value in numbers.items():
        result = [i for i in numbers if numbers[i] == value]
        
    return result