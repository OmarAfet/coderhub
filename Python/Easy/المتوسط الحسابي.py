
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def average(values: list[int]) -> float:
    if all(isinstance(i, (int, float)) for i in values):
        return sum(values) / len(values)