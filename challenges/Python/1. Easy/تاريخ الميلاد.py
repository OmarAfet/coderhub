def kSumSubset(dateString: str) -> bool:
    return int(dateString[:4]) <= (2022 - 4) and int(dateString[:4]) > (2022 - 200)