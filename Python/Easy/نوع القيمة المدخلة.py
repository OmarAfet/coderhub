
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

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