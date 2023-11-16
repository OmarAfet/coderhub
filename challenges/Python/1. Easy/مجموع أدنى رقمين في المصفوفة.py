def sum_two_smallest_nums(arr: list[int]) -> int:
    arr.sort()
    return arr[0] + arr[1]