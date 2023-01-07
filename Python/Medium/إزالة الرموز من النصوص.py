
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def removeSpecialCharacters(strParam: str) -> str:
    blacklist = "!\"#$%&'()*+,./:;<=>?@[\]^`{|}~"
    result = [x for x in strParam if x not in blacklist]
    return "".join(result)