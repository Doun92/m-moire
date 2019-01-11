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

class SyllabeContrepenultieme:

    def __init__(self):
        return

    def syllabe_contrepenultieme(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Gestion du consonantisme explosif
        #En premier lieu, nous devons vérifier la longueur de de la syllabe, car si elle fait un caractère de longueur, ce dernier est automatiquement une voyelle
        if len(syllabes[-2]) == 1:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[-2][0] + syllabes[-2][1] in listes_lettres['consonantisme_explosif_complexe']:
                #Premier groupe avec R en deuxième position
                #Les labiales combinées avec R évoluent toutes vers [vr] p.40.
                if syllabes[-2][0] + syllabes[-2][1] in ['BR', 'PR', 'VR']:
                    changements.append('v' + syllabes[-2][1])
                #Les dentales combinées avec R se simplifient p.40-41
                elif syllabes[-2][0] + syllabes[-2][1] in ['DR', 'TR']:
                    changements.append(syllabes[-2][1])
                #Les palatales combinées avec R s'affaiblissent toutes en [ir] p.41
                elif syllabes[-2][0] + syllabes[-2][1] in ['CR', 'GR']:
                    changements.append('i' + syllabes[-2][1])
                #Deuxième groupe avec L en deuxième position
                #Les labiales combinées avec L subissent des évolutions
                #qui peuvent aller du maintien à la spirantisation en passant par le redoublement p.41
                elif syllabes[-2][0] + syllabes[-2][1] in ['BL', 'FL', 'PL']:
                    changements.append(syllabes[-2][0] + syllabes[-2][1])
                #Les dentales combinées avec L connaissent différentes évolutions p.42
                elif syllabes[-2][0] + syllabes[-2][1] in ['DL', 'TL']:
                    if syllabes[-2][0] == 'T':
                        changements.append('ill')
                    elif syllabes[-2][0] == 'D':
                        changements.append(syllabes[-2][1])
                #Les palatales combinées avec L aboutissent toutes à un l mouillé p.42
                elif syllabes[-2][0] + syllabes[-2][1] in ['CL', 'GL']:
                    changements.append('ill')
                #Troisième groupe avec un wau (W) en deuxième position
                #Les labiales combinée au wau aboutissent à un amuïssement
                #en arrondissant la voyelle tonique qui suit ou qui précède p.43
                elif syllabes[-2][0] + syllabes[-2][1] in ['BW', 'PW', 'VW']:
                    changements.append('')
                #Les dentales combinées au wau constituent des séquences complexes
                #la geminée s'amuit p.43
                elif syllabes[-2][0] + syllabes[-2][1] in ['DW', 'TW', 'SW']:
                    changements.append('u')
                #Les vélaires avec un wau sont réparties en deux catégories p.44
                elif syllabes[-2][0] + syllabes[-2][1] in ['CW', 'GW', 'QW']:
                    #la plus ancienne (QW) se prolonge généralement en [v]
                    if syllabes[-2][0] + syllabes[-2][1] == 'QW':
                        #En final et devant -s ou -t
                        if syllabes[-2][1] == syllabes[-1][-1] or syllabes[-2][2] in ['S', 'T'] or syllabes[-1][0] in ['S', 'T']:
                            changements.append('u')
                        else:
                            changements.append('v')
                    #Les deux autres subissent un affaiblissement
                    else:
                        if syllabes[-2][2] == 'T' or syllabes[-1][0] == 'T':
                            changements.append('')
                        else:
                            changements.append('u')
                #Quatrième groupe avec un yod (J) en deuxième position
                #Les labiales combinées au yod subissent une évolution différente
                #La sourde  se redouble et voit la semi-voyelle se durcir
                #Les sonores tiennent compte de l'entourage vocalique p.44
                elif syllabes[-2][0] + syllabes[-2][1] in ['BJ', 'PJ', 'VJ']:
                    if syllabes[-2][0] + syllabes[-2][1] == 'PJ':
                        changements.append('ch')
                    else:
                        #En milieu paltal
                        if syllabes[-3][-1] in listes_lettres['voyelles_palatales']:
                            changements.append('g')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in listes_lettres['voyelles_vélaires']:
                            changements.append('i')
                #Les dentales combinées à un yod connaissent trois évolutions différentes p.45
                elif syllabes[-2][0] + syllabes[-2][1] in ['TJ', 'DJ', 'SJ']:
                    #L'occlusive sourde s'assibile et se sonorise
                    if syllabes[-2][0] + syllabes[-2][1] == 'TJ':
                        changements.append('is')
                    #L'occlusive sonore s'assimile au yod  puis se simplifie
                    elif syllabes[-2][0] + syllabes[-2][1] == 'DJ':
                        changements.append('i')
                    #La sifflante se palatalise et se sonorise
                    elif syllabes[-2][0] + syllabes[-2][1] == 'SJ':
                        changements.append('is')
                #Les palatales combinées au yod se redoublent
                elif syllabes[-2][0] + syllabes[-2][1] in ['CJ', 'GJ']:
                    if syllabes[-2][0] + syllabes[-2][1] == 'CJ':
                        changements.append('c')
                    #La palatale sourde s'assibile encore
                    elif syllabes[-2][0] + syllabes[-2][1] == 'GJ':
                        changements.append('i')

            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme explosif
            elif syllabes[-2][0] in listes_lettres['consonnes']:
                #Gestion de B
                #L'occlusive labiale sonore se spirantise puis suit une évolution selon son entourage
                if syllabes[-2][0] == 'B':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-3][-1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-2][1] in listes_lettres['voyelles_palatales']:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                            else:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in listes_lettres['voyelles_vélaires']:
                            if syllabes[-2][1] in listes_lettres['voyelles_vélaires']:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                            else:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')

                #Gestion de C
                elif syllabes[-2][0] == 'C':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] in ['E', "Ẹ", "Ę", 'I', 'Í']:
                            if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('z')
                            else:
                                changements.append('s')
                        elif syllabes[-2][1] in ['A', 'Á']:
                            if syllabes[-3][-1] in ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í']:
                                if syllabes[-3][-1] in ['I', 'Í']:
                                    changements.append('')
                                else:
                                    changements.append('i')
                            elif syllabes[-3][-1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                                changements.append('')
                        elif syllabes[-2][1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                            changements.append('')
                    else:
                        if syllabes[-2][1] in ['A', 'Á']:
                            changements.append('ch')
                        else:
                            changements.append('c')

                #Gestion de D
                elif syllabes[-2][0] == 'D':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] == syllabes[-2][-1] == syllabes[-1][-1] in listes_lettres['voyelles_atones']:
                            if syllabes[-1][0] == 'S':
                                changements.append('t')
                            else:
                                changements.append('')
                        elif syllabes[-2][1] == 'T':
                            changements.append('')

                #Gestion  de F
                elif syllabes[-2][0] == 'F':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] in listes_lettres['voyelles_palatales']:
                            changements.append('v')
                        elif syllabes[-2][1] in listes_lettres['voyelles_vélaires']:
                            changements.append('')

                #Gestion  de G
                elif syllabes[-2][0] == 'G':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] in ['E', "Ẹ", "Ę", 'I', 'Í']:
                                if syllabes[-2][2] in ['S', 'T'] or syllabes[-1][0] in ['S', 'T']:
                                    changements.append('i')
                                else:
                                    changements.append('')
                        elif syllabes[-2][1] in ['A', 'Á']:
                            if syllabes[-3][-1] in ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í']:
                                if syllabes[-3][-1] in ['I', 'Í']:
                                    changements.append('')
                                else:
                                    changements.append('i')
                            elif syllabes[-3][-1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                                if syllabes[-3][-1] in ['O', "Ǫ", "Ọ"]:
                                    changements.append('v')
                                else:
                                    changements.append('')
                        elif syllabes[-2][1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                            changements.append('')

                #Gestion de J
                elif syllabes[-2][0] == 'J':
                    changements.append('j')

                #Gestion de K
                elif syllabes[-2][0] == 'K':
                    pass

                #Gestion de P
                elif syllabes[-2][0] == 'P':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-3][-1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-2][1] in listes_lettres['voyelles_palatales']:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                            else:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                        #En milieu vélaire
                        elif syllabes[-3][-1] in listes_lettres['voyelles_vélaires']:
                            if syllabes[-2][1] in listes_lettres['voyelles_vélaires']:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('')
                            else:
                                if syllabes[-2][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')

                #Gestion de Q
                elif syllabes[-2][0] == 'Q':
                    pass

                #Gestion de S
                elif syllabes[-2][0] == 'S':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        changements.append('s')

                #Gestion de T
                elif syllabes[-2][0] == 'T':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] == syllabes[-2][-1] == syllabes[-1][-1] in listes_lettres['voyelles_atones']:
                            if syllabes[-1][0] == 'S':
                                changements.append('t')
                            else:
                                changements.append('')
                        elif syllabes[-2][1] == 'T':
                            changements.append('')

                #Gestion de V
                elif syllabes[-2][0] == 'V':
                    if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-2][1] in listes_lettres['voyelles_atones_sans_A']:
                                changements.append('f')
                            elif syllabes[-2][1] in ['S', 'T']:
                                changements.append('f')
                            else:
                                changements.append('v')
                        elif syllabes[-2][1] in listes_lettres['voyelles_vélaires']:
                            changements.append('')
                    else:
                        changements.append('v')

                #Gestion de X
                elif syllabes[-2][0] == 'X':
                    pass

            elif syllabes[-2][0] in listes_lettres['consonnes_liquides']:
                #Gestion  de L
                if syllabes[-2][0] == 'L':
                    #Épenthèse d'un b après M
                    if syllabes[-3][-1] == 'M':
                        changements.append('b'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "M":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('b' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un d après N
                    if syllabes[-3][-1] == 'N':
                        changements.append('d'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "N":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un d après L
                    if syllabes[-3][-1] == 'L':
                        changements.append('d'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "L":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un d après S sonore
                    if syllabes[-3][-1] == 'S':
                        #Épenthèse d'un t après S sourde
                        if syllabes[-3][-2] == 'S':
                            changements.append('t')
                        else:
                            changements.append('d'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "S":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un t après S sourde
                    elif syllabes[-3][-2] == "X":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('t' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])

                #Gestion de R
                elif syllabes[-2][0] == 'R':
                    #Épenthèse d'un b après M
                    if syllabes[-3][-1] == 'M':
                        changements.append('b'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "M":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('b' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un d après N
                    if syllabes[-3][-1] == 'N':
                        changements.append('d'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "N":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un d après L
                    if syllabes[-3][-1] == 'L':
                        changements.append('d'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "L":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un d après S sonore
                    if syllabes[-3][-1] == 'S':
                        #Épenthèse d'un t après S sourde
                        if syllabes[-3][-2] == 'S':
                            changements.append('t')
                        else:
                            changements.append('d'+syllabes[-2][0])
                    elif syllabes[-3][-2] == "S":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])
                    #Épenthèse d'un t après S sourde
                    elif syllabes[-3][-2] == "X":
                        if syllabes[-3][-1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('t' + syllabes[-2][0])
                        else:
                            changements.append(syllabes[-2][0])

            elif syllabes[-2][0] in listes_lettres['consonnes_nasales']:
                #Gestion  de M
                if syllabes[-2][0] == 'M':
                    changements.append(syllabes[-2][0])

                #Gestion de N
                elif syllabes[-2][0] == 'N':
                    changements.append(syllabes[-2][0])

                #Gestion du H germain
            if syllabes[-2][0] == 'H':
                pass

                #Gestion de W
            if syllabes[-2][0] == 'W':
                if syllabes[-3][-1] in listes_lettres['toutes_les_voyelles']:
                    if syllabes[-2][1] in listes_lettres['voyelles_palatales']:
                        if syllabes[-2][1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('f')
                        elif syllabes[-2][1] in ['S', 'T']:
                            changements.append('f')
                        else:
                            changements.append('v')
                    elif syllabes[-2][1] in listes_lettres['voyelles_vélaires']:
                        changements.append('')
                else:
                    changements.append('v')

                #Gestion de Y
            if syllabes[-2][0] == 'Y':
                pass

        #Gestion des différents vocalismes
        #Vocalisme contretonique
        #Gestion de A
        if 'A' in syllabes[-2]:
            if syllabes[-2][-1] == 'A':
                changements.append('e')
            elif syllabes[-2][-2] == 'A':
                changements.append('e')
            elif syllabes[-2][-3] == 'A':
                changements.append('e')

        #Gestion de E
        if 'E' in syllabes[-2]:
            if syllabes[-2][-1] == 'E':
                changements.append('')
            elif syllabes[-2][-2] == 'E':
                changements.append('')
            elif syllabes[-2][-3] == 'E':
                changements.append('')

        #Gestion de I:
        if 'I' in syllabes[-2]:
            if syllabes[-2][-1] == 'I':
                changements.append('')
            elif syllabes[-2][-2] == 'I':
                changements.append('')
            elif syllabes[-2][-3] == 'I':
                changements.append('')


        #Gestion de O:
        if 'O' in syllabes[-2]:
            if syllabes[-2][-1] == 'O':
                changements.append('')
            elif syllabes[-2][-2] == 'O':
                changements.append('')
            elif syllabes[-2][-3] == 'O':
                changements.append('')


        #Gestion de U:
        if 'U' in syllabes[-2]:
            if syllabes[-2][-1] == 'U':
                changements.append('')
            elif syllabes[-2][-2] == 'U':
                changements.append('')
            elif syllabes[-2][-3] == 'U':
                changements.append('')


        #Vocalisme tonique
        #Gestion de A tonique
        if 'Á' in syllabes[-2]:
            if syllabes[-2][-1] == 'Á':
                if syllabes[-1][0] in listes_lettres['consonnes_nasales']:
                    changements.append('ai')
                elif syllabes[-2][-2] in ['C'. 'G']:
                    changements.append('ie')
                else:
                    changements.append('e')
            elif syllabes[-2][-2] == 'Á':
                if syllabes[-2][-3] in ['C'. 'G']:
                    changements.append('ie')
                else:
                    changements.append('a')
            elif syllabes[-2][-3] == 'Á':
                if syllabes[-2][-4] in ['C'. 'G']:
                    changements.append('ie')
                else:
                    changements.append('a')

        #Gestion du E fermé
        if 'Ẹ' in syllabes[-2]:
            if syllabes[-2][-1] == 'Ẹ':
                #Au contact d'un I long final (Ī)
                if syllabes[-1][0] == 'Ī':
                    changements.append('i')
                #Influence d'un I long final (Ī)
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('ie')
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[-1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                if syllabes[-2][-1] + syllabes[-1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('i')
                else:
                    changements.append('ei')
            elif syllabes[-2][-2] == 'Ẹ':
                changements.append('e')
            elif syllabes[-2][-3] == 'Ẹ':
                changements.append('e')

        #Gestion du E ouvert
        if 'Ę' in syllabes[-2]:
            if syllabes[-2][-1] == 'Ę':
                #Au contact d'un I long final (Ī)
                if syllabes[-1][0] == 'Ī':
                    changements.append('i')
                #Influence d'un I long final (Ī)
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('ie')
                #Au contact d'un yod geminé
                elif syllabes[-1][0] == 'J':
                    changements.append("i")
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[-1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                elif syllabes[-1][0] == 'X':
                    changements.append('i')
                else:
                    changements.append('ie')
            elif syllabes[-2][-2] == 'Ę':
                if syllabes[-2][-1] + syllabes[-1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('i')
                else:
                    changements.append('e')
            elif syllabes[-2][-3] == 'Ę':
                changements.append('e')

        #Gestion de I tonique
        if 'Í' in syllabes[-2]:
            if syllabes[-2][-1] == 'Í':
                changements.append('i')
            elif syllabes[-2][-2] == 'Í':
                #Influence d'une nasale
                if syllabes[-2][-1] in listes_lettres['consonnes_nasales']:
                    changements.append('e')
                else:
                    changements.append('i')
            elif syllabes[-2][-3] == 'Í':
                changements.append('i')

        #Gestion de O fermé
        if 'Ọ' in syllabes[-2]:
            if syllabes[-2][-1] == 'Ọ':
                #Influence d'une nasale
                if syllabes[-1][0] in listes_lettres['consonnes_nasales']:
                    changements.append('o')
                #Au contact d'un I long final
                if syllabes[-1][0] == 'Ī':
                    changements.append('u')
                #Influence d'un I long final (Ī)
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[-1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('u')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                if syllabes[-2][-1] + syllabes[-1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('u')
                else:
                    changements.append('ou')
            elif syllabes[-2][-2] == 'Ọ':
                changements.append('o')
            elif syllabes[-2][-3] == 'Ọ':
                changements.append('o')

        #Gestion de O ouvert
        if 'Ǫ' in syllabes[-2]:
            if syllabes[-2][-1] == 'Ǫ':
                #Influence d'un I long final (Ī)
                if syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                #Au contact d'un yod geminé
                elif syllabes[-1][0] == 'J':
                    changements.append("ui")
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[-1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                elif syllabes[-1][0] == 'X':
                    changements.append('ui')
                else:
                    changements.append('ue')
            elif syllabes[-2][-2] == 'Ǫ':
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                if syllabes[-2][-1] + syllabes[-1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('ui')
                else:
                    changements.append('o')
            elif syllabes[-2][-3] == 'Ǫ':
                changements.append('o')

        #Gestion de U
        if 'Ú' in syllabes[-2]:
            if syllabes[-2][-1] == 'Ú':
                changements.append('u')
            elif syllabes[-2][-2] == 'Ú':
                changements.append('u')
            elif syllabes[-2][-3] == 'Ú':
                changements.append('u')

        #Idem ici, la machine doit d'abord vérifier la longueur de la syllabe pour savoir si elle est uniquement composée d'une voyelle ou d'autre chose.
        if len(syllabes[-2]) == 1:
            pass
        elif syllabes[-2] in listes_lettres['désinences_subjonctif']:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[-2][-2] + syllabes[-2][-1] in listes_lettres['consonantisme_implosif_complexe']:
                pass

            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme implosif
            elif syllabes[-2][-1] in listes_lettres['consonnes']:
                pass
                #Gestion de B
                if syllabes[-2][-1] == 'B':
                    pass
                #Gestion de C
                elif syllabes[-2][-1] == 'C':
                    pass
                #Gestion de D
                elif syllabes[-2][-1] == 'D':
                    pass
                #Gestion  de F
                elif syllabes[-2][-1] == 'F':
                    pass
                #Gestion  de G
                elif syllabes[-2][-1] == 'G':
                    pass
                #Gestion de J
                elif syllabes[-2][-1] == 'J':
                    pass
                #Gestion de K
                elif syllabes[-2][-1] == 'K':
                    pass
                #Gestion de P
                elif syllabes[-2][-1] == 'P':
                    pass
                #Gestion de Q
                elif syllabes[-2][-1] == 'Q':
                    pass
                #Gestion de S
                elif syllabes[-2][-1] == 'S':
                    pass
                #Gestion de T
                elif syllabes[-2][-1] == 'T':
                    pass
                #Gestion de V
                elif syllabes[-2][-1] == 'V':
                    pass
                #Gestion de X
                elif syllabes[-2][-1] == 'X':
                    pass

            elif syllabes[-2][-1] in listes_lettres['consonnes_liquides']:
                pass
                #Gestion  de L
                if syllabes[-2][-1] == 'L':
                    pass
                #Gestion de R
                elif syllabes[-2][-1] == 'R':
                    pass

            elif syllabes[-2][-1] in listes_lettres['consonnes_nasales']:
                pass
                #Gestion  de M
                if syllabes[-2][-1] == 'M':
                    pass
                #Gestion de N
                elif syllabes[-2][-1] == 'N':
                    pass

                #Gestion de H

                #Gestion de W
                #Gestion de Y

        return changements
