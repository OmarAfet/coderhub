def bin_to_oct(b: str) -> int:
    x = int(b, 2)
    return int(oct(x)[2:])