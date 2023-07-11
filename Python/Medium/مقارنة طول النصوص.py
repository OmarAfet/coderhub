
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def str_len_comparison(words: list[str]) -> bool:
    if len(words) == 0 or len(words) == 1:
        return False

    x = len(words[0])
    for i in words:
        if len(i) == x:
            continue
        else:
            return False
    return True