def get_mean(arr: list[int]) -> float:
    sum = 0
    for num in arr:
        sum += num
    return sum / len(arr)