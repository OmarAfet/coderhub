def average(values: list[int]) -> float:
    if all(isinstance(i, (int, float)) for i in values):
        return sum(values) / len(values)