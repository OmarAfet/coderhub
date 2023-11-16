def replaceThe(txt: str) -> str:
    words = txt.split()

    for i, word in enumerate(words):
        if word == "the":
            if words[i+1][0] in ['a', 'e', 'i', 'o', 'u']:
                words[i] = "an"
            else:
                words[i] = "a"

    return " ".join(words)