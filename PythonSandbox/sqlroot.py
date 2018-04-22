#!/usr/bin/env python3
def sqrt(input_s):
    ''' Compute square root using the method of Heron of Alexandria.
    Args:
        x: The number of which the square root is to be computed

    Returns:
        The square root of x.

    Raises: 
        ValueErro: if x is negative.
    '''

    if input_s < 0:
        raise ValueError("Cannot compute square root of "
                        "negative number {}".format(input_s))
    guess = input_s
    i = 0
    while guess * guess != input_s and i < 20:
        guess = (guess + input_s / guess) / 2.0
        i += 1
    return guess
    


