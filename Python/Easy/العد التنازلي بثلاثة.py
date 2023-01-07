
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

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