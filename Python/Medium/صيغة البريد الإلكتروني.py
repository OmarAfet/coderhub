
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

import re
def isEmail(email: str) -> bool:
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))