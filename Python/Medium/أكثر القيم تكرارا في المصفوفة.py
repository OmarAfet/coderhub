
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def most_frequent_element(arr):
    frequency_map = {}
    for digit in arr:
        if digit not in frequency_map:
            frequency_map[digit] = 0
        frequency_map[digit] += 1

    most_frequent = None
    highest_frequency = 0
    for digit, frequency in frequency_map.items():
        if frequency > highest_frequency:
            most_frequent = digit
            highest_frequency = frequency

    return most_frequent