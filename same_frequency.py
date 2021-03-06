from make_counter import make_counter

def same_frequency(num1, num2):
    """
    returns true if the two numbers have the same frequency of digits, O(N+M) time
    """
    counter1 = make_counter(str(num1))
    counter2 = make_counter(str(num2))

    for key in counter1:
        if key not in counter2:
            return False
        if counter1[key] != counter2[key]:
            return False
    return True
