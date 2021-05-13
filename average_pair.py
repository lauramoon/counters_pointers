def average_pair(arr, avg):
    """
    returns true if there is a pair of intergers in sorted list arr that has the average avg
    in O(N) time
    """
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