from datetime import datetime
def timePeriod(date1: str, date2: str) -> bool:
    start_date = datetime.fromisoformat(date1)
    end_date = datetime.fromisoformat(date2)

    if start_date >= end_date:
        return False

    today = datetime.today()
    if start_date >= today or end_date >= today:
        return False

    return True