
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def average(values: list[int]) -> float:
    if all(isinstance(i, (int, float)) for i in values):
        return sum(values) / len(values)