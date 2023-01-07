
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def cap_space(txt: str) -> str:
    result = ""
    for i, c in enumerate(txt):
        if c.isupper() and i > 0:
            result += " "
        result += c.lower()
    return result