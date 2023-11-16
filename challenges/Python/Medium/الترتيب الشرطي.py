def namesSort(namesArray: list[str], order: str) -> list[str]:
    if order == "ASC":
        namesArray.sort()
    elif order == "DESC":
        namesArray.sort(reverse=True)
    return namesArray