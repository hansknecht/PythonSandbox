#!/usr/bin/env python3
""" This module converts a string to a number
"""
import sys
def convert(input_s):
    """ This is the convert function
    """
    try:
        x_return = int(input_s)
        return x_return
    except (ValueError, TypeError) as e_out:
        print("Conversion Error: {}".format(str(e_out)), file=sys.stderr)
        raise
