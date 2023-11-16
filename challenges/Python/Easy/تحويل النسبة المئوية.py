def convertPercent(percentage: str) -> float:
    x = percentage.split('%')
    x = int(x[0]) / 100
    return x