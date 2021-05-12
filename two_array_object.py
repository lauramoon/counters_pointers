def two_array_object(arr1, arr2):
    map = {}
    for i in range(len(arr1)):
        map[arr1[i]] = arr2[i] if i < len(arr2) else None

    return map