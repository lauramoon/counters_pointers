from make_counter import make_counter

def construct_note(msg, letters):
    """
    returns True if the characters in the string letters are sufficient to create
    the string msg. Assume all lowercase and no special characters
    """
    msg_counter = make_counter(msg)
    letter_counter = make_counter(letters)

    for key in msg_counter:
        if key not in letter_counter:
            return False
        if msg_counter[key] > letter_counter[key]:
            return False
    return True