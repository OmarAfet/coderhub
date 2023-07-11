
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def sortByLength(txt: str) -> str:
    words = txt.split()

    sorted_words = sorted(words, key=lambda x: (len(x), x))

    return ' '.join(sorted_words)