def arrowDuplicates(word: str) -> str:
    table = [x.lower() for x in word]
    result = ''

    for i in table:
        if table.count(i) > 1:
            result += '<'
        else:
            result += '>'

    return result