def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    uppercase = to_swap.upper()
    lowercase = to_swap.lower()
    word = ""
    for ltr in phrase:
        if ltr == uppercase:
            word += f"{ltr.lower()}"
        elif ltr == lowercase:
            word += f"{ltr.upper()}"
        else:
            word += f"{ltr}"
    return word