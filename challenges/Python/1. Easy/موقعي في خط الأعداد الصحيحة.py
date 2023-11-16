def less_or_more_than_zero(number: int) -> str:
    if number > 0:
        return 'Greater than zero'
    elif number < 0:
        return 'Less than zero'
    elif number == 0:
        return 'Equal to zero'
