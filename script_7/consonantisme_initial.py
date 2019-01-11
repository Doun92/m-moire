"""
Ce script s'occupe de tout ce qui est en rapport avec le consonantisme initial.
"""

class ConsonantismeInitial:

    def __init__(self):
        return

    def position_initiale(self, object):
        if object in ["T", "P", "S", "D", "F", "G", "C", "B", 'V', 'J', 'Q']:
            return object
        elif object in ["R", "L"]:
            return object
        elif object in ["M", "N"]:
            return object
