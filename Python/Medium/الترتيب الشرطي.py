
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def namesSort(namesArray: list[str], order: str) -> list[str]:
    if order == "ASC":
        namesArray.sort()
    elif order == "DESC":
        namesArray.sort(reverse=True)
    return namesArray