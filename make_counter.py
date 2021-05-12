def make_counter(string):
    """
    returns dictionary with letter as key and frequescy as value
    """
    counter = {}
    for char in string:
        counter[char] = 1 if char not in counter else counter[char] + 1

    return counter