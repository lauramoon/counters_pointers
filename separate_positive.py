def separate_positive(arr):
    lower = 0
    upper = len(arr) - 1

    while lower < upper:
        if arr[lower] > 0:
            lower += 1
        elif arr[upper] < 0:
            upper -= 1
        else:
            temp = arr[lower]
            arr[lower] = arr[upper]
            arr[upper] = temp
    return arr