
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def math_expr(expr: str) -> bool:
    for i in expr:
        if i.isalpha() or i in "!#\"$&'(),.:;<=>?@[\]^_`{|}~":
            return False

    return True