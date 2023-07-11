
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def convertPercent(percentage: str) -> float:
    x = percentage.split('%')
    x = int(x[0]) / 100
    return x