def remove_duplicate(arr: list[int]) -> list[int]:
    arrr = []
    for i in arr:
        if i not in arrr:
            arrr.append(i)

    return arrr