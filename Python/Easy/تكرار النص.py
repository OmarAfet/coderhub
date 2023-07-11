
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def word_repeat(word: str, n: int) -> str:
    if (' ' in word) == False:
        word = word + ' '
        x = word * n
        return x[:-1]
    else:
        x = word * n
        return x[:-1]