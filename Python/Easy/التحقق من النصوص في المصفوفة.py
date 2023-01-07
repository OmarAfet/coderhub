
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def stringCheck(value: list[str]) -> bool:
    first = value[0]
    return all(first == elem for elem in value)
