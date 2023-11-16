def allSameCase(word: str) -> bool:
    if word.islower():
        return word.islower()
    elif word.isupper():
        return word.isupper()
    else:
        return False
