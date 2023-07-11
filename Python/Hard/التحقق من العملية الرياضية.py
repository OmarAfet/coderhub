
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def math_expr(expr: str) -> bool:
    for i in expr:
        if i.isalpha() or i in "!#\"$&'(),.:;<=>?@[\]^_`{|}~":
            return False

    return True