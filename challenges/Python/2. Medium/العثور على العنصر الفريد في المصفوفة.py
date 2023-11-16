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