
# Creator: OmarAfet
# https://profile.satr.codes/OmarAfet/public/overview
# https://github.com/OmarAfet

def countdown(num: int) -> list[int]:
    if num <= 3:
        return [0]
    else:
        even_numbers = []
        countdown = num
        while countdown > 0:
            if countdown % 2 == 0 and countdown != num:
                even_numbers.append(countdown)
            countdown -= 3
        return sorted(even_numbers)