
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def oct_to_hex(octal_number: int) -> str:
    return (hex(int(str(octal_number), 8))[2:]).upper()