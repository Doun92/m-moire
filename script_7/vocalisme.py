"""
Ce script s'occupe de tout ce qui est lié au vocalisme.
"""

class Vocalisme:

    def __init__(self):
        return

    def syllabe_fermee(self, object):
        if ("Í") in object:
            changements = object.replace("Í", "i")
        elif ("Ẹ") in object:
            changements = object.replace("Ẹ", "e")
        elif ("Ę") in object:
            changements = object.replace("Ę", "e")
        elif ("Á") in object:
            changements = object.replace("Á", "a")
        elif ("Ǫ") in object:
            changements = object.replace("Ǫ", "o")
        elif ("Ọ") in object:
            changements = object.replace("Ọ", "o")
        elif ("Ú") in object:
            changements = object.replace("Ú", "u")
        return changements

    def syllabe_ouverte(self, object):
        if ("Í") in object:
            changements = object.replace("Í", "i")
        elif("AU") in object:
            changements = object.replace("AU", "o")
        elif ("Ẹ") in object:
            changements = object.replace("Ẹ", "ei")
        elif ("Ę") in object:
            changements = object.replace("Ę", "ie")
        elif ("Á") in object:
            changements = object.replace("Á", "e")
        elif ("Ǫ") in object:
            changements = object.replace("Ǫ", "ue")
        elif ("Ọ") in object:
            changements = object.replace("Ọ", "ou")
        elif ("Ú") in object:
            changements = object.replace("Ú", "u")
        return changements

    def vocalisme_contretonique(self, object):
        if "I" in object:
            changements = object.replace("I", "i")
        elif "E" in object:
            changements = object.replace("E", "e")
        elif "U" in object:
            changements = object.replace("U", "u")
        elif "A" in object:
            changements = object.replace("A", "a")
        elif "O" in object:
            changements = object.replace("O", "o")
        return changements
