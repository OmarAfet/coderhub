
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def sortByLength(txt: str) -> str:
    words = txt.split()

    sorted_words = sorted(words, key=lambda x: (len(x), x))

    return ' '.join(sorted_words)