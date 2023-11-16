def date_formating(date: str) -> str:
    return "-".join(list(reversed(date.split("-"))))