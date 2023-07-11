
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def namesSort(namesArray: list[str], order: str) -> list[str]:
    if order == "ASC":
        namesArray.sort()
    elif order == "DESC":
        namesArray.sort(reverse=True)
    return namesArray