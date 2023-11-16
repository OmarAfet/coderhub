def middle_char(word: str) -> str:
    result = (len(word) / 2)

    if result % 1 == 0:
        result = word[int(result) - 1:int(result) + 1]
    else:
        result = word[int(result)]
        
    return result