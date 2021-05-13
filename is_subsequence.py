def is_subsequence(str1, str2):
    """
    returns True if str2 is a subsequence of str1
    """
    index = 0
    for char in str2:
        if str1[index] == char:
            index += 1
            if index == len(str1):
                return True
    return False