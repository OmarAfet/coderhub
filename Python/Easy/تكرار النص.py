
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def word_repeat(word: str, n: int) -> str:
    if (' ' in word) == False:
        word = word + ' '
        x = word * n
        return x[:-1]
    else:
        x = word * n
        return x[:-1]