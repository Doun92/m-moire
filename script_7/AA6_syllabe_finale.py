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
'SB',
'DC', 'PC', 'SC', 'TC',
'RD',
'BJ', 'CJ', 'DJ', 'FJ', 'GJ', 'LJ', 'PJ', 'RJ', 'SJ', 'TJ', 'VJ',
'BL', 'CL', 'DL', 'FL', 'GL', 'HL', 'PL', 'SL', 'TL',
'SM',
'SN', 'TN',
'CP', 'NP', 'SP',
'BR', 'CR', 'DR', 'GR', 'HR', 'LR', 'MR', 'PR', 'SR', 'RR', 'TR', 'VR',
'PS',
'BT', 'CT', 'DT', 'NT', 'PT', 'VT',
'BW', 'CW', 'DW', 'GW', 'PW', 'QW', 'SW', 'TW', 'VW',
],

'consonantisme_implosif_complexe': ['NS', 'NT', 'RG'],

'suffixes' : ['ÁRIU', 'DON', 'JAN'],

'prefixes': ['AD'],

'désinences_verbales': ['DET', 'DON', 'MUS', 'TAN'],

'désinences_futur' : ['BO']

}

class SyllabeFinale:

    def __init__(self):
        return

    def syllabe_finale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #La dernière syllabe comporte une désinence verbale
        if syllabes[-1] in listes_lettres['désinences_verbales']:
            if syllabes[-1] == 'DON':
                changements.append('der')
            elif syllabes[-1] == 'MUS':
                if syllabes[-3] + syllabes[-2][0] == 'FAC':
                    changements.append('ons')
                else:
                    changements.append('mes')
            elif syllabes[-1] == 'TAN':
                changements.append('ter')
            else:
                changements.append('t')
        elif syllabes[-1] in listes_lettres['désinences_futur']:
            if syllabes[-1] == 'BO':
                changements.append('is')

        #Gestion du consonantisme explosif
        #En premier lieu, nous devons vérifier la longueur de de la syllabe, car si elle fait un caractère de longueur, ce dernier est automatiquement une voyelle
        if len(syllabes[-1]) == 1:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe']:
                #Premier groupe avec R en deuxième position
                #Les labiales combinées avec R évoluent toutes vers [vr] p.40.
                if syllabes[-1][0] + syllabes[-1][1] in ['BR', 'PR', 'VR']:
                    if syllabes[-1][0] + syllabes[-1][1] == 'VR':
                        if syllabes[-2][-1] == 'L':
                            changements.append('dr')
                        else:
                            changements.append('v' + syllabes[-1][1])
                    elif syllabes[-1][0] + syllabes[-1][1] == 'PR':
                        if syllabes[-2][-1] == 'S':
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                        else:
                            changements.append('v' + syllabes[-1][1])
                    else:
                        if syllabes[-2][-1] == 'M':
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                        else:
                            changements.append('v' + syllabes[-1][1])
                #Les dentales combinées avec R se simplifient p.40-41
                elif syllabes[-1][0] + syllabes[-1][1] in ['DR', 'TR']:
                    if syllabes[-2][-1] in listes_lettres['consonnes']:
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-2][-1] in ['N', 'R']:
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                    else:
                        changements.append(syllabes[-1][1])
                #Les palatales combinées avec R s'affaiblissent toutes en [ir] p.41
                elif syllabes[-1][0] + syllabes[-1][1] in ['CR', 'GR']:
                    if syllabes[-2][-1] in ['L', 'R', 'S']:
                        if syllabes[-1][2] == syllabes[-1][-1] == 'U':
                            changements.append('gr')
                        else:
                            changements.append('d' + syllabes[-1][1])
                    elif syllabes[-2][-1] == 'N':
                        if syllabes[-2][-2] == 'Ọ':
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                        elif syllabes[-2][-2] == 'Ẹ':
                            changements.append('t' + syllabes[-1][1])
                        else:
                            changements.append('d' + syllabes[-1][1])
                    elif syllabes[-2][-1] == 'Ẹ':
                        changements.append(syllabes[-1][1])
                    else:
                         changements.append('i' + syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] == 'RR':
                    changements.append(syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] == 'SR':
                    if syllabes[-2][-1] == 'S':
                        changements.append(syllabes[-1][0] + 't' + syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] == 'MR':
                    changements.append('b' + syllabes[-1][1])

                #Deuxième groupe avec L en deuxième position
                #Les labiales combinées avec L subissent des évolutions
                #qui peuvent aller du maintien à la spirantisation en passant par le redoublement p.41
                elif syllabes[-1][0] + syllabes[-1][1] in ['BL', 'FL', 'PL']:
                    if syllabes[-2][-1] == 'Ọ':                     #à revoir le groupe
                        if syllabes[-1][2] == 'U':                  # à revoir le groupe
                            changements.append('b' + syllabes[-1][1])
                        else:
                            changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-2][-1] == 'Ǫ':
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                    else:
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                #Les dentales combinées avec L connaissent différentes évolutions p.42
                elif syllabes[-1][0] + syllabes[-1][1] in ['DL', 'TL']:
                    if syllabes[-1][0] == 'T':
                        if syllabes[-2][-1] == 'R':
                            changements.append(syllabes[-1][0] + 'r')
                        elif syllabes[-2][-1] == 'Á':
                            changements.append('ll')
                        elif syllabes[-1][2] == syllabes[-1][-1] == 'U':
                            changements.append('il')
                        else:
                            changements.append('ill')
                    if syllabes[-1][0] == 'D':
                        if syllabes[-2][-1] == 'Ǫ':
                            if syllabes[-1][-1] == 'U':
                                changements.append(syllabes[-1][1] + syllabes[-1][1])
                            else:
                                changements.append(syllabes[-1][1])
                        else:
                            changements.append(syllabes[-1][1])
                #Les palatales combinées avec L aboutissent toutes à un l mouillé p.42
                elif syllabes[-1][0] + syllabes[-1][1] in ['CL', 'GL']:
                    if syllabes[-2][-1] == 'C':
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-2][-1] in ['Ę', 'Ǫ']:
                        changements.append('il')
                    elif syllabes[-2][-1] in ['N', 'R']:
                        changements.append(syllabes[-1][0] + syllabes[-1][1])
                    elif syllabes[-2][-1] == 'S':
                        changements.append(syllabes[-1][1])
                    else:
                        changements.append('ill')
                elif syllabes[-1][0] + syllabes[-1][1] == 'SL':
                    changements.append(syllabes[-1][0] + syllabes[-1][1])

                elif syllabes[-1][0] + syllabes[-1][1] == 'LR':
                    changements.append('dr')

                #Troisième groupe avec un wau (W) en deuxième position
                #Les labiales combinée au wau aboutissent à un amuïssement
                #en arrondissant la voyelle tonique qui suit ou qui précède p.43
                elif syllabes[-1][0] + syllabes[-1][1] in ['BW', 'PW', 'VW']:
                    changements.append('')
                #Les dentales combinées au wau constituent des séquences complexes
                #la geminée s'amuit p.43
                elif syllabes[-1][0] + syllabes[-1][1] in ['DW', 'TW', 'SW']:
                    if syllabes[-1][0] + syllabes[-1][1] == 'SW':
                        if syllabes[-2][-1] == 'N':
                            changements.append('')
                        else:
                            changements.append('u')
                    else:
                        changements.append('u')
                #Les vélaires avec un wau sont réparties en deux catégories p.44
                elif syllabes[-1][0] + syllabes[-1][1] in ['CW', 'GW', 'QW']:
                    if syllabes[-2][-1] == 'N':
                        if syllabes[-1][2] == syllabes[-1][-1] == 'A':
                            changements.append('qu')
                        else:
                            changements.append('gu')
                    elif syllabes[-2][-1] == 'S':
                        changements.append('qu')
                    elif syllabes[-1][2] == 'T':
                        changements.append('')
                    else:
                        changements.append('u')
                #Quatrième groupe avec un yod (J) en deuxième position
                #Les labiales combinées au yod subissent une évolution différente
                #La sourde  se redouble et voit la semi-voyelle se durcir
                #Les sonores tiennent compte de l'entourage vocalique p.44
                elif syllabes[-1][0] + syllabes[-1][1] in ['BJ', 'PJ', 'VJ']:
                    if syllabes[-1][0] + syllabes[-1][1] == 'PJ':
                        changements.append('ch')
                    else:
                        #En milieu paltal
                        if syllabes[-2][-1] in listes_lettres['voyelles_palatales']:
                            changements.append('g')
                        #En milieu vélaire
                        elif syllabes[-2][-1] in listes_lettres['voyelles_vélaires']:
                            changements.append('i')
                #Les dentales combinées à un yod connaissent trois évolutions différentes p.45
                elif syllabes[-1][0] + syllabes[-1][1] in ['TJ', 'DJ', 'SJ']:
                    #L'occlusive sourde s'assibile et se sonorise
                    if syllabes[-1][0] + syllabes[-1][1] == 'TJ':
                        changements.append('is')
                    #L'occlusive sonore s'assimile au yod  puis se simplifie
                    elif syllabes[-1][0] + syllabes[-1][1] == 'DJ':
                        changements.append('i')
                    #La sifflante se palatalise et se sonorise
                    elif syllabes[-1][0] + syllabes[-1][1] == 'SJ':
                        changements.append('is')
                #Les palatales combinées au yod se redoublent
                elif syllabes[-1][0] + syllabes[-1][1] in ['CJ', 'GJ']:
                    if syllabes[-1][0] + syllabes[-1][1] == 'CJ':
                        changements.append('c')
                    #La palatale sourde s'assibile encore
                    elif syllabes[-1][0] + syllabes[-1][1] == 'GJ':
                        changements.append('i')

                elif syllabes[-1][0] + syllabes[-1][1] == 'NT':
                    changements.append(syllabes[-1][0] + syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] in ['CT', 'DT', 'PT', 'VT']:
                    changements.append(syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] == 'BT':
                    if syllabes[-2][-1] == 'R':
                        changements.append('d')

                elif syllabes[-1][0] + syllabes[-1][1] == 'SB':
                    changements.append(syllabes[-1][0] + syllabes[-1][1])

                elif syllabes[-1][0] + syllabes[-1][1] == 'SC':
                    if syllabes[-1][2] in ['Á', 'A']:
                        changements.append('sch')
                    else:
                        changements.append(syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] == 'TC':
                    if syllabes[-1][2] in ['Á', 'A']:
                        changements.append('ch')
                    elif syllabes[-2][-1] == 'R':
                        changements.append('ch')
                    else:
                        changements.append(syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] == 'PC':
                    changements.append(syllabes[-1][1])
                elif syllabes[-1][0] + syllabes[-1][1] == 'DC':
                    changements.append('z')

                elif syllabes[-1][0] + syllabes[-1][1] == 'RD':
                    if syllabes[-1][2] in listes_lettres['voyelles_atones_sans_A']:
                        if syllabes[-1][2] == syllabes[-1][-1]:
                            changements.append('t')

                elif syllabes[-1][0] + syllabes[-1][1] == 'TN':
                    if syllabes[-2][-2] == 'Ę':
                        changements.append('gn')
                elif syllabes[-1][0] + syllabes[-1][1] == 'SN':
                    changements.append(syllabes[-1][0] + syllabes[-1][1])

                elif syllabes[-1][0] + syllabes[-1][1] == 'SM':
                    changements.append(syllabes[-1][0] + syllabes[-1][1])

                elif syllabes[-1][0] + syllabes[-1][1] == 'CP':
                    changements.append('qu')
                elif syllabes[-1][0] + syllabes[-1][1] == 'NP':
                    changements.append('nvr')

                elif syllabes[-1][0] + syllabes[-1][1] == 'PS':
                    changements.append(syllabes[-1][1])



            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme explosif
            elif syllabes[-1][0] in listes_lettres['consonnes']:
                #Gestion de B
                #L'occlusive labiale sonore se spirantise puis suit une évolution selon son entourage
                if syllabes[-1][0] == 'B':
                    if syllabes[-1] in listes_lettres['désinences_futur']:
                        changements.append('')
                    else:
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            #En milieu palatal
                            if syllabes[-2][-1] in listes_lettres['voyelles_palatales']:
                                if syllabes[-1][1] in listes_lettres['voyelles_palatales']:
                                    if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                        if syllabes[-1][1] + syllabes[-1][2] == 'ET':
                                            changements.append('')
                                        else:
                                            changements.append('f')
                                    else:
                                        changements.append('v')
                                else:
                                    if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                        changements.append('f')
                                    else:
                                        changements.append('')
                            #En milieu vélaire
                            elif syllabes[-2][-1] in listes_lettres['voyelles_vélaires']:
                                if syllabes[-1][1] in listes_lettres['voyelles_vélaires']:
                                    if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                        changements.append('f')
                                    else:
                                        changements.append('')
                                else:
                                    if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                        changements.append('f')
                                    else:
                                        if syllabes[-2][-1] == 'Ú':
                                            changements.append('')
                                        else:
                                            changements.append('v')
                        elif syllabes[-2][-1] == 'R':
                            if syllabes[-1][1] == syllabes[-1][-1] in ['E', 'U']:
                                if syllabes[-2][-2] == 'Ǫ':
                                    changements.append('b')
                                else:
                                    changements.append('p')
                        else:
                            changements.append(syllabes[-1][0])

                #Gestion de C
                elif syllabes[-1][0] == 'C':
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-1][1] in ['E', "Ẹ", "Ę", 'I', 'Í']:
                            if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                if len(syllabes[-1]) > 2:
                                    #Vérification si c'est un verbe
                                    if syllabes[-1][1] + syllabes[-1][2] in ['EM', 'ET', 'IT']:
                                        changements.append('s')
                                    else:
                                        changements.append('z')
                                else:
                                    if syllabes[-2][-1] == 'Ọ':
                                        changements.append('iz')
                                    elif syllabes[-2] in ['LI', 'MI']:
                                        changements.append('c')
                                    else:
                                        changements.append('z')
                            else:
                                changements.append('s')
                        elif syllabes[-1][1] in ['A', 'Á']:
                            if syllabes[-2][-1] in ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í']:
                                if syllabes[-2][-1] in ['I', 'Í',]:
                                    changements.append('')
                                else:
                                    changements.append('i')
                            elif syllabes[-2][-1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                                changements.append('')
                        elif syllabes[-1][1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                            if len(syllabes[-2]) > 1:
                                if syllabes[-2][1] == 'I' and syllabes[-1][1] == syllabes[-1][-1] == 'U':
                                    if syllabes[-2][-2] == 'N':
                                        changements.append('')
                                    else:
                                        changements.append(syllabes[-1][0])
                                else:
                                    changements.append('')
                            else:
                                changements.append('')
                    else:
                        if syllabes[-1][1] in ['A', 'Á']:
                            if syllabes[-2][-1] == 'L':
                                changements.append(syllabes[-1][0])
                            else:
                                changements.append('ch')
                        elif syllabes[-1][1] == 'E':
                            if syllabes[-2][-1] in ['L', 'R']:
                                if syllabes[1][-1] == 'T':
                                    changements.append('')
                                else:
                                    changements.append('z')
                            elif syllabes[-2][-1] in listes_lettres['consonnes_nasales']:
                                changements.append(syllabes[-1][0])
                        elif syllabes[-2][-1] == 'D':
                            if syllabes[-1][1] == syllabes[-1][-1] == 'Ī':
                                changements.append('tz')
                            else:
                                changements.append('g')
                        else:
                            changements.append('c')

                #Gestion de D
                elif syllabes[-1][0] == 'D':
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-1][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones']:
                            changements.append('')
                        elif syllabes[-1][1] == 'T':
                            changements.append('')
                        elif syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                            if syllabes[-1][-1] == 'T':
                                changements.append('')
                    elif syllabes[-2][-2] in listes_lettres['voyelles_toniques'] and syllabes[-2][-1] in listes_lettres['consonnes_nasales']:
                        if syllabes[-1][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones_sans_A']:
                            if syllabes[-2][-2] in ['Á', 'Ọ']:
                                changements.append('t')
                            else:
                                changements.append('')
                        elif syllabes[-1][1] == syllabes[-1][-1] == 'A':
                            changements.append(syllabes[-1][0])
                    elif syllabes[-2][-1] in ['R', 'T']:
                        if syllabes[-1][1] == syllabes[-1][-1] in ['A', 'E', 'U']:
                            if syllabes[-2][-2] == 'Ǫ':
                                changements.append('g')
                            else:
                                changements.append('t')
                        else:
                            changements.append('t')
                    else:
                        changements.append(syllabes[-1][0])

                #Gestion  de F
                elif syllabes[-1][0] == 'F':
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-1][1] in listes_lettres['voyelles_palatales']:
                            changements.append('v')
                        elif syllabes[-1][1] in listes_lettres['voyelles_vélaires']:
                            changements.append('')
                    else:
                        changements.append(syllabes[-1][0])

                #Gestion  de G
                elif syllabes[-1][0] == 'G':
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-1][1] in ['E', "Ẹ", "Ę", 'I', 'Í']:
                            if len(syllabes[-1]) > 2:
                                if syllabes[-1][2] in ['S', 'T']:
                                    if syllabes[-2][-1] == 'Ę':
                                        changements.append('')
                                    else:
                                        changements.append('i')
                                else:
                                    changements.append('')
                            else:
                                changements.append('')
                        elif syllabes[-1][1] in ['A', 'Á']:
                            if syllabes[-2][-1] in ['A', 'Á', 'E', "Ẹ", "Ę", 'I', 'Í']:
                                if syllabes[-2][-1] in ['Ẹ', 'I', 'Í']:
                                    changements.append('')
                                elif syllabes[-2][-2] == 'R':
                                    changements.append('g')
                                else:
                                    changements.append('i')
                            elif syllabes[-2][-1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                                if syllabes[-2][-1] in ['O', "Ǫ", "Ọ"]:
                                    changements.append('v')
                                else:
                                    changements.append('')
                        elif syllabes[-1][1] in ['O', "Ǫ", "Ọ", 'U', "Ú",]:
                            changements.append('')
                    else:
                        if syllabes[-1][-1] == 'U':
                            changements.append('c')
                        elif syllabes[-2][-1] == 'N':
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])

                #Gestion de J
                elif syllabes[-1][0] == 'J':
                    changements.append('j')

                #Gestion de K
                elif syllabes[-1][0] == 'K':
                    pass

                #Gestion de P
                elif syllabes[-1][0] == 'P':
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        #En milieu palatal
                        if syllabes[-2][-1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-1][1] in listes_lettres['voyelles_palatales']:
                                if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                elif syllabes[-2][-1] == 'A':
                                    changements.append(syllabes[-1][0])
                                else:
                                    changements.append('v')
                            else:
                                if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                    if syllabes[-2] == 'Á':
                                        changements.append('')
                                    elif syllabes[-2][-1] == 'Ę':
                                        changements.append('')
                                    else:
                                        changements.append('f')
                                else:
                                    changements.append('')
                        #En milieu vélaire
                        elif syllabes[-2][-1] in listes_lettres['voyelles_vélaires']:
                            if syllabes[-1][1] in listes_lettres['voyelles_vélaires']:
                                if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                    if syllabes[-2][-1] == 'Ǫ':
                                        changements.append('')
                                    else:
                                        changements.append('f')
                                else:
                                    changements.append('')
                            else:
                                if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                    changements.append('f')
                                else:
                                    changements.append('v')
                        else:
                            changements.append(syllabes[-1][0])
                    elif syllabes[-2][-1] in ['R']:
                        if syllabes[-1][1] == 'U':
                            changements.append('')
                    else:
                        changements.append(syllabes[-1][0])

                #Gestion de Q
                elif syllabes[-1][0] == 'Q':
                    pass

                #Gestion de S
                elif syllabes[-1][0] == 'S':
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-2][-1] == syllabes[-1][1]:
                            changements.append('')
                        else:
                            changements.append('s')
                    else:
                        if syllabes[-2][-1] in ['L', 'P']:
                            if syllabes[-2][-1] and syllabes[-1][-1] in ['Á', 'A']:
                                changements.append(syllabes[-1][0] + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        else:
                            changements.append(syllabes[-1][0])

                #Gestion de T
                elif syllabes[-1][0] == 'T':
                    if syllabes[-1] in listes_lettres['désinences_verbales']:
                        changements.append('')
                    else:
                        if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                            if syllabes[-2][-1] in listes_lettres['voyelles_toniques']:
                                if len(syllabes[-2]) > 1:
                                    if syllabes[-2][1] == 'I':
                                        changements.append('ci')
                                    elif syllabes[-2][-1] == 'Ę':
                                        changements.append(syllabes[-1][0])
                                    else:
                                        changements.append('')
                                else:
                                    if syllabes[-2][-1] == 'Ę':
                                        changements.append(syllabes[-1][0])
                                    else:
                                        changements.append('')
                            elif syllabes[-1][1] == syllabes[-1][-1] in listes_lettres['voyelles_atones']:
                                changements.append('')
                            elif syllabes[-1][1] == 'T':
                                changements.append('')
                            else:
                                changements.append(syllabes[-1][0])
                        else:
                            if syllabes[-2][-1] in listes_lettres['consonnes_nasales']:
                                if syllabes[-1][1] == 'I':
                                    changements.append('ci')
                                else:
                                    changements.append(syllabes[-1][0])
                            elif syllabes[-2][-1] == 'C':
                                changements.append('d')
                            else:
                                changements.append(syllabes[-1][0])

                #Gestion de V
                elif syllabes[-1][0] == 'V':
                    if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                        if syllabes[-1][1] in listes_lettres['voyelles_palatales']:
                            if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                                if syllabes[-1][1] in ['E', 'I']:
                                    if syllabes[-2][-1] in ['Á', 'Ę', 'Ǫ']:
                                        changements.append('f')
                                    else:
                                        changements.append('')
                                else:
                                    changements.append('f')
                            elif syllabes[-1][1] in ['S', 'T']:
                                changements.append('f')
                            else:
                                changements.append('v')
                        elif syllabes[-1][1] in listes_lettres['voyelles_vélaires']:
                            if syllabes[-1][1] == syllabes[-1][-1] == 'U':
                                if syllabes[-2][-1] == 'Í':
                                    if syllabes[-2][-2] == 'T':
                                        changements.append('f')
                                    else:
                                        changements.append('')
                                else:
                                    changements.append('f')
                            else:
                                changements.append('')
                    elif syllabes[-2][-1] == 'L':
                        if syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('f')
                        else:
                            changements.append('')
                    else:
                        changements.append('')

                #Gestion de X
                elif syllabes[-1][0] == 'X':
                    if syllabes[-2][-1] == 'Ǫ':
                        if syllabes[-1][1] == syllabes[-1][-1] == 'A':
                            changements.append('ss')
                        else:
                            changements.append('s')
                    else:
                        changements.append('s')

            elif syllabes[-1][0] in listes_lettres['consonnes_liquides']:
                #Gestion  de L
                if syllabes[-1][0] == 'L':
                    #Épenthèses avec une syllabe antérieure à une lettre
                    if len(syllabes[-2]) == 1:
                        #Épenthèse d'un b après M
                        if syllabes[-2][-1] == 'M':
                            changements.append('b'+syllabes[-1][0])
                        #Épenthèse d'un d après N
                        elif syllabes[-2][-1] == 'N':
                            changements.append('d'+syllabes[-1][0])
                        #Épenthèse d'un d après L
                        elif syllabes[-2][-1] == 'L':
                            changements.append('d'+syllabes[-1][0])
                        #Épenthèse d'un d après S sonore
                        elif syllabes[-2][-1] == 'S':
                            changements.append('d'+syllabes[-1][0])
                        else:
                            changements.append(syllabes[-1][0])
                    #Tous les autres cas
                    else:
                        #Épenthèse d'un b après M
                        if syllabes[-2][-1] == 'M':
                            changements.append('b'+syllabes[-1][0])
                        elif syllabes[-2][-2] == "M":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('b' + syllabes[-1][0])
                            elif syllabes[-2][-1] == 'Ę':
                                changements.append('u')
                            else:
                                changements.append(syllabes[-1][0])
                        #Épenthèse d'un d après N
                        elif syllabes[-2][-1] == 'N':
                            if syllabes[-2][-2] == 'Í':
                                changements.append('g' + syllabes[-1][0])
                            else:
                                changements.append('d' + syllabes[-1][0])
                        elif syllabes[-2][-2] == "N":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('d' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        #Épenthèse d'un d après S sonore
                        elif syllabes[-2][-1] == 'S':
                            #Épenthèse d'un t après S sourde
                            if syllabes[-2][-2] == 'S':
                                changements.append('t')
                            elif syllabes[-2][-2] == 'Í':
                                changements.append(syllabes[-1][0])
                            else:
                                changements.append('d'+syllabes[-1][0])
                        elif syllabes[-2][-1] == 'Ę':
                            changements.append(syllabes[-1][0])
                        elif syllabes[-2][-2] == "S":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('d' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        #Épenthèse d'un t après S sourde
                        elif syllabes[-2][-2] == "X":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('t' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        elif syllabes[-2][-1] == 'L':
                            changements.append(syllabes[-1][0])
                        elif syllabes[-1][1] == syllabes[-1][-1] == 'U':
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])

                #Gestion de R
                elif syllabes[-1][0] == 'R':
                    #Gestion de la syllabe précédente ne comportant qu'une syllabe
                    if len(syllabes[-2]) > 1:
                        #Épenthèse d'un b après M
                        if syllabes[-2][-1] == 'M':
                            changements.append('b'+syllabes[-1][0])
                        elif syllabes[-2][-2] == "M":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('b' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        #Épenthèse d'un d après N
                        elif syllabes[-2][-1] == 'N':
                            changements.append('d'+syllabes[-1][0])
                        elif syllabes[-2][-2] == "N":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('d' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        #Épenthèse d'un d après L
                        elif syllabes[-2][-1] == 'L':
                            changements.append('d'+syllabes[-1][0])
                        elif syllabes[-2][-2] == "L":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('d' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        #Épenthèse d'un d après S sonore
                        elif syllabes[-2][-1] == 'S':
                            #Épenthèse d'un t après S sourde
                            if syllabes[-2][-2] == 'S':
                                changements.append('t')
                            else:
                                changements.append('d'+syllabes[-1][0])
                        elif syllabes[-2][-2] == "S":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('d' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        elif syllabes[-2][-1] == 'X':
                            changements.append('t' + syllabes[-1][0])
                        #Épenthèse d'un t après S sourde
                        elif syllabes[-2][-2] == "X":
                            if syllabes[-2][-1] in listes_lettres['voyelles_atones_sans_A'] and syllabes[-2] != syllabes[0]:
                                changements.append('t' + syllabes[-1][0])
                            else:
                                changements.append(syllabes[-1][0])
                        #assimilation au R précédent
                        elif syllabes[-2][-1] == 'R':
                            if syllabes[-1][-1] == 'A':
                                changements.append(syllabes[-1][0])
                            else:
                                changements.append('')
                        else:
                            changements.append(syllabes[-1][0])
                    else:
                        #assimilation au R précédent
                        if syllabes[-2][-1] == 'R':
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])

            elif syllabes[-1][0] in listes_lettres['consonnes_nasales']:
                #Gestion  de M
                if syllabes[-1][0] == 'M':
                    if syllabes[-1] in listes_lettres['désinences_verbales']:
                        changements.append('')
                    else:
                        #Fermeture de la nasale
                        if syllabes[-1][-2] + syllabes[-1][-1] == 'ES':
                            changements.append('n')
                        elif syllabes[-2][-1] == 'M':
                            changements.append('')
                        else:
                            changements.append(syllabes[-1][0])

                #Gestion de N
                elif syllabes[-1][0] == 'N':
                    if len(syllabes[-1]) == 2:
                        if syllabes[-2][-1] == 'M':
                            changements.append('')
                        #mouillure du N
                        elif syllabes[-2][-1] == 'G':
                            if syllabes[-1][1] == 'A':
                                changements.append('gn')
                            else:
                                changements.append('ng')
                        elif syllabes[-2][-1] in ['Á', 'Ọ', 'O', 'Í', 'J', 'S']:
                            changements.append('n')
                        elif syllabes[-1][-1] == 'E':
                            if syllabes[-2][-1] in ['Á', 'Ę']:
                                changements.append(syllabes[1][0])
                            elif syllabes[-2][-2] == 'Ọ':
                                changements.append('n')
                            else:
                                changements.append('m')
                        elif syllabes[-1][-1] == 'U':
                            if syllabes[-2][-2] + syllabes[-2][-1] == 'ỌR':
                                changements.append(syllabes[-1][0])
                            else:
                                changements.append('')
                        else:
                            changements.append(syllabes[-1][0])
                    else:
                        changements.append(syllabes[-1][0])

                #Gestion du H germain
            elif syllabes[-1][0] == 'H':
                pass

                #Gestion de W
            if syllabes[-1][0] == 'W':
                if syllabes[-2][-1] in listes_lettres['toutes_les_voyelles']:
                    if syllabes[-1][1] in listes_lettres['voyelles_palatales']:
                        if syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('f')
                        elif syllabes[-1][1] in ['S', 'T']:
                            changements.append('f')
                        else:
                            changements.append('v')
                    elif syllabes[-1][1] in listes_lettres['voyelles_vélaires']:
                        changements.append('')
                elif syllabes[-2][-1] == 'Q':
                    if syllabes[-1][1] == syllabes[-1][-1] == 'A':
                        changements.append('v')
                    else:
                        changements.append('u')
                elif syllabes[-1][1] == syllabes[-1][-1] == 'Ī':
                    changements.append('')
                elif syllabes[-1][1] == 'I':
                    changements.append('')
                else:
                    changements.append('v')

                #Gestion de Y
            if syllabes[-1][0] == 'Y':
                pass

        #Gestion des différents vocalismes
        #Vocalisme contretonique
        #Gestion de A
        if 'A' in syllabes[-1]:
            if syllabes[-1][-1] == 'A':
                changements.append('e')
            elif syllabes[-1][-2] == 'A':
                if syllabes[-1] == 'TAN':
                    changements.append('')
                else:
                    #Vérification s'il s'agit d'un mot provenant du germain
                    if syllabes[-2][-1] == 'J':
                        if syllabes[-1][-1] == 'N':
                            changements.append('ir')
                        else:
                            pass
                    else:
                        changements.append('e')
            elif syllabes[-1][-3] == 'A':
                if syllabes[-1][-2] + syllabes[-1][-1] == 'NS':
                    changements.append('a')
                else:
                    changements.append('e')

        #Gestion de E
        if 'E' in syllabes[-1]:
            if syllabes[-1][-1] == 'E':
                if len(syllabes[-1]) > 1:
                    if syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe']:
                        changements.append(syllabes[-1][-1])
                    elif syllabes[-2][-1] + syllabes[-1][0] in ['MC', 'MT', 'NR', 'SR', 'VR', 'SN', 'WN']:
                        changements.append(syllabes[-1][-1])
                    elif syllabes[-2] in ['CJ', 'DI', 'GJ', 'LI', 'MI']:
                        changements.append(syllabes[-1][-1])
                    elif syllabes[-1][-2] == syllabes[-1][0] == 'R':
                        if syllabes[-2][-1] == 'L':
                            changements.append('e')
                        elif syllabes[-2][-1] == 'Í':
                            changements.append('')
                        elif syllabes[-2][-1] == 'E':
                            changements.append('e')
                    elif syllabes[-1][-2] == syllabes[-1][0] == 'G':
                        if syllabes[-2][-1] == 'N':
                            if syllabes[-2][-2] == 'Ǫ':
                                changements.append('')
                            else:
                                changements.append('e')
                        else:
                            pass
                    elif syllabes[-1][0] + syllabes[-1][1] in ['CP']:
                        changements.append(syllabes[-1][-1])
                    else:
                        changements.append('')
                else:
                    changements.append('')
            elif syllabes[-1][-2] == 'E':
                changements.append('')
            elif syllabes[-1][-3] == 'E':
                if syllabes[-1][0] + syllabes[-1][1] in listes_lettres['consonantisme_explosif_complexe']:
                    changements.append(syllabes[-1][-3])
                else:
                    changements.append('')

        #Gestion de I:
        if 'I' in syllabes[-1]:
            if syllabes[-1][-1] == 'I':
                if len(syllabes[-1]) > 2:
                    if syllabes[-1][0] + syllabes[-1][1] == 'DC':
                        changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            elif syllabes[-1][-2] == 'I':
                if len(syllabes[-1]) == 4:
                    if (syllabes[-1][-4] + syllabes[-1][-3]) in listes_lettres['consonantisme_explosif_complexe']:
                        changements.append('e')
                    else:
                        changements.append('')
                else:
                    changements.append('')
            elif syllabes[-1][-3] == 'I':
                changements.append('')


        #Gestion de O:
        if 'O' in syllabes[-1]:
            if syllabes[-1][-1] == 'O':
                if len(syllabes[-1]) == 1:
                    if syllabes[-2] == 'Ę':
                        changements.append('')
                    elif syllabes[-2] in ['CJ', 'RÍ']:
                        changements.append('')
                    elif syllabes[-2][-1] == 'J':
                        changements.append('e')
                    else:
                        changements.append('on')
                else:
                    if len(syllabes[-1]) > 2:
                        if syllabes[-1][-3] + syllabes[-1][-2] == 'TR':
                            changements.append('e')
                        else:
                            changements.append('')
                    else:
                        changements.append('')
            elif syllabes[-1][-2] == 'O':
                if len(syllabes[-1]) > 2:
                    if syllabes[-1][-3] == 'Y':
                        if syllabes[-2][-1] == 'Á':
                            changements.append('')
                        else:
                            changements.append('o')
                    elif syllabes[-1][-1] == 'R':
                        if syllabes[-1][-3] == 'S':
                            changements.append('')
                        else:
                            changements.append('e')
                    #En présence d'un pluriel
                    elif syllabes[-1][-3] == 'S':
                        if syllabes[-2][-1] == syllabes[-1][-2]:
                            changements.append('')
                        else:
                            changements.append('e')
                    #Pour les verbes venant du germain
                    # elif syllabes[-1][-1] == 'N':
                        # changements.append('e')
                    # else:
                        # changements.append('')
                else:
                    #Vérification si c'est un pluriel
                    if syllabes[-1][-1] == 'S':
                        if syllabes[-2][-1] == 'Ę':
                            changements.append('u')
                        else:
                            changements.append('')
                    else:
                        changements.append('')
            elif syllabes[-1][-3] == 'O':
                changements.append('')

        #Gestion de U:
        if 'U' in syllabes[-1]:
            if syllabes[-1][-1] == 'U':
                if len(syllabes[-1]) == 1:
                    if syllabes[-2][-1] == 'Ę':
                        changements.append(syllabes[-1][-1])
                    elif syllabes[-2] in ['LE', 'BJ', 'NJ', 'MJ', 'PJ', 'RJ']:
                        changements.append('e')
                    elif syllabes[-2] in ['BRJ', 'PRJ']:
                        changements.append('e')
                    elif syllabes[-2] == 'DJ':
                        changements.append('')
                    else:
                        changements.append('')
                elif len(syllabes[-1]) == 2:
                    if syllabes[-2][-1] in ['B', 'C', 'D', 'G', 'J', 'P', 'R', 'S']:
                        if syllabes[-1][0] in ['C', 'D', 'M', 'N', 'T']:
                            changements.append('e')
                        elif syllabes[-2][-1] == 'P':
                            if syllabes[-2][-2] == 'Á':
                                changements.append('e')
                            else:
                                changements.append('')
                        elif syllabes[-2][-1] == ' L':
                            if syllabes[-1][0] == 'M':
                                changements.append('e')
                            else:
                                changements.append('')
                        else:
                            changements.append('')
                    elif syllabes[-2][-1] == 'L':
                        if len(syllabes[1]) > 2:
                            if syllabes[-2][0] + syllabes[-2][1] == 'PS':
                                changements.append('e')
                            else:
                                changements.append('')
                        else:
                            changements.append('')
                    elif syllabes[-2] in ['CJ', 'NI', 'XI', 'XJ']:
                        changements.append('e')
                    elif syllabes[-2][-1] == 'Ę':
                        changements.append('u')
                    else:
                        changements.append('')
                elif len(syllabes[-1]) == 3:
                    if syllabes[-1][0] + syllabes[-1][1] in ['CL', 'TL', 'NP', 'NT']:
                        if syllabes[-2][-1] in ['Ę', 'Ǫ']:
                            changements.append('')
                        else:
                            changements.append('e')
                    elif syllabes[-1][0] + syllabes[-1][1] == 'PS':
                        changements.append('')
                    elif syllabes[-2][-1] == 'N':
                        if syllabes[-2][-2] == 'Á':
                            changements.append('')
                        else:
                            changements.append('e')
                    else:
                        changements.append('e')
                else:
                    changements.append('e')
            elif syllabes[-1][-2] == 'U':
                changements.append('')
            elif syllabes[-1][-3] == 'U':
                if syllabes[-1][-2] + syllabes[-1][-1] in ['NP', 'NT']:
                    changements.append('e')
                else:
                    changements.append('')


        #Vocalisme tonique
        #Gestion de A tonique
        if 'Á' in syllabes[-1]:
            if syllabes[-1][-1] == 'Á':
                if len(syllabes[-1]) == 1:
                    if syllabes[-2] == 'TI':
                        changements.append('a')
                    else:
                        changements.append('e')
                else:
                    if syllabes[-1][-2] in ['C', 'G']:
                        changements.append('ie')
                    else:
                        changements.append('e')
            elif syllabes[-1][-2] == 'Á':
                if len(syllabes[-1]) > 2:
                    if syllabes[-1][-3] in ['C', 'G']:
                        changements.append('ie')
                    else:
                        changements.append('a')
                else:
                    changements.append('a')
            elif syllabes[-1][-3] == 'Á':
                if syllabes[-1][-4] in ['C', 'G']:
                    changements.append('ie')
                else:
                    changements.append('a')

        #Gestion du E fermé
        if 'Ẹ' in syllabes[-1]:
            if syllabes[-1][-1] == 'Ẹ':
                #Influence d'un I long final (Ī)
                if syllabes[-1][-1] == 'Ī':
                    changements.append('ie')
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[-1] in ['BJ', 'VJ', 'DJ', 'GI', 'GE']:
                    changements.append('i')
                else:
                    changements.append('ei')
            elif syllabes[-1][-2] == 'Ẹ':
                changements.append('e')
            elif syllabes[-1][-3] == 'Ẹ':
                changements.append('e')

        #Gestion du E ouvert
        if 'Ę' in syllabes[-1]:
            if syllabes[-1][-1] == 'Ę':
                #Influence d'un I long final (Ī)
                if syllabes[-1][-1] == 'Ī':
                    changements.append('ie')
                else:
                    changements.append('ie')
            elif syllabes[-1][-2] == 'Ę':
                changements.append('e')
            elif syllabes[-1][-3] == 'Ę':
                changements.append('e')

        #Gestion de I tonique
        if 'Í' in syllabes[-1]:
            if syllabes[-1][-1] == 'Í':
                changements.append('i')
            elif syllabes[-1][-2] == 'Í':
                #Influence d'une nasale
                if syllabes[-1][-1] in listes_lettres['consonnes_nasales']:
                    changements.append('e')
                else:
                    changements.append('i')
            elif syllabes[-1][-3] == 'Í':
                changements.append('i')


        #Gestion de O fermé
        if 'Ọ' in syllabes[-1]:
            if syllabes[-1][-1] == 'Ọ':
                #Influence d'un I long final (Ī)
                if syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                else:
                    changements.append('ou')
            elif syllabes[-1][-2] == 'Ọ':
                if len(syllabes[-1]) == 3:
                    if syllabes[-1][-3] == 'V':
                        changements.append('ou')
                    else:
                        changements.append('o')
                elif syllabes[-2][-1] == 'U':
                    changements.append('ou')
                else:
                    changements.append('o')
            elif syllabes[-1][-3] == 'Ọ':
                changements.append('o')

        #Gestion de O ouvert
        if 'Ǫ' in syllabes[-1]:
            if syllabes[-1][-1] == 'Ǫ':
                #Influence d'un I long final (Ī)
                if syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                else:
                    changements.append('ue')
            elif syllabes[-1][-2] == 'Ǫ':
                changements.append('o')
            elif syllabes[-1][-3] == 'Ǫ':
                changements.append('o')

        #Gestion de U
        if 'Ú' in syllabes[-1]:
            if syllabes[-1][-1] == 'Ú':
                changements.append('u')
            elif syllabes[-1][-2] == 'Ú':
                changements.append('u')
            elif syllabes[-1][-3] == 'Ú':
                changements.append('u')

        if 'Ī' in syllabes[-1]:
            if len(syllabes[-1]) == 2:
                if syllabes[-1][-2] == syllabes[-1][0] == 'C':
                    changements.append('e')

        #Idem ici, la machine doit d'abord vérifier la longueur de la syllabe pour savoir si elle est uniquement composée d'une voyelle ou d'autre chose.
        if len(syllabes[-1]) == 1:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[-1][-2] + syllabes[-1][-1] in listes_lettres['consonantisme_implosif_complexe']:
                if syllabes[-1][-2] + syllabes[-1][-1] == 'NS':
                    if syllabes[-1][-3] == 'A':
                        changements.append('nz')
                    else:
                        changements.append(syllabes[-1][-2] + syllabes[-1][-1])
                elif syllabes[-1][-2] + syllabes[-1][-1] == 'RG':
                    changements.append('rc')
                else:
                    changements.append(syllabes[-1][-2] + syllabes[-1][-1])

            elif syllabes[-1] in listes_lettres['désinences_verbales']:
                changements.append('')

            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme implosif
            elif syllabes[-1][-1] in listes_lettres['consonnes']:
                pass
                #Gestion de B
                if syllabes[-1][-1] == 'B':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de C
                elif syllabes[-1][-1] == 'C':
                    #spirantisation
                    changements.append('')
                #Gestion de D
                elif syllabes[-1][-1] == 'D':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion  de F
                elif syllabes[-1][-1] == 'F':
                    changements.append('')
                #Gestion  de G
                elif syllabes[-1][-1] == 'G':
                    #Après I et E
                    if syllabes[-1][-2] in ["Ẹ", "Ę", 'E', 'I', 'Í']:
                        changements.append('i')
                    else:
                        changements.append('u')
                #Gestion de J
                elif syllabes[-1][-1] == 'J':
                    pass
                #Gestion de K
                elif syllabes[-1][-1] == 'K':
                    pass
                #Gestion de P
                elif syllabes[-1][-1] == 'P':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de Q
                elif syllabes[-1][-1] == 'Q':
                    pass
                #Gestion de S
                elif syllabes[-1][-1] == 'S':
                    if syllabes[-1][0] + syllabes[-1][1] in ['DE', 'TU']:
                        changements.append('z')
                    elif syllabes[1][0] + syllabes[1][1] in ['CI', 'DU', 'NI']:
                        changements.append('')
                    elif syllabes[1][0] == 'S':
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][-1])
                #Gestion de T
                elif syllabes[-1][-1] == 'T':
                    if syllabes[-1][-2] == 'A':
                        changements.append('')
                    elif syllabes[-1] == 'DET':
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][-1])
                #Gestion de V
                elif syllabes[-1][-1] == 'V':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de X
                elif syllabes[-1][-1] == 'X':
                    changements.append('s')

            elif syllabes[-1][-1] in listes_lettres['consonnes_liquides']:
                pass
                #Gestion  de L
                if syllabes[-1][-1] == 'L':
                    #Vocalisation en W
                    changements.append('u')

                #Gestion de R
                elif syllabes[-1][-1] == 'R':
                    if len(syllabes[-1]) == 3:
                        if len(syllabes[-2]) >= 4:
                            if syllabes[-2][0] + syllabes[-2][1] == 'TC':
                                if syllabes[-2][-1] == 'S':
                                    changements.append('tre')
                                else:
                                    pass
                            else:
                                pass
                        elif syllabes[-1][0] + syllabes[-1][1] in ['TE', 'YO']:
                            changements.append(syllabes[-1][-1] + 'e')
                        #Épenthèse d'un D après L et d'un E de soutien
                        elif syllabes[-1][0] == 'L' and syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-1][-1] + 'e')
                        #Épenthèse d'un D après N et d'un E de soutien
                        elif syllabes[-1][0] == 'N' and syllabes[-1][1] in listes_lettres['voyelles_atones_sans_A']:
                            changements.append('d' + syllabes[-1][-1] + 'e')
                        else:
                            changements.append(syllabes[-1][-1])
                    else:
                        if syllabes[-1] == 'MR':
                            changements.append('e')
                        elif syllabes[-1] == 'OR':
                            changements.append('re')
                        else:
                            changements.append(syllabes[-1][-1])

            elif syllabes[-1][-1] in listes_lettres['consonnes_nasales']:
                pass
                #Gestion  de M
                if syllabes[-1][-1] == 'M':
                    if syllabes[-1][-2] in ['O', 'U']:
                        if syllabes[-2][-1] in ['Ę', 'Ǫ']:
                            changements.append('n')
                        else:
                            changements.append('')
                    else:
                        changements.append('')

                #Gestion de N
                elif syllabes[-1][-1] == 'N':
                    if syllabes[-2][-1] + syllabes[-1][0] == 'JA':
                        changements.append('')
                    elif syllabes[-1][-3] + syllabes[-1][-2] == 'DO':
                        changements.append('')
                    elif syllabes[-1][0] == 'M':
                        changements.append('')
                    else:
                        changements.append(syllabes[-1][-1])

                #Gestion de H

                #Gestion de W
                #Gestion de Y

        return changements
