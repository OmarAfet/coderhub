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