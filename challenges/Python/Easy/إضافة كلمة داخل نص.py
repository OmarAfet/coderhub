def say_hi_bye(name: str, num: int) -> str:
    if num == 0:
        return f'Bye {name}'
    elif num == 1:
        return f'Hi {name}'