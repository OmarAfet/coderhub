def largest_smallest(array_values: list[int]) -> list[int]:
    result = sorted(array_values)
    return [result[-1], result[0]]