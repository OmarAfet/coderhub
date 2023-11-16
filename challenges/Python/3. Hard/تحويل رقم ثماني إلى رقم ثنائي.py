def oct_to_bin(octal: int) -> str:
    x = int(str(octal), 8)
    return str(int(bin(x)[2:]))