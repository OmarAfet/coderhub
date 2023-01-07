
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def find_prefix(words: list[str], text: str) -> list[str]:
    x = []
    for i in words:
        if (i[:2]).lower() == (text).lower():
            x.append(i)

    if len(x) == 0:
        return ['No matches found']

    return x