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
'toutes_les_voyelles' : ["A", "Á", "E", "Ẹ", "Ę", "I", "Í", "Ī", "O", "Ǫ", "Ọ", "U", "Ú"],

'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í'],

'voyelles_atones' : ["A", "E", "U", "I", "O"],

'voyelles_atones_sans_A' : ["E", "U", "I", "O"],

'voyelles_palatales': ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í'],

'voyelles_vélaires' : ['O', "Ǫ", "Ọ", 'U', "Ú",],

'consonnes' : ["T", "P", "S", "D", "F", "G", "C", "B", 'V', 'K', 'Q', 'J', 'X'],

'consonnes_liquides' : ["R", "L"],

'consonnes_nasales' : ["M", "N"],

'yod_et_wau' : ["W", "Y"],

'consonantisme_explosif_complexe' : [
'BR', 'PR', 'VR', 'DR', 'TR', 'CR', 'GR',
'BL', 'FL', 'PL', 'DL', 'TL', 'CL', 'GL',
'BW', 'PW', 'VW', 'DW', 'SW', 'TW', 'CW', 'GW', 'QW',
'BJ', 'FJ', 'PJ', 'VJ', 'DJ', 'SJ', 'TJ', 'CJ', 'GJ',
],

'consonantisme_implosif_complexe': [],

'suffixes' : ['ÁRIU', 'DON', 'JAN'],

'prefixes': ['AD'],

'désinences_présent': ['BET', 'CET', 'DET', 'NIT', 'TET', 'VET'],

'désinences_futur': ['BO'],

'désinences_passé': ['RUNT'],

'désinences_subjonctif': ['CEM']

}

