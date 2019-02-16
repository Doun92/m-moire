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
'BR', 'PR', 'VR', 'DR', 'TR', 'CR', 'GR', 'HR',
'BL', 'FL', 'PL', 'DL', 'TL', 'CL', 'GL', 'HL',
'BW', 'PW', 'VW', 'DW', 'SW', 'TW', 'CW', 'KW', 'GW', 'QW',
'BJ', 'FJ', 'PJ', 'VJ', 'DJ', 'SJ', 'TJ', 'CJ', 'GJ',
'SC', 'SCR', 'SL', 'SN', 'SM', 'SP', 'ST', 'STR',
],

'consonantisme_implosif_complexe': [
'LL',
'NC', 'NG', 'NK',
],

'suffixes' : ['ÁRIU', 'DON', 'JAN'],

'prefixes': ['AD'],

'désinences_présent': ['BET', 'CET', 'DET', 'NIT', 'TET', 'VET'],

'désinences_futur': ['BO'],

'désinences_passé': ['RUNT'],

'désinences_subjonctif': ['CEM']

}

class SyllabeInitiale:

    def __init__(self):
        return

    def syllabe_initiale(self, object):
        syllabes = syllabifier.syllabify(object)

        changements = list()

        if syllabes[0] in listes_lettres['prefixes']:
            if syllabes[0] == 'AD':
                changements.append('a')
        else:
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
                    #Les dentales combinées avec R se simplifient p.40-41, sauf si elles sont en première absolue
                    elif syllabes[0][0] + syllabes[0][1] in ['DR', 'TR']:
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #Les palatales combinées avec R s'affaiblissent toutes en [ir] p.41
                    elif syllabes[0][0] + syllabes[0][1] in ['CR', 'GR']:
                        changements.append('i' + syllabes[0][1])
                    #Gestion de HR, groupe trouvé dans quelques mots d'origine germaine
                    elif syllabes[0][0] + syllabes[0][1] == 'HR':
                        if syllabes[0][2] == 'Ọ':
                            changements.append('f'+syllabes[0][1])
                        elif syllabes[0][2] == 'Ẹ':
                            changements.append(syllabes[0][1])
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
                        changements.append(syllabes[0][0] + syllabes[0][1])
                    #Gestion de la séquence HL issue du germain
                    elif syllabes[0][0] + syllabes[0][1] == 'HL':
                        if syllabes[0][2] == 'Á':
                            changements.append('f' + syllabes[0][1])
                        elif syllabes[0][2] == 'Ọ':
                            changements.append(syllabes[0][1])
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
                    elif syllabes[0][0] + syllabes[0][1] in ['CW', 'GW', 'QW', 'KW']:
                        #la plus ancienne (QW) se prolonge généralement en [v]
                        if syllabes[0][0] + syllabes[0][1] == 'QW':
                            #En final et devant -s ou -t
                            if syllabes[0][1] == syllabes[-1][-1] or syllabes[0][2] in ['S', 'T'] or syllabes[-1][0] in ['S', 'T']:
                                changements.append('u')
                            elif syllabes[0][2] in listes_lettres['voyelles_toniques']:
                                changements.append('c')
                            else:
                                changements.append('v')
                        elif syllabes[0][0] + syllabes[0][1] == 'KW':
                            changements.append('qu')
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
                    #Les S suivis d'une consonne ou d'une sonante subissent une prosthèse
                    elif syllabes[0][0] + syllabes[0][1] + syllabes[0][2] in ['STR', 'SCR']:
                        changements.append('e' + syllabes[0][0] + syllabes[0][1] + syllabes[0][2])
                    elif syllabes[0][0] + syllabes[0][1] in ['SC', 'SL', 'SM', 'SN', 'SP', 'ST']:
                        if syllabes[0][0] + syllabes[0][1] in ['SN']:
                            changements.append('i'+syllabes[0][0] + syllabes[0][1])
                        elif syllabes[0][0] + syllabes[0][1] in ['SL']:
                            if len(syllabes) > 1:
                                if syllabes[0][-1] + syllabes[1][0] == 'TH':
                                    changements.append('escl')
                                else:
                                    changements.append('e'+syllabes[0][0] + syllabes[0][1])
                            #Petite exception pour le mot SLAG du germain
                            elif syllabes[0][2] + syllabes[0][3] == 'ÁG':
                                changements.append('escl')
                            else:
                                changements.append('e'+syllabes[0][0] + syllabes[0][1])
                        elif syllabes[0][0] + syllabes[0][1] in ['SC']:
                            if syllabes[0][2] == 'Á':
                                changements.append('e' + syllabes[0][0] + syllabes[0][1]+'h')
                            else:
                                changements.append('e' + syllabes[0][0] + syllabes[0][1])
                        else:
                            if syllabes[0][-1] == syllabes[-1][-1] == 'G':
                                changements.append('escl')
                            else:
                                changements.append('e'+syllabes[0][0] + syllabes[0][1])

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
                    changements.append('g')

                    #Gestion de Y
                if syllabes[0][0] == 'Y':
                    changements.append('j')

            #Gestion des différents vocalismes
            #Cas où il y a AU
            if 'AU' in syllabes[0]:
                changements.append('o')
            else:
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
                elif 'E' in syllabes[0]:
                    if syllabes[0][-1] == 'E':
                        changements.append('e')
                    elif syllabes[0][-2] == 'E':
                        if syllabes[0][-2] == syllabes[0][0]:
                            if syllabes[0][-1] == 'L':
                                changements.append('a')
                            else:
                                changements.append('e')
                        else:
                            changements.append('e')
                    elif syllabes[0][-3] == 'E':
                        changements.append('e')

                #Gestion de I:
                elif 'I' in syllabes[0]:
                    if syllabes[0][-1] == 'I':
                        changements.append('i')
                    elif syllabes[0][-2] == 'I':
                        changements.append('i')
                    elif syllabes[0][-3] == 'I':
                        changements.append('i')


                #Gestion de O:
                elif 'O' in syllabes[0]:
                    if syllabes[0][-1] == 'O':
                        changements.append('o')
                    elif syllabes[0][-2] == 'O':
                        changements.append('o')
                    elif syllabes[0][-3] == 'O':
                        changements.append('o')


                #Gestion de U:
                elif 'U' in syllabes[0]:
                    if syllabes[0][-1] == 'U':
                        changements.append('u')
                    elif syllabes[0][-2] == 'U':
                        changements.append('u')
                    elif syllabes[0][-3] == 'U':
                        changements.append('u')


                #Vocalisme tonique
                #Gestion de A tonique
                elif 'Á' in syllabes[0]:
                    if syllabes[0][-1] == 'Á':
                        if len(syllabes[0]) > 1:
                            if syllabes[0][-2] in ['C', 'G']:
                                changements.append('ie')
                            elif syllabes[-1][0] in listes_lettres['consonnes_nasales']:
                                changements.append('ai')
                            #Présence d'un yod
                            elif syllabes[-1][0] == 'Y':
                                changements.append('ai')
                            else:
                                changements.append('e')
                        else:
                            if syllabes[-1][0] in listes_lettres['consonnes_nasales']:
                                changements.append('ai')
                            #Présence d'un yod
                            elif syllabes[-1][0] == 'Y':
                                changements.append('ai')
                            else:
                                changements.append('e')
                    elif syllabes[0][-2] == 'Á':
                        #Travail sur le mot
                        #Fermeture de la bouche en milieu monosyllabique
                        if len(syllabes) == 1:
                            if syllabes[0][-1] == 'G' : #En ajouter d'autres, à chercher
                                changements.append('o')
                            else:
                                changements.append('a')
                        #Travail sur la syllabe en elle-même
                        elif len(syllabes[0]) > 2:
                            if syllabes[0][-3] in ['C', 'G']:
                                changements.append('ie')
                            else:
                                changements.append('a')
                        else:
                            changements.append('a')
                    elif syllabes[0][-3] == 'Á':
                        if syllabes[0][-4] in ['C', 'G']:
                            changements.append('ie')
                        else:
                            changements.append('a')

                #Gestion du E fermé
                elif 'Ẹ' in syllabes[0]:
                    if syllabes[0][-1] == 'Ẹ':
                        if len(syllabes) == 1:
                            changements.append('ei')
                        else:
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
                elif 'Ę' in syllabes[0]:
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
                        elif len(syllabes[1]) == 2:
                            if syllabes[1] == 'RI':
                                changements.append('e')
                        else:
                            changements.append('ie')
                    elif syllabes[0][-2] == 'Ę':
                        #Gestion des plurisyllabiques
                        if len(syllabes) > 1:
                            if syllabes[0][-1] + syllabes[1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                                changements.append('i')
                            else:
                                changements.append('e')
                        else:
                            if syllabes[0][-1] == 'M':
                                changements.append('ie')
                            #Ouverture de la bouche
                            elif syllabes[0][-1] == syllabes[-1][-1] == 'R':
                                changements.append('a')
                            else:
                                changements.append('e')
                    elif syllabes[0][-3] == 'Ę':
                        changements.append('e')

                #Gestion de I tonique
                elif 'Í' in syllabes[0]:
                    if syllabes[0][-1] == 'Í':
                        #Fermeture face à un O final
                        if syllabes[1][0] == syllabes[-1][-1] == 'O':
                            changements.append('u')
                        else:
                            changements.append('i')
                    elif syllabes[0][-2] == 'Í':
                        #Influence d'une nasale
                        if syllabes[0][-1] in listes_lettres['consonnes_nasales']:
                            #Présence d'un yod avec la nasale
                            if syllabes[1][0] == 'Y':
                                changements.append('i')
                            else:
                                changements.append('e')
                        else:
                            changements.append('i')
                    elif syllabes[0][-3] == 'Í':
                        changements.append('i')

                #Gestion de O fermé
                elif 'Ọ' in syllabes[0]:
                    if syllabes[0][-1] == 'Ọ':
                        #Influence d'une nasale
                        if syllabes[1][0] in listes_lettres['consonnes_nasales']:
                            changements.append('o')
                        #Au contact d'un I long final
                        elif syllabes[1][0] == 'Ī':
                            changements.append('u')
                        #Influence d'un I long final (Ī)
                        elif syllabes[-1][-1] == 'Ī':
                            changements.append('u')
                        #Au contact d'un yod geminé  ou en milieu vélaire
                        elif syllabes[1] in ['BJ', 'VJ', 'DJ', 'GJ', 'GI', 'GE']:
                            changements.append('u')
                        #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                        elif syllabes[0][-1] + syllabes[1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                            changements.append('u')
                        else:
                            changements.append('ou')
                    elif syllabes[0][-2] == 'Ọ':
                        changements.append('o')
                    elif syllabes[0][-3] == 'Ọ':
                        changements.append('o')

                #Gestion de O ouvert
                elif 'Ǫ' in syllabes[0]:
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
                        if len(syllabes) > 1:
                            #Au contact d'un élément ou d'un groupe comportant ou dégageant un yod
                            if syllabes[0][-1] + syllabes[1][0] in ['CT', 'SJ', 'LJ', 'CL', 'ST']:
                                changements.append('ui')
                            else:
                                changements.append('o')
                        else:
                            changements.append('o')
                    elif syllabes[0][-3] == 'Ǫ':
                        changements.append('o')

                #Gestion de U
                elif 'Ú' in syllabes[0]:
                    if syllabes[0][-1] == 'Ú':
                        changements.append('u')
                    elif syllabes[0][-2] == 'Ú':
                        changements.append('u')
                    elif syllabes[0][-3] == 'Ú':
                        changements.append('u')

            #Idem ici, la machine doit d'abord vérifier la longueur de la syllabe pour savoir si elle est uniquement composée d'une voyelle ou d'autre chose.
            if len(syllabes[0]) == 1:
                pass
            else:
                #D'abord l'algorithme vérifie s'il à affaire avec un élément consonantique complexe
                #Consonantisme explosif complexe
                if syllabes[0][-2] + syllabes[0][-1] in listes_lettres['consonantisme_implosif_complexe']:
                    if syllabes[0][-2] + syllabes[0][-1] in ['NC', 'NG', 'NK']:
                        changements.append(syllabes[0][-2] + 'c')
                    elif syllabes[0][-2] + syllabes[0][-1] == 'LL':
                        changements.append(syllabes[0][-1])

                #Si ce n'est pas le cas, il traitera de l'élément consonantique simple
                #Consonantisme implosif
                elif syllabes[0][-1] in listes_lettres['consonnes']:
                    #Gestion de B
                    if syllabes[0][-1] == 'B':
                        #S'assimile à la consonne suivante
                        changements.append('')
                    #Gestion de C
                    elif syllabes[0][-1] == 'C':
                        if syllabes[0][-1] == syllabes[-1][-1] and syllabes[0][-2] == 'Ǫ':
                            changements.append('')
                        else:
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
                        if syllabes[0][-1] == syllabes[-1][-1]:
                            changements.append('c')
                        else:
                            changements.append('')
                    #Gestion de P
                    elif syllabes[0][-1] == 'P':
                        #S'assimile à la consonne suivante
                        changements.append('')
                    #Gestion de Q
                    elif syllabes[0][-1] == 'Q':
                        pass
                    #Gestion de S
                    elif syllabes[0][-1] == 'S':
                        if syllabes[1][0] == 'S':
                            changements.append('')
                        else:
                            changements.append(syllabes[0][-1])
                    #Gestion de T
                    elif syllabes[0][-1] == 'T':
                        if syllabes[0][-1] == syllabes[-1][-1]:
                            changements.append(syllabes[0][-1])
                        else:
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
                        #Gestion d'un plurisyllabiques
                        if len(syllabes) > 1:
                            #Vocalisation en W
                            if syllabes[1][0] == 'W':
                                changements.append('u')
                            #L devant M
                            elif syllabes[1][0] == 'M':
                                changements.append(syllabes[0][-1])
                            #L devant T
                            elif syllabes[1][0] == 'T':
                                changements.append('u')
                            #L face à Y
                            elif syllabes[1][0] == 'Y':
                                #Différentiation entre le féminin et le masculin
                                if syllabes[1][1] == syllabes[-1][-1] == 'A':
                                    changements.append(syllabes[0][-1] + syllabes[0][-1])
                                else:
                                    changements.append(syllabes[0][-1])
                            else:
                                changements.append('')
                        else:
                            changements.append('')
                    #Gestion de R
                    elif syllabes[0][-1] == 'R':
                        changements.append(syllabes[0][-1])

                elif syllabes[0][-1] in listes_lettres['consonnes_nasales']:
                    pass
                    #Gestion  de M
                    if syllabes[0][-1] == 'M':
                        if syllabes[0][-2] == 'Ę':
                            changements.append('n')
                        elif syllabes[1][0] in ['T', 'D']:
                            changements.append('n')
                        else:
                            changements.append(syllabes[0][-1])
                    #Gestion de N
                    elif syllabes[0][-1] == 'N':
                        if len(syllabes) == 1:
                            changements.append(syllabes[0][-1])
                        else:
                            #Mouillure de la nasale
                            if syllabes[1][0] == 'Y':
                                changements.append('gn')
                            else:
                                changements.append(syllabes[0][-1])

                    #Gestion de H

                    #Gestion de W
                    #Gestion de Y


        return changements
