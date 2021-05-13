def count_pairs(arr, num):
    """
    counts number of pairs of integers in list arr that sum to num
    arr consists of integers and no duplicates
    """
    prev_set = set([arr[0]])
    count = 0
    for i in range(1, len(arr)):
        if num - arr[i] in prev_set:
            count += 1
        prev_set.add(arr[i])
    return count