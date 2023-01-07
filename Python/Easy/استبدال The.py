
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def replaceThe(txt: str) -> str:
    words = txt.split()

    for i, word in enumerate(words):
        if word == "the":
            if words[i+1][0] in ['a', 'e', 'i', 'o', 'u']:
                words[i] = "an"
            else:
                words[i] = "a"

    return " ".join(words)