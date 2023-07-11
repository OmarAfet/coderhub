
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def input_type(value: str) -> str:
    if value.isdigit():
        return 'integer'
    elif value.isalpha():
        return 'string'

    for i in value:
        if i == '.':
            return 'double'
        else:
            pass