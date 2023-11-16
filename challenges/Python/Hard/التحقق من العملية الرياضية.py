def math_expr(expr: str) -> bool:
    for i in expr:
        if i.isalpha() or i in "!#\"$&'(),.:;<=>?@[\]^_`{|}~":
            return False

    return True