class SyllabeAntePenultieme:

    def __init__(self):
        return

    def syllabe_ante_penultieme(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Gestion du consonantisme explosif
        #En premier lieu, nous devons vérifier la longueur de de la syllabe, car si elle fait un caractère de longueur, ce dernier est automatiquement une voyelle
        if len(syllabes[-3]) == 1:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[-3][0] + syllabes[-3][1] in listes_lettres['consonantisme_explosif_complexe']:
                #Premier groupe avec R en deuxième position
                #Les labiales combinées avec R évoluent toutes vers [vr] p.40.
                if syllabes[-3][0] + syllabes[-3][1] in ['BR', 'PR', 'VR']:
                    changements.append('v' + syllabes[-3][1])
                #Les dentales combinées avec R se simplifient p.40-41
                elif syllabes[-3][0] + syllabes[-3][1] in ['DR', 'TR']:
                    changements.append(syllabes[-3][1])
                #Les palatales combinées avec R s'affaiblissent toutes en [ir] p.41
                elif syllabes[-3][0] + syllabes[-3][1] in ['CR', 'GR']:
                    if syllabes[-4][-1] and syllabes[-3][2] in ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í']:
                        changements.append('gr')
                    else:
                        changements.append('i' + syllabes[-3][1])
                #Deuxième groupe avec L en deuxième position
                #Les labiales combinées avec L subissent des évolutions
                #qui peuvent aller du maintien à la spirantisation en passant par le redoublement p.41
                elif syllabes[-3][0] + syllabes[-3][1] in ['BL', 'FL', 'PL']:
                    changements.append(syllabes[-3][0] + syllabes[-3][1])
                #Les dentales combinées avec L connaissent différentes évolutions p.42
                elif syllabes[-3][0] + syllabes[-3][1] in ['DL', 'TL']:
                    if syllabes[-3][0] == 'T':
                        changements.append('ill')
                    elif syllabes[-3][0] == 'D':
                        changements.append(syllabes[-3][1])
                #Les palatales combinées avec L aboutissent toutes à un l mouillé p.42
                elif syllabes[-3][0] + syllabes[-3][1] in ['CL', 'GL']:
                    changements.append('ill')
                #Troisième groupe avec un wau (W) en deuxième position
                #Les labiales combinée au wau aboutissent à un amuïssement
                #en arrondissant la voyelle tonique qui suit ou qui précède p.43
                elif syllabes[-3][0] + syllabes[-3][1] in ['BW', 'PW', 'VW']:
                    changements.append('')
                #Les dentales combinées au wau constituent des séquences complexes
                #la geminée s'amuit p.43
                elif syllabes[-3][0] + syllabes[-3][1] in ['DW', 'TW', 'SW']:
                    changements.append('u')
                #Les vélaires avec un wau sont réparties en deux catégories p.44
                elif syllabes[-3][0] + syllabes[-3][1] in ['CW', 'GW', 'QW']:
                    #la plus ancienne (QW) se prolonge généralement en [v]
                    if syllabes[-3][0] + syllabes[-3][1] == 'QW':
                        #En final et devant -s ou -t
                        if syllabes[-3][1] == syllabes[-2][-1] or syllabes[-3][2] in ['S', 'T'] or syllabes[-2][0] in ['S', 'T']:
                            changements.append('u')
                        else:
                            changements.append('v')
                    #Les deux autres subissent un affaiblissement
                    else:
                        if syllabes[-3][2] == 'T' or syllabes[-2][0] == 'T':
                            changements.append('')
                        else:
                            changements.append('u')
                #Quatrième groupe avec un yod (J) en deuxième position
                #Les labiales combinées au yod subissent une évolution différente
                #La sourde  se redouble et voit la semi-voyelle se durcir
                #Les sonores tiennent compte de l'entourage vocalique p.44
                elif syllabes[-3][0] + syllabes[-3][1] in ['BJ', 'PJ', 'VJ']:
                    if syllabes[-3][0] + syllabes[-3][1] == 'PJ':
                        changements.append('ch')
                    else:
                        #En milieu paltal
                        if syllabes[-4][-1] in listes_lettres['voyelles_palatales']:
                            changements.append('g')
                        #En milieu vélaire
                        elif syllabes[-4][-1] in listes_lettres['voyelles_vélaires']:
                            changements.append('i')
                #Les dentales combinées à un yod connaissent trois évolutions différentes p.45
                elif syllabes[-3][0] + syllabes[-3][1] in ['TJ', 'DJ', 'SJ']:
                    #L'occlusive sourde s'assibile et se sonorise
                    if syllabes[-3][0] + syllabes[-3][1] == 'TJ':
                        #Entre deux A
                        if syllabes[-4][-1] in ['Á', 'A'] and syllabes[-2][0] in ['Á', 'A']:
                            changements.append('i')
                        else:
                            changements.append('is')
                    #L'occlusive sonore s'assimile au yod  puis se simplifie
                    elif syllabes[-3][0] + syllabes[-3][1] == 'DJ':
                        changements.append('i')
                    #La sifflante se palatalise et se sonorise
                    elif syllabes[-3][0] + syllabes[-3][1] == 'SJ':
                        changements.append('is')
                #Les palatales combinées au yod se redoublent
                elif syllabes[-3][0] + syllabes[-3][1] in ['CJ', 'GJ']:
                    if syllabes[-3][0] + syllabes[-3][1] == 'CJ':
                        changements.append('c')
                    #La palatale sourde s'assibile encore
                    elif syllabes[-3][0] + syllabes[-3][1] == 'GJ':
                        changements.append('i')

            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme explosif
            elif syllabes[-3][0] in listes_lettres['consonnes']:
                #Gestion de B
                #L'occlusive labiale sonore se spirantise puis suit une évolution selon son entourage
                if syllabes[-3][0] == 'B':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-4][-1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-3][1] in listes_lettres['voyelles_palatales']:
                                if syllabes[-3][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                            else:
                                if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                        #En milieu vélaire
                        elif syllabes[-4][-1] in listes_lettres['voyelles_vélaires']:
                            if syllabes[-3][1] in listes_lettres['voyelles_vélaires']:
                                if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                            else:
                                if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                    else:
                        changements.append(syllabes[-3][0])

                #Gestion de C
                elif syllabes[-3][0] == 'C':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][1] in ['E', "Ẹ", "Ę", 'I', 'Í']:
                            if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('z')
                            else:
                                changements.append('s')
                        elif syllabes[-3][1] in ['A', 'Á']:
                            if syllabes[-4][-1] in ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í']:
                                if syllabes[-4][-1] in ['I', 'Í']:
                                    changements.append('')
                                else:
                                    changements.append('i')
                            elif syllabes[-4][-1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                                changements.append('')
                        elif syllabes[-3][1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                            changements.append('')
                    else:
                        if syllabes[-3][1] in ['A', 'Á']:
                            changements.append('ch')
                        else:
                            changements.append('c')

                #Gestion de D
                elif syllabes[-3][0] == 'D':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][1] == syllabes[-3][-1] == syllabes[-2][-1] in listes_lettres['voyelles_atones']:
                            if syllabes[-2][0] == 'S':
                                changements.append('t')
                            else:
                                changements.append('')
                        elif syllabes[-3][1] == 'T':
                            changements.append('')
                    else:
                        changements.append(syllabes[-3][0])

                #Gestion  de F
                elif syllabes[-3][0] == 'F':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][1] in listes_lettres['voyelles_palatales']:
                            changements.append('v')
                        elif syllabes[-3][1] in listes_lettres['voyelles_vélaires']:
                            changements.append('')
                    else:
                        changements.append(syllabes[-3][0])

                #Gestion  de G
                elif syllabes[-3][0] == 'G':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][1] in ['E', "Ẹ", "Ę", 'I', 'Í']:
                            if len(syllabes[-3]) > 2:
                                if syllabes[-3][2] in ['S', 'T'] or syllabes[-2][0] in ['S', 'T']:
                                    changements.append('i')
                                else:
                                    changements.append('')
                            else:
                                if syllabes[-2][0] in ['S', 'T']:
                                    changements.append('i')
                                else:
                                    changements.append('')
                        elif syllabes[-3][1] in ['A', 'Á']:
                            if syllabes[-4][-1] in ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í']:
                                if syllabes[-4][-1] in ['I', 'Í']:
                                    changements.append('')
                                else:
                                    changements.append('i')
                            elif syllabes[-4][-1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                                if syllabes[-4][-1] in ['O', "Ǫ", "Ọ"]:
                                    changements.append('v')
                                else:
                                    changements.append('')
                        elif syllabes[-3][1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                            changements.append('')
                    else:
                        changements.append(syllabes[-3][0])

                #Gestion de J
                elif syllabes[-3][0] == 'J':
                    changements.append('j')

                #Gestion de K
                elif syllabes[-3][0] == 'K':
                    pass

                #Gestion de P
                elif syllabes[-3][0] == 'P':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-4][-1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-3][1] in listes_lettres['voyelles_palatales']:
                                if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                            else:
                                if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                        #En milieu vélaire
                        elif syllabes[-4][-1] in listes_lettres['voyelles_vélaires']:
                            if syllabes[-3][1] in listes_lettres['voyelles_vélaires']:
                                if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                            else:
                                if syllabes[-3][1] == syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                    else:
                        changements.append(syllabes[-3][0])

                #Gestion de Q
                elif syllabes[-3][0] == 'Q':
                    pass

                #Gestion de S
                elif syllabes[-3][0] == 'S':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        changements.append('s')
                    else:
                        changements.append(syllabes[-3][0])

                #Gestion de T
                elif syllabes[-3][0] == 'T':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-4][-1] in listes_lettres['voyelles_toniques']:
                            if syllabes[-3][1] == 'I':
                                changements.append('ci')
                            else:
                                changements.append('')
                        elif syllabes[-3][1] == syllabes[-3][-1] == syllabes[-2][-1] in listes_lettres['voyelles_atones']:
                            if syllabes[-2][0] == 'S':
                                changements.append('t')
                            else:
                                changements.append('')
                        elif syllabes[-3][1] == 'T':
                            changements.append('')
                        elif syllabes[-3][1] == syllabes[-3][-1] in listes_lettres['voyelles_toniques']:
                            changements.append(syllabes[-3][0])
                    else:
                        if syllabes[-4][-1] in listes_lettres['consonnes_nasales']:
                            if syllabes[-3][1] == 'I':
                                changements.append('ci')
                            else:
                                changements.append(syllabes[-3][0])
                        else:
                            changements.append(syllabes[-3][0])

                #Gestion de V
                elif syllabes[-3][0] == 'V':
                    if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-3][1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-3][1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('f')
                            elif syllabes[-3][1] in ['S', 'T']:
                                changements.append('f')
                            else:
                                changements.append('v')
                        elif syllabes[-3][1] in listes_lettres['voyelles_vélaires']:
                            changements.append('')
                    else:
                        changements.append('v')

                #Gestion de X
                elif syllabes[-3][0] == 'X':
                    pass

            elif syllabes[-3][0] in listes_lettres['consonnes_liquides']:
                #Gestion  de L
                if syllabes[-3][0] == 'L':
                    #Épenthèses avec une syllabe antérieure à une lettre
                    if len(syllabes[-4]) == 1:
                        #Épenthèse d'un b après M
                        if syllabes[-4][-1] == 'M':
                            changements.append('b'+syllabes[-3][0])
                        #Épenthèse d'un d après N
                        elif syllabes[-4][-1] == 'N':
                            changements.append('d'+syllabes[-3][0])
                        #Épenthèse d'un d après L
                        elif syllabes[-4][-1] == 'L':
                            changements.append('d'+syllabes[-3][0])
                        #Épenthèse d'un d après S sonore
                        elif syllabes[-4][-1] == 'S':
                            changements.append('d'+syllabes[-3][0])
                        else:
                            changements.append(syllabes[-3][0])
                    else:
                        #Épenthèse d'un b après M
                        if syllabes[-4][-1] == 'M':
                            changements.append('b'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "M":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('b' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un d après N
                        elif syllabes[-4][-1] == 'N':
                            changements.append('d'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "N":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('d' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un d après L
                        elif syllabes[-4][-1] == 'L':
                            changements.append('d'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "L":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('d' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un d après S sonore
                        elif syllabes[-4][-1] == 'S':
                            #Épenthèse d'un t après S sourde
                            if syllabes[-4][-2] == 'S':
                                changements.append('t')
                            else:
                                changements.append('d'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "S":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('d' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un t après S sourde
                        elif syllabes[-4][-2] == "X":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('t' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        else:
                            changements.append(syllabes[-3][0])

                #Gestion de R
                elif syllabes[-3][0] == 'R':
                    #Gestion de la syllabe précédente ne comportant qu'une syllabe
                    if len(syllabes[-4]) == 1:
                        #Épenthèse d'un b après M
                        if syllabes[-4][-1] == 'M':
                            changements.append('b'+syllabes[-3][0])
                        #Épenthèse d'un d après N
                        elif syllabes[-4][-1] == 'N':
                            changements.append('d'+syllabes[-3][0])
                        #Épenthèse d'un d après L
                        elif syllabes[-4][-1] == 'L':
                            changements.append('d'+syllabes[-3][0])
                        #Épenthèse d'un d après S sonore
                        elif syllabes[-4][-1] == 'S':
                            changements.append('d'+syllabes[-3][0])
                    else:
                        #Épenthèse d'un b après M
                        if syllabes[-4][-1] == 'M':
                            changements.append('b'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "M":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('b' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un d après N
                        elif syllabes[-4][-1] == 'N':
                            changements.append('d'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "N":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('d' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un d après L
                        elif syllabes[-4][-1] == 'L':
                            changements.append('d'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "L":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('d' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un d après S sonore
                        elif syllabes[-4][-1] == 'S':
                            #Épenthèse d'un t après S sourde
                            if syllabes[-4][-2] == 'S':
                                changements.append('t')
                            else:
                                changements.append('d'+syllabes[-3][0])
                        elif syllabes[-4][-2] == "S":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('d' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        #Épenthèse d'un t après S sourde
                        elif syllabes[-4][-2] == "X":
                            if syllabes[-4][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('t' + syllabes[-3][0])
                            else:
                                changements.append(syllabes[-3][0])
                        else:
                            changements.append(syllabes[-3][0])

            elif syllabes[-3][0] in listes_lettres['consonnes_nasales']:
                #Gestion  de M
                if syllabes[-3][0] == 'M':
                    changements.append(syllabes[-3][0])

                #Gestion de N
                elif syllabes[-3][0] == 'N':
                    changements.append(syllabes[-3][0])

                #Gestion du H germain
            if syllabes[-3][0] == 'H':
                pass

                #Gestion de W
            if syllabes[-3][0] == 'W':
                if syllabes[-4][-1] in listes_lettres['toutes_les_voyelles']:
                    if syllabes[-3][1] in listes_lettres['voyelles_palatales']:
                        if syllabes[-3][1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('f')
                        elif syllabes[-3][1] in ['S', 'T']:
                            changements.append('f')
                        else:
                            changements.append('v')
                    elif syllabes[-3][1] in listes_lettres['voyelles_vélaires']:
                        changements.append('')
                else:
                    changements.append('v')

                #Gestion de Y
            if syllabes[-3][0] == 'Y':
                pass

        #Gestion des différents vocalismes
        #Gestion des différents vocalismes
        #Si la première syllabe est un préfixe
        if syllabes[0] in listes_lettres['prefixes']:
            if syllabes[-3] == syllabes[1]:
                #Vocalisme contretonique
                #Gestion de A
                if 'A' in syllabes[-3]:
                    if syllabes[-3][-1] == 'A':
                        changements.append('a')
                    elif syllabes[-3][-2] == 'A':
                        changements.append('a')
                    elif syllabes[-3][-3] == 'A':
                        changements.append('a')

                #Gestion de E
                elif 'E' in syllabes[-3]:
                    if syllabes[-3][-1] == 'E':
                        changements.append('e')
                    elif syllabes[-3][-2] == 'E':
                        if syllabes[-3][-2] == syllabes[-3][0]:
                            if syllabes[-3][-1] == 'L':
                                changements.append('a')
                            else:
                                changements.append('e')
                        else:
                            changements.append('e')
                    elif syllabes[-3][-3] == 'E':
                        changements.append('e')

                #Gestion de I:
                elif 'I' in syllabes[-3]:
                    if syllabes[-3][-1] == 'I':
                        changements.append('i')
                    elif syllabes[-3][-2] == 'I':
                        changements.append('i')
                    elif syllabes[-3][-3] == 'I':
                        changements.append('i')


                #Gestion de O:
                elif 'O' in syllabes[-3]:
                    if syllabes[-3][-1] == 'O':
                        changements.append('o')
                    elif syllabes[-3][-2] == 'O':
                        changements.append('o')
                    elif syllabes[-3][-3] == 'O':
                        changements.append('o')


                #Gestion de U:
                elif 'U' in syllabes[-3]:
                    if syllabes[-3][-1] == 'U':
                        changements.append('u')
                    elif syllabes[-3][-2] == 'U':
                        changements.append('u')
                    elif syllabes[-3][-3] == 'U':
                        changements.append('u')

                #Vocalisme tonique
                #Gestion de A tonique
                elif 'Á' in syllabes[-3]:
                    if syllabes[-3][-1] == 'Á':
                        if len(syllabes[-3]) == 1:
                            #Avant une consonne nasale
                            if syllabes[-2][0] in listes_lettres['consonnes_nasales']:
                                changements.append('ai')
                            #En précense d'un groupe syntaxique dégageant un yod
                            elif syllabes[-4] == 'TI':
                                changements.append('a')
                            else:
                                changements.append('e')
                        else:
                            if syllabes[-2] == 'TJ':
                                changements.append('a')
                            #Avant une consonne nasale
                            elif syllabes[-2][0] in listes_lettres['consonnes_nasales']:
                                changements.append('ai')
                            #Loi de Bartsh
                            elif syllabes[-3][-2] in ['C','G']:
                                changements.append('ie')
                            else:
                                changements.append('e')
                    elif syllabes[-3][-2] == 'Á':
                        #Travail sur le mot
                        #Fermeture de la bouche en milieu monosyllabique
                        if len(syllabes) == 1:
                            if syllabes[-3][-1] == 'G' : #En ajouter d'autres, à chercher
                                changements.append('o')
                            else:
                                changements.append('a')
                        #Travail sur la syllabe en elle-même
                        elif len(syllabes[-3]) > 2:
                            if syllabes[-3][-3] in ['C', 'G']:
                                changements.append('ie')
                            else:
                                changements.append('a')
                        else:
                            changements.append('a')
                    elif syllabes[-3][-3] == 'Á':
                        if syllabes[-3][-4] in ['C', 'G']:
                            changements.append('ie')
                        else:
                            changements.append('a')

                #Gestion du E fermé
                elif 'Ẹ' in syllabes[-3]:
                    if syllabes[-3][-1] == 'Ẹ':
                        if len(syllabes) == 1:
                            changements.append('ei')
                        else:
                            #Au contact d'un I long final (Ī)
                            if syllabes[-3][0] == 'Ī':
                                changements.append('i')
                            #Influence d'un I long final (Ī)
                            elif syllabes[-1][-1] == 'Ī':
                                changements.append('ie')
                            #Au contact d'un yod geminé  ou en milieu vélaire
                            elif syllabes[-2] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                                changements.append('i')
                            #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                            if syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                                changements.append('i')
                            else:
                                changements.append('ei')
                    elif syllabes[-3][-2] == 'Ẹ':
                        changements.append('e')
                    elif syllabes[-3][-3] == 'Ẹ':
                        changements.append('e')

                #Gestion du E ouvert
                elif 'Ę' in syllabes[-3]:
                    if syllabes[-3][-1] == 'Ę':
                        #Au contact d'un I long final (Ī)
                        if syllabes[-2][0] == 'Ī':
                            changements.append('i')
                        #Influence d'un I long final (Ī)
                        elif syllabes[-1][-1] == 'Ī':
                            changements.append('ie')
                        #Au contact d'un yod geminé
                        elif syllabes[-2][0] == 'J':
                            changements.append("i")
                        #Au contact d'un yod geminé  ou en milieu vélaire
                        elif syllabes[-2] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                            changements.append('i')
                        #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                        elif syllabes[-2][0] == 'X':
                            changements.append('i')
                        else:
                            changements.append('ie')
                    elif syllabes[-3][-2] == 'Ę':
                        #Gestion des plurisyllabiques
                        if len(syllabes) > 1:
                            if syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                                changements.append('i')
                            else:
                                changements.append('e')
                        else:
                            if syllabes[-3][-1] == 'M':
                                changements.append('ie')
                            #Ouverture de la bouche
                            elif syllabes[-3][-1] == syllabes[-1][-1] == 'R':
                                changements.append('a')
                            else:
                                changements.append('e')
                    elif syllabes[-3][-3] == 'Ę':
                        changements.append('e')

                #Gestion de I tonique
                elif 'Í' in syllabes[-3]:
                    if syllabes[-3][-1] == 'Í':
                        #Fermeture face à un O final
                        if syllabes[-2][0] == syllabes[-1][-1] == 'O':
                            changements.append('u')
                        else:
                            changements.append('i')
                    elif syllabes[-3][-2] == 'Í':
                        #Influence d'une nasale
                        if syllabes[-3][-1] in listes_lettres['consonnes_nasales']:
                            #Présence d'un yod avec la nasale
                            if syllabes[-2][0] == 'Y':
                                changements.append('i')
                            else:
                                changements.append('e')
                        else:
                            changements.append('i')
                    elif syllabes[-3][-3] == 'Í':
                        changements.append('i')

                #Gestion de O fermé
                elif 'Ọ' in syllabes[-3]:
                    if syllabes[-3][-1] == 'Ọ':
                        #Influence d'une nasale
                        if syllabes[-2][0] in listes_lettres['consonnes_nasales']:
                            changements.append('o')
                        #Au contact d'un I long final
                        elif syllabes[-2][0] == 'Ī':
                            changements.append('u')
                        #Influence d'un I long final (Ī)
                        elif syllabes[-1][-1] == 'Ī':
                            changements.append('u')
                        #Au contact d'un yod geminé  ou en milieu vélaire
                        elif syllabes[-2] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                            changements.append('u')
                        #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                        elif syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                            changements.append('u')
                        else:
                            changements.append('ou')
                    elif syllabes[-3][-2] == 'Ọ':
                        changements.append('o')
                    elif syllabes[-3][-3] == 'Ọ':
                        changements.append('o')

                #Gestion de O ouvert
                elif 'Ǫ' in syllabes[-3]:
                    if syllabes[-3][-1] == 'Ǫ':
                        #Influence d'un I long final (Ī)
                        if syllabes[-1][-1] == 'Ī':
                            changements.append('oi')
                        #Au contact d'un yod geminé
                        elif syllabes[-2][0] == 'J':
                            changements.append("ui")
                        #Au contact d'un yod geminé  ou en milieu vélaire
                        elif syllabes[-2] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                            changements.append('ui')
                        #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                        elif syllabes[-2][0] == 'X':
                            changements.append('ui')
                        else:
                            changements.append('ue')
                    elif syllabes[-3][-2] == 'Ǫ':
                        if len(syllabes) > 1:
                            #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                            if syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                                changements.append('ui')
                            else:
                                changements.append('o')
                        else:
                            changements.append('o')
                    elif syllabes[-3][-3] == 'Ǫ':
                        changements.append('o')

                #Gestion de U
                elif 'Ú' in syllabes[-3]:
                    if syllabes[-3][-1] == 'Ú':
                        changements.append('u')
                    elif syllabes[-3][-2] == 'Ú':
                        changements.append('u')
                    elif syllabes[-3][-3] == 'Ú':
                        changements.append('u')

        #S'il n'y a pas de préfixes
        else:
            #Vocalisme contretonique
            #Gestion de A
            if 'A' in syllabes[-3]:
                if syllabes[-3][-1] == 'A':
                    changements.append('e')
                elif syllabes[-3][-2] == 'A':
                    changements.append('e')
                elif syllabes[-3][-3] == 'A':
                    changements.append('e')

            #Gestion de E
            if 'E' in syllabes[-3]:
                if syllabes[-3][-1] == 'E':
                    changements.append('')
                elif syllabes[-3][-2] == 'E':
                    changements.append('')
                elif syllabes[-3][-3] == 'E':
                    changements.append('')

            #Gestion de I:
            if 'I' in syllabes[-3]:
                if syllabes[-3][-1] == 'I':
                    changements.append('')
                elif syllabes[-3][-2] == 'I':
                    changements.append('')
                elif syllabes[-3][-3] == 'I':
                    changements.append('')


            #Gestion de O:
            if 'O' in syllabes[-3]:
                if syllabes[-3][-1] == 'O':
                    changements.append('')
                elif syllabes[-3][-2] == 'O':
                    changements.append('')
                elif syllabes[-3][-3] == 'O':
                    changements.append('')


            #Gestion de U:
            if 'U' in syllabes[-3]:
                if syllabes[-3][-1] == 'U':
                    changements.append('')
                elif syllabes[-3][-2] == 'U':
                    changements.append('')
                elif syllabes[-3][-3] == 'U':
                    changements.append('')

            #Vocalisme tonique
            #Gestion de A tonique
            if 'Á' in syllabes[-3]:
                if syllabes[-3][-1] == 'Á':
                    if len(syllabes[-3]) == 1:
                        #Avant une consonne nasale
                        if syllabes[-2][0] in listes_lettres['consonnes_nasales']:
                            changements.append('ai')
                        #En présense d'un groupe syntaxique dégageant un yod
                        elif syllabes[-4] == 'TI':
                            changements.append('a')
                        else:
                            changements.append('e')
                    else:
                        if syllabes[-2] == 'TJ':
                            changements.append('a')
                        #Avant une consonne nasale
                        elif syllabes[-2][0] in listes_lettres['consonnes_nasales']:
                            changements.append('ai')
                        #Loi de Bartsch
                        elif syllabes[-3][-2] in ['C', 'G']:
                            changements.append('ie')
                        else:
                            changements.append('e')
                elif syllabes[-3][-2] == 'Á':
                    if syllabes[-3][-3] in ['C', 'G']:
                        changements.append('ie')
                    else:
                        changements.append('a')
                elif syllabes[-3][-3] == 'Á':
                    if syllabes[-3][-4] in ['C', 'G']:
                        changements.append('ie')
                    else:
                        changements.append('a')

            #Gestion du E fermé
            if 'Ẹ' in syllabes[-3]:
                if syllabes[-3][-1] == 'Ẹ':
                    #Influence d'un I long final (Ī)
                    if syllabes[-1][-1] == 'Ī':
                        changements.append('ie')
                    #Au contact d'un yod geminé  ou en milieu vélaire
                    elif syllabes[-2] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                        changements.append('i')
                    #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                    if syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                        changements.append('i')
                    else:
                        changements.append('ei')
                elif syllabes[-3][-2] == 'Ẹ':
                    changements.append('e')
                elif syllabes[-3][-3] == 'Ẹ':
                    changements.append('e')

            #Gestion du E ouvert
            if 'Ę' in syllabes[-3]:
                if syllabes[-3][-1] == 'Ę':
                    #Influence d'un I long final (Ī)
                    if syllabes[-2][-1] == 'Ī':
                        changements.append('ie')
                    #Au contact d'un yod geminé
                    elif syllabes[-2][0] == 'J':
                        changements.append("i")
                    #Au contact d'un yod geminé  ou en milieu vélaire
                    elif syllabes[-2] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                        changements.append('i')
                    #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                    elif syllabes[-2][0] == 'X':
                        changements.append('i')
                    else:
                        changements.append('ie')
                elif syllabes[-3][-2] == 'Ę':
                    if syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                        changements.append('i')
                    else:
                        changements.append('e')
                elif syllabes[-3][-3] == 'Ę':
                    changements.append('e')

            #Gestion de I tonique
            if 'Í' in syllabes[-3]:
                if syllabes[-3][-1] == 'Í':
                    changements.append('i')
                elif syllabes[-3][-2] == 'Í':
                    #Influence d'une nasale
                    if syllabes[-3][-1] in listes_lettres['consonnes_nasales']:
                        changements.append('e')
                    else:
                        changements.append('i')
                elif syllabes[-3][-3] == 'Í':
                    changements.append('i')

            #Gestion de O fermé
            if 'Ọ' in syllabes[-3]:
                if syllabes[-3][-1] == 'Ọ':
                    #Influence d'une nasale
                    if syllabes[-2][0] in listes_lettres['consonnes_nasales']:
                        changements.append('o')
                    #Au contact d'un I long final
                    if syllabes[-2][0] == 'Ī':
                        changements.append('u')
                    #Influence d'un I long final (Ī)
                    elif syllabes[-2][-1] == 'Ī':
                        changements.append('u')
                    #Au contact d'un yod geminé  ou en milieu vélaire
                    elif syllabes[-3] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                        changements.append('u')
                    #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                    if syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                        changements.append('u')
                    else:
                        changements.append('ou')
                elif syllabes[-3][-2] == 'Ọ':
                    changements.append('o')
                elif syllabes[-3][-3] == 'Ọ':
                    changements.append('o')

            #Gestion de O ouvert
            if 'Ǫ' in syllabes[-3]:
                if syllabes[-3][-1] == 'Ǫ':
                    #Au contact d'un yod geminé
                    if syllabes[-2][0] == 'J':
                        changements.append("ui")
                    #Au contact d'un yod geminé  ou en milieu vélaire
                    elif syllabes[-2] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                        changements.append('ui')
                    #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                    elif syllabes[-2][0] == 'X':
                        changements.append('ui')
                    else:
                        changements.append('ue')
                elif syllabes[-3][-2] == 'Ǫ':
                    #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                    if syllabes[-3][-1] + syllabes[-2][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                        changements.append('ui')
                    else:
                        changements.append('o')
                elif syllabes[-3][-3] == 'Ǫ':
                    changements.append('o')

            #Gestion de U
            if 'Ú' in syllabes[-3]:
                if syllabes[-3][-1] == 'Ú':
                    changements.append('u')
                elif syllabes[-3][-2] == 'Ú':
                    changements.append('u')
                elif syllabes[-3][-3] == 'Ú':
                    changements.append('u')

        #Idem ici, la machine doit d'abord vérifier la longueur de la syllabe pour savoir si elle est uniquement composée d'une voyelle ou d'autre chose.
        if len(syllabes[-3]) == 1:
            pass
        elif syllabes[-3] in listes_lettres['désinences_subjonctif']:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[-3][-2] + syllabes[-3][-1] in listes_lettres['consonantisme_implosif_complexe']:
                pass

            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme implosif
            elif syllabes[-3][-1] in listes_lettres['consonnes']:
                pass
                #Gestion de B
                if syllabes[-3][-1] == 'B':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de C
                elif syllabes[-3][-1] == 'C':
                    #spirantisation
                    changements.append('i')
                #Gestion de D
                elif syllabes[-3][-1] == 'D':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion  de F
                elif syllabes[-3][-1] == 'F':
                    changements.append('')
                #Gestion  de G
                elif syllabes[-3][-1] == 'G':
                    #Après I et E
                    if syllabes[-3][-2] in ["Ẹ", "Ę", 'E', 'I', 'Í']:
                        changements.append('i')
                    else:
                        changements.append('u')
                #Gestion de J
                elif syllabes[-3][-1] == 'J':
                    pass
                #Gestion de K
                elif syllabes[-3][-1] == 'K':
                    pass
                #Gestion de P
                elif syllabes[-3][-1] == 'P':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de Q
                elif syllabes[-3][-1] == 'Q':
                    pass
                #Gestion de S
                elif syllabes[-3][-1] == 'S':
                    changements.append(syllabes[-3][-1])
                #Gestion de T
                elif syllabes[-3][-1] == 'T':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de V
                elif syllabes[-3][-1] == 'V':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de X
                elif syllabes[-3][-1] == 'X':
                    pass

            elif syllabes[-3][-1] in listes_lettres['consonnes_liquides']:
                pass
                #Gestion  de L
                if syllabes[-3][-1] == 'L':
                    #Gestion d'un plurisyllabiques
                    if syllabes[-2][0] == 'W':
                        #Vocalisation en W
                        changements.append('u')
                    #L devant M
                    elif syllabes[-2][0] == 'M':
                        changements.append(syllabes[-3][-1])
                    #L face à Y
                    elif syllabes[-2][0] == 'Y':
                        #Différentiation entre le féminin et le masculin
                        if syllabes[-2][1] == syllabes[-1][-1] == 'A':
                            changements.append(syllabes[-3][-1] + syllabes[-3][-1])
                        else:
                            changements.append(syllabes[-3][-1])
                    else:
                        changements.append('')
                #Gestion de R
                elif syllabes[-3][-1] == 'R':
                    changements.append(syllabes[-3][-1])

            elif syllabes[-3][-1] in listes_lettres['consonnes_nasales']:
                pass
                #Gestion  de M
                if syllabes[-3][-1] == 'M':
                    changements.append(syllabes[-3][-1])
                #Gestion de N
                elif syllabes[-3][-1] == 'N':
                    changements.append(syllabes[-3][-1])

                #Gestion de H

                #Gestion de W
                #Gestion de Y

        return changements
