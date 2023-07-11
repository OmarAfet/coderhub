
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def allSameCase(word: str) -> bool:
    if word.islower():
        return word.islower()
    elif word.isupper():
        return word.isupper()
    else:
        return False
