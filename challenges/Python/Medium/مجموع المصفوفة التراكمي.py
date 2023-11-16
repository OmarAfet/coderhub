def cumulative_sum(arr: list[int]) -> list[int]:
    cumulative_sum_arr = []
    cumulative_sum = 0
    for value in arr:
        cumulative_sum += value
        cumulative_sum_arr.append(cumulative_sum)
    return cumulative_sum_arr