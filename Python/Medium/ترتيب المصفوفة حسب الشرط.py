
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def sort_array(my_array: list[int], typeParam: str) -> list[int]:
    if typeParam == "S":
        return sorted(my_array)
    if typeParam == "B":
        return sorted(my_array, reverse=True)