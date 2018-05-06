"""Basic Show Class"""
class Show(object):
    """description of class"""
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No event code is '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid event code '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid show number '{}'".format(number))

        self._number = number

    def number(self):
        return self._number

    def event(self):
        return self._number[:2]


