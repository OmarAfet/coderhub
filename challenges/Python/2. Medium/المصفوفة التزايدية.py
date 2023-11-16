def increasing_array(arr: list[int]) -> int:
    points = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            points += arr[i-1] - arr[i]
            arr[i] = arr[i-1]
    return points