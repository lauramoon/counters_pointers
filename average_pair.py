def average_pair(arr, avg):
    lower = 0
    upper = len(arr) - 1

    while lower < upper:
        average = (arr[lower] + arr[upper])/2
        if average == avg:
            return True
        if average > avg:
            upper -= 1
        else:
            lower += 1

    return False