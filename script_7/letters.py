"""
Lettre Á (A tonique)
"""
import re
#Importation des autres scripts
from vocalisme import Vocalisme
vocalisme = Vocalisme()

from vocalisme_non_tonique import VocalismeNonTonique
vocalisme_non_tonique = VocalismeNonTonique()

from consonantisme_initial import ConsonantismeInitial
consonantisme_initial = ConsonantismeInitial()

from consonantisme_final import ConsonantismeFinal
consonantisme_final = ConsonantismeFinal()

from syllabifier import Syllabifier
syllabifier = Syllabifier()

from suffixes import Suffixes
suffixes = Suffixes()

#Listes de toutes les lettres traitées dans le script
listes_lettres = {
'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'consonnes' : ["T", "P", "S", "D", "F", "G", "C", "B", 'V'],

'consonnes_liquides' : ["R", "L"],

'consonnes_nasales' : ["M", "N"],

'yod_et_wau' : ["W", "Y"],

# 'prefixes' :  ["EN", "EM", "DES"],

'suffixes' : ['ÁRIU']
}

class LettreA:

    def ___init__(self):
        return

    def règle_générale(self, object):

        syllabes = syllabifier.syllabify(object)

        #Si Á appartient à un groupe spécifique
        #suffixes
        if syllabes[-3][-1] + syllabes[-2] + syllabes[-1] == 'ÁRIU':
            changement.append(suffixes.suffixes('ÁRIU'))
        else:
            pass

        #Autres groupes
        #Je peux tout mettre ici, à compléter
        test_Á = re.search(r'ÁBUI', object)
        if 'Á' in object:
            if test_Á == True:
                changement.append('e')
            else:
                pass

        #Pour vérifier si Á est à la fin d'une syllabe
        for char in syllabes:
            if char[-1] == 'Á':
                if char[-2] in ['C', 'X', 'T']:
                    channgement.append('ie')
                else:
                    changements.append(vocalisme.syllabe_ouverte(char[-1]))
            else:
                pass
