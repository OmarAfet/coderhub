
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

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