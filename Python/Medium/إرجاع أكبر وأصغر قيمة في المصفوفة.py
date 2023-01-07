
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def largest_smallest(array_values: list[int]) -> list[int]:
    result = sorted(array_values)
    return [result[-1], result[0]]