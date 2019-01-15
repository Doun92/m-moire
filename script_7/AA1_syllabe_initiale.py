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

'consonantisme_explosif_complexe' : ['BI', 'BL', 'BR', 'BU', 'CH', 'CL', 'CR',
 'DE', 'DI', 'DR', 'DY', 'FL', 'FR', 'GL', 'GR', 'KW',
 'PC', 'PL', 'PR', 'PS', 'PT',
 'SC', 'SCR', 'SL', 'SN', 'SM', 'SP', 'ST', 'STR', 'TR'],

'consonantisme_implosif_complexe': ['LL', 'NC', 'NG', 'NK'],

'suffixes' : ['ÁRIU'],

'prefixes': ['DES'],

'désinences_présent': ['DET'],

'désinences_futur': ['BO']

}

class SyllabeInitiale:

    def __init__(self):
        return

    def syllabe_initiale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        #Gestion du consonantisme explosif
        #En premier lieu, nous devons vérifier la longueur de de la syllabe, car si elle fait un caractère de longueur, ce dernier est automatiquement une voyelle
        if len(syllabes[0]) == 1:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[0][0] + syllabes[0][1] in listes_lettres['consonantisme_explosif_complexe']:
                #Premier groupe avec R en deuxième position
                #Les labiales combinées avec R évoluent toutes vers [vr] p.40.
                if syllabes[0][0] + syllabes[0][1] in ['BR', 'PR', 'VR']:
                    changements.append('v' + syllabes[0][1])
                #Les dentales combinées avec R se simplifient p.40-41
                elif syllabes[0][0] + syllabes[0][1] in ['DR', 'TR']:
                    changements.append(syllabes[0][1])
                #Les palatales combinées avec R s'affaiblissent toutes en [ir] p.41
                elif syllabes[0][0] + syllabes[0][1] in ['CR', 'GR']:
                    changements.append('i' + syllabes[0][1])
                #Deuxième groupe avec L en deuxième position
                #Les labiales combinées avec L subissent des évolutions
                #qui peuvent aller du maintien à la spirantisation en passant par le redoublement p.41
                elif syllabes[0][0] + syllabes[0][1] in ['BL', 'FL', 'PL']:
                    changements.append(syllabes[0][0] + syllabes[0][1])
                #Les dentales combinées avec L connaissent différentes évolutions p.42
                elif syllabes[0][0] + syllabes[0][1] in ['DL', 'TL']:
                    if syllabes[0][0] == 'T':
                        changements.append('ill')
                    elif syllabes[0][0] == 'D':
                        changements.append(syllabes[0][1])
                #Les palatales combinées avec L aboutissent toutes à un l mouillé p.42
                elif syllabes[0][0] + syllabes[0][1] in ['CL', 'GL']:
                    changements.append('ill')
                #Troisième groupe avec un wau (W) en deuxième position
                #Les labiales combinée au wau aboutissent à un amuïssement
                #en arrondissant la voyelle tonique qui suit ou qui précède p.43
                elif syllabes[0][0] + syllabes[0][1] in ['BW', 'PW', 'VW']:
                    changements.append('')
                #Les dentales combinées au wau constituent des séquences complexes
                #la geminée s'amuit p.43
                elif syllabes[0][0] + syllabes[0][1] in ['DW', 'TW', 'SW']:
                    changements.append('u')
                #Les vélaires avec un wau sont réparties en deux catégories p.44
                elif syllabes[0][0] + syllabes[0][1] in ['CW', 'GW', 'QW']:
                    #la plus ancienne (QW) se prolonge généralement en [v]
                    if syllabes[0][0] + syllabes[0][1] == 'QW':
                        #En final et devant -s ou -t
                        if syllabes[0][1] == syllabes[-1][-1] or syllabes[0][2] in ['S', 'T'] or syllabes[-1][0] in ['S', 'T']:
                            changements.append('u')
                        else:
                            changements.append('v')
                    #Les deux autres subissent un affaiblissement
                    else:
                        if syllabes[0][2] == 'T' or syllabes[-1][0] == 'T':
                            changements.append('')
                        else:
                            changements.append('u')
                #Quatrième groupe avec un yod (J) en deuxième position
                #Les labiales combinées au yod subissent une évolution différente
                #La sourde  se redouble et voit la semi-voyelle se durcir
                #Les sonores tiennent compte de l'entourage vocalique p.44
                elif syllabes[0][0] + syllabes[0][1] in ['BJ', 'PJ', 'VJ']:
                    if syllabes[0][0] + syllabes[0][1] == 'PJ':
                        changements.append('ch')
                #Les dentales combinées à un yod connaissent trois évolutions différentes p.45
                elif syllabes[0][0] + syllabes[0][1] in ['TJ', 'DJ', 'SJ']:
                    #L'occlusive sourde s'assibile et se sonorise
                    if syllabes[0][0] + syllabes[0][1] == 'TJ':
                        changements.append('is')
                    #L'occlusive sonore s'assimile au yod  puis se simplifie
                    elif syllabes[0][0] + syllabes[0][1] == 'DJ':
                        changements.append('i')
                    #La sifflante se palatalise et se sonorise
                    elif syllabes[0][0] + syllabes[0][1] == 'SJ':
                        changements.append('is')
                #Les palatales combinées au yod se redoublent
                elif syllabes[0][0] + syllabes[0][1] in ['CJ', 'GJ']:
                    if syllabes[0][0] + syllabes[0][1] == 'CJ':
                        changements.append('c')
                    #La palatale sourde s'assibile encore
                    elif syllabes[0][0] + syllabes[0][1] == 'GJ':
                        changements.append('i')

            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme explosif
            elif syllabes[0][0] in listes_lettres['consonnes']:
                #Gestion de B
                #L'occlusive labiale sonore se spirantise puis suit une évolution selon son entourage
                if syllabes[0][0] == 'B':
                    changements.append(syllabes[0][0])

                #Gestion de C
                elif syllabes[0][0] == 'C':
                    if syllabes[0][1] in ['A', 'Á']:
                        changements.append('ch')
                    else:
                        changements.append('c')

                #Gestion de D
                elif syllabes[0][0] == 'D':
                    changements.append(syllabes[0][0])

                #Gestion  de F
                elif syllabes[0][0] == 'F':
                    changements.append(syllabes[0][0])

                #Gestion  de G
                elif syllabes[0][0] == 'G':
                    changements.append(syllabes[0][0])

                #Gestion de J
                elif syllabes[0][0] == 'J':
                    changements.append('j')

                #Gestion de K
                elif syllabes[0][0] == 'K':
                    changements.append('c')

                #Gestion de P
                elif syllabes[0][0] == 'P':
                    changements.append(syllabes[0][0])

                #Gestion de Q
                elif syllabes[0][0] == 'Q':
                    changements.append('c')

                #Gestion de S
                elif syllabes[0][0] == 'S':
                    changements.append(syllabes[0][0])

                #Gestion de T
                elif syllabes[0][0] == 'T':
                    changements.append(syllabes[0][0])

                #Gestion de V
                elif syllabes[0][0] == 'V':
                    changements.append(syllabes[0][0])

                #Gestion de X
                elif syllabes[0][0] == 'X':
                    pass

            elif syllabes[0][0] in listes_lettres['consonnes_liquides']:
                #Gestion  de L
                if syllabes[0][0] == 'L':
                    changements.append(syllabes[0][0])

                #Gestion de R
                elif syllabes[0][0] == 'R':
                    changements.append(syllabes[0][0])

            elif syllabes[0][0] in listes_lettres['consonnes_nasales']:
                #Gestion  de M
                if syllabes[0][0] == 'M':
                    changements.append(syllabes[0][0])

                #Gestion de N
                elif syllabes[0][0] == 'N':
                    changements.append(syllabes[0][0])

                #Gestion du H germain
            if syllabes[0][0] == 'H':
                pass

                #Gestion de W
            if syllabes[0][0] == 'W':
                changements.append(syllabes[0][0])

                #Gestion de Y
            if syllabes[0][0] == 'Y':
                changements.append('j')

        #Gestion des différents vocalismes
        #Vocalisme contretonique
        #Gestion de A
        if 'A' in syllabes[0]:
            if syllabes[0][-1] == 'A':
                changements.append('a')
            elif syllabes[0][-2] == 'A':
                changements.append('a')
            elif syllabes[0][-3] == 'A':
                changements.append('a')

        #Gestion de E
        if 'E' in syllabes[0]:
            if syllabes[0][-1] == 'E':
                changements.append('e')
            elif syllabes[0][-2] == 'E':
                changements.append('e')
            elif syllabes[0][-3] == 'E':
                changements.append('e')

        #Gestion de I:
        if 'I' in syllabes[0]:
            if syllabes[0][-1] == 'I':
                changements.append('i')
            elif syllabes[0][-2] == 'I':
                changements.append('i')
            elif syllabes[0][-3] == 'I':
                changements.append('i')


        #Gestion de O:
        if 'O' in syllabes[0]:
            if syllabes[0][-1] == 'O':
                changements.append('o')
            elif syllabes[0][-2] == 'O':
                changements.append('o')
            elif syllabes[0][-3] == 'O':
                changements.append('o')


        #Gestion de U:
        if 'U' in syllabes[0]:
            if syllabes[0][-1] == 'U':
                changements.append('u')
            elif syllabes[0][-2] == 'U':
                changements.append('u')
            elif syllabes[0][-3] == 'U':
                changements.append('u')


        #Vocalisme tonique
        #Gestion de A tonique
        if 'Á' in syllabes[0]:
            if syllabes[0][-1] == 'Á':
                if syllabes[-1][0] in listes_lettres['consonnes_nasales']:
                    changements.append('ai')
                elif syllabes[0][-2] in ['C'. 'G']:
                    changements.append('ie')
                else:
                    changements.append('e')
            elif syllabes[0][-2] == 'Á':
                if syllabes[0][-3] in ['C'. 'G']:
                    changements.append('ie')
                else:
                    changements.append('a')
            elif syllabes[0][-3] == 'Á':
                if syllabes[0][-4] in ['C'. 'G']:
                    changements.append('ie')
                else:
                    changements.append('a')

        #Gestion du E fermé
        if 'Ẹ' in syllabes[0]:
            if syllabes[0][-1] == 'Ẹ':
                #Au contact d'un I long final (Ī)
                if syllabes[1][0] == 'Ī':
                    changements.append('i')
                #Influence d'un I long final (Ī)
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('ie')
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                if syllabes[0][-1] + syllabes[1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('i')
                else:
                    changements.append('ei')
            elif syllabes[0][-2] == 'Ẹ':
                changements.append('e')
            elif syllabes[0][-3] == 'Ẹ':
                changements.append('e')

        #Gestion du E ouvert
        if 'Ę' in syllabes[0]:
            if syllabes[0][-1] == 'Ę':
                #Au contact d'un I long final (Ī)
                if syllabes[1][0] == 'Ī':
                    changements.append('i')
                #Influence d'un I long final (Ī)
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('ie')
                #Au contact d'un yod geminé
                elif syllabes[1][0] == 'J':
                    changements.append("i")
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('i')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                elif syllabes[1][0] == 'X':
                    changements.append('i')
                else:
                    changements.append('ie')
            elif syllabes[0][-2] == 'Ę':
                if syllabes[0][-1] + syllabes[1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('i')
                else:
                    changements.append('e')
            elif syllabes[0][-3] == 'Ę':
                changements.append('e')

        #Gestion de I tonique
        if 'Í' in syllabes[0]:
            if syllabes[0][-1] == 'Í':
                changements.append('i')
            elif syllabes[0][-2] == 'Í':
                #Influence d'une nasale
                if syllabes[0][-1] in listes_lettres['consonnes_nasales']:
                    changements.append('e')
                else:
                    changements.append('i')
            elif syllabes[0][-3] == 'Í':
                changements.append('i')

        #Gestion de O fermé
        if 'Ọ' in syllabes[0]:
            if syllabes[0][-1] == 'Ọ':
                #Influence d'une nasale
                if syllabes[1][0] in listes_lettres['consonnes_nasales']:
                    changements.append('o')
                #Au contact d'un I long final
                if syllabes[1][0] == 'Ī':
                    changements.append('u')
                #Influence d'un I long final (Ī)
                elif syllabes[-1][-1] == 'Ī':
                    changements.append('u')
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('u')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                if syllabes[0][-1] + syllabes[1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('u')
                else:
                    changements.append('ou')
            elif syllabes[0][-2] == 'Ọ':
                changements.append('o')
            elif syllabes[0][-3] == 'Ọ':
                changements.append('o')

        #Gestion de O ouvert
        if 'Ǫ' in syllabes[0]:
            if syllabes[0][-1] == 'Ǫ':
                #Influence d'un I long final (Ī)
                if syllabes[-1][-1] == 'Ī':
                    changements.append('oi')
                #Au contact d'un yod geminé
                elif syllabes[1][0] == 'J':
                    changements.append("ui")
                #Au contact d'un yod geminé  ou en milieu vélaire
                elif syllabes[1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                    changements.append('ui')
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                elif syllabes[1][0] == 'X':
                    changements.append('ui')
                else:
                    changements.append('ue')
            elif syllabes[0][-2] == 'Ǫ':
                #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                if syllabes[0][-1] + syllabes[1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                    changements.append('ui')
                else:
                    changements.append('o')
            elif syllabes[0][-3] == 'Ǫ':
                changements.append('o')

        #Gestion de U
        if 'Ú' in syllabes[0]:
            if syllabes[0][-1] == 'Ú':
                changements.append('u')
            elif syllabes[0][-2] == 'Ú':
                changements.append('u')
            elif syllabes[0][-3] == 'Ú':
                changements.append('u')

        #Idem ici, la machine doit d'abord vérifier la longueur de la syllabe pour savoir si elle est uniquement composée d'une voyelle ou d'autre chose.
        if len(syllabes[0]) == 1:
            pass
        elif syllabes[0] in listes_lettres['désinences_subjonctif']:
            pass
        else:
            #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
            #Consonantisme explosif complexe
            if syllabes[0][-2] + syllabes[0][-1] in listes_lettres['consonantisme_implosif_complexe']:
                pass

            #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
            #Consonantisme implosif
            elif syllabes[0][-1] in listes_lettres['consonnes']:
                pass
                #Gestion de B
                if syllabes[0][-1] == 'B':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de C
                elif syllabes[0][-1] == 'C':
                    #spirantisation
                    changements.append('i')
                #Gestion de D
                elif syllabes[0][-1] == 'D':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion  de F
                elif syllabes[0][-1] == 'F':
                    changements.append('')
                #Gestion  de G
                elif syllabes[0][-1] == 'G':
                    #Après I et E
                    if syllabes[0][-2] in ["Ẹ", "Ę", 'E', 'I', 'Í']:
                        changements.append('i')
                    else:
                        changements.append('u')
                #Gestion de J
                elif syllabes[0][-1] == 'J':
                    pass
                #Gestion de K
                elif syllabes[0][-1] == 'K':
                    pass
                #Gestion de P
                elif syllabes[0][-1] == 'P':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de Q
                elif syllabes[0][-1] == 'Q':
                    pass
                #Gestion de S
                elif syllabes[0][-1] == 'S':
                    changements.append(syllabes[0][-1])
                #Gestion de T
                elif syllabes[0][-1] == 'T':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de V
                elif syllabes[0][-1] == 'V':
                    #S'assimile à la consonne suivante
                    changements.append('')
                #Gestion de X
                elif syllabes[0][-1] == 'X':
                    pass

            elif syllabes[0][-1] in listes_lettres['consonnes_liquides']:
                pass
                #Gestion  de L
                if syllabes[0][-1] == 'L':
                    #Vocalisation en W
                    changements.append('u')
                #Gestion de R
                elif syllabes[0][-1] == 'R':
                    changements.append(syllabes[0][-1])

            elif syllabes[0][-1] in listes_lettres['consonnes_nasales']:
                pass
                #Gestion  de M
                if syllabes[0][-1] == 'M':
                    changements.append(syllabes[0][-1])
                #Gestion de N
                elif syllabes[0][-1] == 'N':
                    changements.append(syllabes[0][-1])

                #Gestion de H

                #Gestion de W
                #Gestion de Y

        return changements
