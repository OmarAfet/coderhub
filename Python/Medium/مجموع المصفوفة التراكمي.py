
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def cumulative_sum(arr: list[int]) -> list[int]:
    cumulative_sum_arr = []
    cumulative_sum = 0
    for value in arr:
        cumulative_sum += value
        cumulative_sum_arr.append(cumulative_sum)
    return cumulative_sum_arr