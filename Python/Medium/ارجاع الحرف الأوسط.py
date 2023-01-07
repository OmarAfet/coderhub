
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def middle_char(word: str) -> str:
    result = (len(word) / 2)

    if result % 1 == 0:
        result = word[int(result) - 1:int(result) + 1]
    else:
        result = word[int(result)]
        
    return result