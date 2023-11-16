def removeSpecialCharacters(strParam: str) -> str:
    blacklist = "!\"#$%&'()*+,./:;<=>?@[\]^`{|}~"
    result = [x for x in strParam if x not in blacklist]
    return "".join(result)