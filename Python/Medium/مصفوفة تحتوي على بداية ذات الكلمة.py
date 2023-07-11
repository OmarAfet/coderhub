
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def find_prefix(words: list[str], text: str) -> list[str]:
    x = []
    for i in words:
        if (i[:2]).lower() == (text).lower():
            x.append(i)

    if len(x) == 0:
        return ['No matches found']

    return x