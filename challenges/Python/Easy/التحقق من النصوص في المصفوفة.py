def stringCheck(value: list[str]) -> bool:
    first = value[0]
    return all(first == elem for elem in value)
