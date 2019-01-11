"""
Ce script s'occupe de tout ce qui est en rapport avec le consonantisme final.
"""

class ConsonantismeFinal:

    def __init__(self):
        return

    def position_finale(self, object):
        if object in ["T", "P", "S", "D", "F", "G", "C", "B", 'V']:
            return('')
        elif object in ["R", "L"]:
            return('')
        elif object in ["M", "N"]:
            return('')
