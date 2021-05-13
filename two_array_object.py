def two_array_object(arr1, arr2):
    """
    create dictionary from two lists, arr1 contains the keys and arr2 the values
    if the lists are not the same size, extra values are ignored, extra keys have value None
    """
    map = {}
    for i in range(len(arr1)):
        map[arr1[i]] = arr2[i] if i < len(arr2) else None

    return map