def count_ones(num: int) -> int:
    return bin(num)[2:].count("1")