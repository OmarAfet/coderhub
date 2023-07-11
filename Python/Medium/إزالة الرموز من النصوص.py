
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def removeSpecialCharacters(strParam: str) -> str:
    blacklist = "!\"#$%&'()*+,./:;<=>?@[\]^`{|}~"
    result = [x for x in strParam if x not in blacklist]
    return "".join(result)