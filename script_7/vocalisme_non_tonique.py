"""
Ce script s'occupe de tout ce qui est lié au vocalisme.
"""

class VocalismeNonTonique:

    def __init__(self):
        return

    def vocalisme_atone(object):
        changements = ''

        if ("I") in object:
            changements = object.replace("I", "")
        elif ("AU") in object:
            changements = object.replace("AU", "")
        elif ("E") in object:
            changements = object.replace("E", "")
        elif ("U") in object:
            changements = object.replace("U", "")
        elif ("A") in object:
            changements = object.replace("A", "e")
        elif ("O") in object:
            changements = object.replace("O", "")

        return changements
