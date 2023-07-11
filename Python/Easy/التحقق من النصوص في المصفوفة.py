
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def stringCheck(value: list[str]) -> bool:
    first = value[0]
    return all(first == elem for elem in value)
