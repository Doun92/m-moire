"""

auteur : Daniel Escoval
license : license UNIL
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


#Listes de toutes les lettres traitées dans le script
listes_lettres = {
'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'consonnes' : ["T", "P", "S", "D", "F", "G", "C", "B", 'V', 'K', 'Q', 'J', 'X'],

'consonnes_liquides' : ["R", "L"],

'consonnes_nasales' : ["M", "N"],

'yod_et_wau' : ["W", "Y"],

'consonantisme_complexe' : ['BI', 'BL', 'BR', 'BU', 'DE', 'DI'],

'suffixes' : ['ÁRIU'],

'prefixes': []

}

class SyllabeInitiale:

    def __init__(self):
        return

    def syllabe_initiale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
        #Consonantisme explosif complexe
        if syllabes[0][0] + syllabes[0][1] in listes_lettres['consonantisme_complexe']:
            #Gestion de B
            if syllabes[0][0] + syllabes[0][1] in ['BR', 'BL']:
                changements.append(syllabes[0][0] + syllabes[0][1])
            elif syllabes[0][0] + syllabes[0][1] == 'BI':
                changements.append('gi')
            elif syllabes[0][0] + syllabes[0][1] == 'BU':
                pass
            #Gestion de D
            elif syllabes[0][0] + syllabes[0][1] in ['DI', 'DE':
                changements.append('j')

        #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
        #Consonantisme explosif
        elif syllabes[0][0] in listes_lettres['consonnes']
            #Gestion de B
            if syllabes[0][0] == 'B':
                changements.append(syllabes[0][0])
            #Gestion de C
            elif syllabes[0][0] == 'C':
                #Palatalisation devant A
                if syllabes[0][1] in ['A', 'Á']:
                    changements.append('ch')
                else:
                    changements.append(syllabes[0][0])
            #Gestion de D
            elif syllabes[0][0] == 'D':
                changements.append(syllabes[0][0])
            #Gestion  de F
            #Gestion  de G
            #Gestion de J
            #Gestion de K
            #Gestion de P
            #Gestion de Q
            #Gestion de S
            #Gestion de T
            #Gestion de V
            #Gestion de X

            #Gestion de H

            #Gestion  de L
            #Gestion de R

            #Gestion  de M
            #Gestion de N

            #Gestion de W
            #Gestion de Y

        #Gestion des différents vocalismes
        #Vocalisme contretonique
        if listes_lettres['voyelles_atones'] in syllabes[0]:
            #Gestion de A
            if 'A' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'A':
                        if syllabes[1][0] == 'U':
                            changements.append('e')
                        else
                            changements.append(vocalisme.vocalisme_contretonique(char[-1])
                    elif char[-2] == 'A':
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.vocalisme_contretonique(char[-2])
                    elif char[-3] == 'A':
                        changements.append(vocalisme.vocalisme_contretonique(char[-3])

            #Gestion de E
            if 'E' in syllabes[0]:
                if syllabes[0] == 'DI':
                    changements.append('')
                else:
                    for char in syllabes:
                        if char[-1] == 'E':
                            if len syllabes >= 3:
                                #Gestion du hiatus chez les paroxytons
                                if listes_lettres['voyelles_toniques'] in syllabes[-2][0]:
                                    if syllabes[-2][0] == 'Í':
                                        changements.append('')
                                    elif syllabes[-2][0] == 'Ọ':
                                        changements.append('ie')
                                #Autres règles
                                elif syllabes[1][0] + syllabes[1][1] in ['GÁ', 'GẸ']:
                                    changements.append('ei')
                                else:
                                    changements.append(vocalisme.vocalisme_contretonique(char[-1])
                            else:
                                if sylllabes[1][0] in ['Ọ']:
                                    changements.append('')
                                elif syllabes[1][0] + syllabes[1][1] in ['GÁ', 'GẸ']:
                                    changements.append('ei')
                                else:
                                    changements.append(vocalisme.vocalisme_contretonique(char[-1])
                        elif char[-2] == 'E':
                            if char[-1] in listes_lettres['consonnes_liquides']:
                                if char[-3] in listes_lettres['consonnes']:
                                    changements.append('')
                                else:
                                    changements.append(vocalisme.vocalisme_contretonique(char[-2])
                        elif char[-3] == 'E':
                            changements.append(vocalisme.vocalisme_contretonique(char[-3])

            #Gestion de I:
            if 'I' in syllabes[0]:
                if syllabes[0] == 'DI':
                    changements.append('')
                else:
                    for char in syllabes:
                        if char[-1] == 'I':
                            changements.append(vocalisme.vocalisme_contretonique(char[-1])
                        elif char[-2] == 'I':
                            if char[-1] in listes_lettres['consonnes_liquides']:
                                if char[-3] in listes_lettres['consonnes']:
                                    changements.append('')
                                else:
                                    changements.append(vocalisme.vocalisme_contretonique(char[-2])
                        elif char[-3] == 'I':
                            changements.append(vocalisme.vocalisme_contretonique(char[-3])

            #Gestion de O:
            if 'O' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'O':
                        changements.append(vocalisme.vocalisme_contretonique(char[-1])
                    elif char[-2] == 'O':
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.vocalisme_contretonique(char[-2])
                    elif char[-3] == 'O':
                        changements.append(vocalisme.vocalisme_contretonique(char[-3])

            #Gestion de U:
            if 'U' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'U':
                        changements.append(vocalisme.vocalisme_contretonique(char[-1])
                    elif char[-2] == 'U':
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.vocalisme_contretonique(char[-2])
                    elif char[-3] == 'U':
                        changements.append(vocalisme.vocalisme_contretonique(char[-3])


        #Vocalisme tonique
        if listes_lettres['voyelles_toniques'] in syllabes[0]:
            #Gestion de A tonique
            if 'Á' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'Á':
                        #Loi de Bartsh
                        if char[-2] in ['C', 'X', 'T']:
                            changements.append('ie')
                        else:
                            if syllabes[1][0] + syllabes[1][1] == 'BR':
                                if syllabes[1][2] == 'I':
                                    if syllabes[2][0] == 'C':
                                        changements.append('o')
                                    else:
                                        changements.append(vocalisme.syllabe_ouverte(char[-1]))
                                else:
                                    changements.append(vocalisme.syllabe_ouverte(char[-1]))
                            else:
                                changements.append(vocalisme.syllabe_ouverte(char[-1]))
                    elif char[-2] == 'Á':
                            #Influence des nasales
                            if char[-1] in listes_lettres[consonnes_nasales]:
                                changements.append('ai')
                            elif char[-1] in listes_lettres['consonnes_liquides']:
                                if char[-3] in listes_lettres['consonnes']:
                                    changements.append('')
                                else:
                                    changements.append(vocalisme.syllabe_fermee(char[-2])
                            else:
                                changements.append(vocalisme.syllabe_fermee(char[-2]))
                    elif char[-3] == 'Á':
                        changements.append(vocalisme.syllabe_fermee(char[-3]))

            #Gestion du E fermé
            if 'Ẹ' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'Ẹ':
                        if syllabes[1][0] in listes_lettres['consonnes_nasales']:
                            changements.append('e')
                        elif syllabes[-1][-1] == 'Í':
                            channgements.append('i')
                        else:
                            changements.append(vocalisme.syllabe_ouverte(char[-1]))
                    elif char[-2] == 'Ẹ':
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.syllabe_fermee(char[-2]))
                        elif syllabes[0][-1] in listes_lettres['consonnes_nasales']:
                            changements.append('e')
                        elif syllabes[-1][-1] == 'Í':
                            channgements.append('i')
                        else:
                            changements.append(vocalisme.syllabe_ouverte(char[-2]))
                    elif char[-3] == 'Ẹ':
                        changements.append(vocalisme.syllabe_fermee(char[-3]))
                    else:
                        pass

            #Gestion du E ouvert
            if 'Ę' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'Ę':
                        #Influence des nasales
                        if syllabes[1][0] in listes_lettres['consonnes_nasales']:
                            changements.append('ie')
                        else:
                            changements.append(vocalisme.syllabe_ouverte(char[-1]))
                    elif char[-2] == 'Ę':
                        #Si la voyelle se trouve entre une consonne et une liquide
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.syllabe_fermee(char[-2]))
                        #Influence des nasales
                        elif syllabes[0][-1] in listes_lettres['consonnes_nasales']:
                            changements.append('ie')
                        else:
                            changements.append(vocalisme.syllabe_fermee(char[-2]))
                    elif char[-3] == 'Ę':
                        changements.append(vocalisme.syllabe_fermee(char[-3]))

            #Gestion de I tonique
            elif 'Í' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'Í':
                        changements.append(vocalisme.syllabe_ouverte(char[-1]))
                    elif char[-2] == 'Í':
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.syllabe_fermee(char[-2])
                    elif char[-3] == 'Í':
                        changements.append(vocalisme.syllabe_fermee(char[-3]))

            #Gestion de O fermé
            if 'Ọ' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'Ọ':
                        if syllabes[1] == ['FU']:
                            changements.append('io')
                        else:
                            changements.append(vocalisme.syllabe_ouverte(char[-1]))
                    elif char[-2] == 'Ọ':
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.syllabe_fermee(char[-2]))
                        else:
                            changements.append(vocalisme.syllabe_fermee(char[-2]))
                    elif char[-3] == 'Ọ':
                        changements.append(vocalisme.syllabe_fermee(char[-3]))

            #Gestion de O ouvert
            elif 'Ǫ' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'Ǫ':
                        changements.append(vocalisme.syllabe_ouverte(char[-1]))
                    elif char[-2] == 'Ǫ':
                        if char[-1] in listes_lettres['consonnes_liquides']:
                            if char[-3] in listes_lettres['consonnes']:
                                changements.append('')
                            else:
                                changements.append(vocalisme.syllabe_fermee(char[-2])
                    elif char[-3] == 'Ǫ':
                        changements.append(vocalisme.syllabe_fermee(char[-3]))

            #Gestion de U
            elif 'Ú' in syllabes[0]:
                for char in syllabes:
                    if char[-1] == 'Ú':
                        changements.append(vocalisme.syllabe_ouverte(char[-1]))
                    elif char[-2] == 'Ú':
                        changements.append(vocalisme.syllabe_fermee(char[-2]))
                    elif char[-3] == 'Ú':
                        changements.append(vocalisme.syllabe_fermee(char[-3]))

        #Gestion du consonantisme implosif
            #Gestion de B
            #Gestion de C
            #Gestion de D
            #Gestion  de F
            #Gestion  de G
            #Gestion de J
            #Gestion de K
            #Gestion de P
            #Gestion de Q
            #Gestion de S
            #Gestion de T
            #Gestion de V
            #Gestion de X

            #Gestion de H

            #Gestion  de L
            #Gestion de R

            #Gestion  de M
            #Gestion de N

            #Gestion de W
            #Gestion de Y

        return changements
