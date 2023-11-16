def sortByLength(txt: str) -> str:
    words = txt.split()

    sorted_words = sorted(words, key=lambda x: (len(x), x))

    return ' '.join(sorted_words)