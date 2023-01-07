
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def sort_array(my_array: list[int], typeParam: str) -> list[int]:
    if typeParam == "S":
        return sorted(my_array)
    if typeParam == "B":
        return sorted(my_array, reverse=True)