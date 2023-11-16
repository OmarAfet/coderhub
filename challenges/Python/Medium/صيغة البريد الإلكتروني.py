import re
def isEmail(email: str) -> bool:
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))