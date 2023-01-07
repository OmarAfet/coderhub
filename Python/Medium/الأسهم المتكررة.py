
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def arrowDuplicates(word: str) -> str:
    table = [x.lower() for x in word]
    result = ''

    for i in table:
        if table.count(i) > 1:
            result += '<'
        else:
            result += '>'

    return result