
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def oct_to_bin(octal: int) -> str:
    x = int(str(octal), 8)
    return str(int(bin(x)[2:]))