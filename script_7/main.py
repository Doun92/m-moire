"""
Ce script unit tous les autres scrits qui s'occupent de tâches plus ponctuelles.
Il parcourt chaque mot, lettre par lettre ou syllabe par syllabe, selon les particularités de chacun.

auteur : Daniel Escoval
license : license UNIL
"""

class EvolutionPhonetique:

    def __init__(self):
        return

    def evolution_phonetique(self):

        from syllabifier import Syllabifier
        syllabifier = Syllabifier()

        # from mot_1_syllabe import MotUneSyllabe
        # monosyllabique = MotUneSyllabe()

        from AA1_syllabe_initiale import SyllabeInitiale
        syllabe_initiale = SyllabeInitiale()

        from AA2_syllabe_contrepenultieme import SyllabeContrepenultieme
        syllabe_contrepenultieme = SyllabeContrepenultieme()

        from AA3_syllabe_contrefinale import SyllabeContrefinale
        syllabe_contrefinale = SyllabeContrefinale()

        from AA4_syllabe_ante_penultieme import SyllabeAntePenultieme
        syllabe_ante_penultieme = SyllabeAntePenultieme()

        from AA5_syllabe_pénultième import SyllabePenultieme
        syllabe_penultieme = SyllabePenultieme()

        from AA6_syllabe_finale import SyllabeFinale
        syllabe_finale = SyllabeFinale()

        # print('----------------------------------------')
        # print(self)

        syllabes = syllabifier.syllabify(self)
        # print(syllabes)
        # print(syllabes[0])
        # print(len(syllabes))

        changements = list()


        #Première syllabe et/ou préfixe
        if len(syllabes) > 0:
            changements.append(syllabe_initiale.syllabe_initiale(self))

        #Syllabe contrepénultième
        if len(syllabes) > 5:
            changements.append(syllabe_contrepenultieme.syllabe_contrepenultieme(self))

        #Syllabe contrefinale
        if len(syllabes) > 4:
            changements.append(syllabe_contrefinale.syllabe_contrefinale(self))

        #Anté-pénultième syllabe
        if len(syllabes) > 3:
            changements.append(syllabe_ante_penultieme.syllabe_ante_penultieme(self))

        #Pénultième syllabe
        if len(syllabes) > 2:
            changements.append(syllabe_penultieme.syllabe_penultieme(self))

        #Dernière syllabe
        if len(syllabes) > 1:
            changements.append(syllabe_finale.syllabe_finale(self))

        flat_list = [item for sublist in changements for item in sublist]
        # print(flat_list)



        output = "".join(flat_list)
        # print(output)
        output = output.lower()

        return output

        # return changements
"""
Le Ī fonctionne, voir si je peux le mettre pour les I en yod,
ne pas oublier de les mettre dans les voyelles du Syllaifier
Le Į ogonek fonctionne éfalement, à voir

Le Ụ, Ū, et Ų fonctionnent, à voir ce que je peux faire avec
"""
"""
Penser à diviser les consonnes par longueur de syllabes à l'intérieur de la gestion des consonnes

'voyelles_toniques' : ["Ẹ", "Ę", "Á", "Ǫ", "Ọ", "Ú", 'Í']
"""

"""
J'ai encore un petit soucis avec la séquence ÁL, à voir
"""


# print(EvolutionPhonetique.evolution_phonetique("DUỌS"))         #dous
# print(EvolutionPhonetique.evolution_phonetique("PẸRA"))         #peire
# print(EvolutionPhonetique.evolution_phonetique("TẸLA"))         #teile
# print(EvolutionPhonetique.evolution_phonetique("TẸCTO"))        #teit
# print(EvolutionPhonetique.evolution_phonetique("GỌLA"))         #goule
# print(EvolutionPhonetique.evolution_phonetique("FLỌRE"))        #flour
# print(EvolutionPhonetique.evolution_phonetique("CỌRSO"))        #cors
# print(EvolutionPhonetique.evolution_phonetique("PẸNA"))         #peine
# print(EvolutionPhonetique.evolution_phonetique("CĘLO"))         #ciel
# print(EvolutionPhonetique.evolution_phonetique("LĘTOS"))        #liez
# print(EvolutionPhonetique.evolution_phonetique("SẸTA"))         #seie
# print(EvolutionPhonetique.evolution_phonetique("SẸPE"))         #seif
# print(EvolutionPhonetique.evolution_phonetique("AURO"))         #or
# print(EvolutionPhonetique.evolution_phonetique("PAUCA"))        #poe
# print(EvolutionPhonetique.evolution_phonetique("VẸRGA"))        #verge
# print(EvolutionPhonetique.evolution_phonetique("MẸSA"))         #meise
# print(EvolutionPhonetique.evolution_phonetique("MÚRO"))         #mur
# print(EvolutionPhonetique.evolution_phonetique("PǪRTA"))        #porte
# print(EvolutionPhonetique.evolution_phonetique("PÁRTE"))        #part
# print(EvolutionPhonetique.evolution_phonetique("GỌTTA"))        #gote
# print(EvolutionPhonetique.evolution_phonetique("PÁTRE"))        #pere
# print(EvolutionPhonetique.evolution_phonetique("CỌDA"))          #coue
# print(EvolutionPhonetique.evolution_phonetique("ẸSCA"))         #esche
# print(EvolutionPhonetique.evolution_phonetique("FÚSTE"))        #fust
# print(EvolutionPhonetique.evolution_phonetique("CLAUSTRA"))     #clostre
# print(EvolutionPhonetique.evolution_phonetique("RÍPA"))         #rive
# print(EvolutionPhonetique.evolution_phonetique("FẸDE"))         #fei
# print(EvolutionPhonetique.evolution_phonetique("TẸLA"))         #teile
# print(EvolutionPhonetique.evolution_phonetique("SẸTA"))         #seie
# print(EvolutionPhonetique.evolution_phonetique("MÁRE"))         #mer
# print(EvolutionPhonetique.evolution_phonetique("FÁTA"))         #fee
# print(EvolutionPhonetique.evolution_phonetique("CǪRE"))         #cuer
# print(EvolutionPhonetique.evolution_phonetique("CÚRA"))         #cure
# print(EvolutionPhonetique.evolution_phonetique("CAUSA"))        #chose
# print(EvolutionPhonetique.evolution_phonetique("FÍLYA"))        #fille
# print(EvolutionPhonetique.evolution_phonetique("KWẸTO"))        #quei
# print(EvolutionPhonetique.evolution_phonetique("CỌRTE"))        #cort
# print(EvolutionPhonetique.evolution_phonetique("MÁSCLU"))       #masle
# print(EvolutionPhonetique.evolution_phonetique("VĘCLO"))        #vieil
# print(EvolutionPhonetique.evolution_phonetique("VẸRDE"))        #vert
# print(EvolutionPhonetique.evolution_phonetique("VÍNO"))         #vin
# print(EvolutionPhonetique.evolution_phonetique("ỌRA"))          #oure
# print(EvolutionPhonetique.evolution_phonetique("ǪMO"))          #uem
# print(EvolutionPhonetique.evolution_phonetique("MẸA"))          #meie
# print(EvolutionPhonetique.evolution_phonetique("TỌA"))          #toue
# print(EvolutionPhonetique.evolution_phonetique("SỌA"))          #soue
# print(EvolutionPhonetique.evolution_phonetique("DỌAS"))         #doues
# print(EvolutionPhonetique.evolution_phonetique("TǪOM"))         #tuen
# print(EvolutionPhonetique.evolution_phonetique("SǪOM"))         #suen
# print(EvolutionPhonetique.evolution_phonetique("TǪOS"))         #tos
# print(EvolutionPhonetique.evolution_phonetique("SǪOS"))         #sos
# print(EvolutionPhonetique.evolution_phonetique("VẸA"))          #veie
# print(EvolutionPhonetique.evolution_phonetique("SẸA"))          #seie
# print(EvolutionPhonetique.evolution_phonetique("CRÍTAT"))       #crie
# print(EvolutionPhonetique.evolution_phonetique("PLÁNCA"))       #planche
# print(EvolutionPhonetique.evolution_phonetique("ÁMAT"))         #aime
# print(EvolutionPhonetique.evolution_phonetique("ẸNTRO"))        #entre
# print(EvolutionPhonetique.evolution_phonetique("VẸRDE"))        #vert
# print(EvolutionPhonetique.evolution_phonetique("DỌMNA"))        #dame
# print(EvolutionPhonetique.evolution_phonetique("CỌMTE"))        #comte
# print(EvolutionPhonetique.evolution_phonetique("RÍO"))          #ru
# print(EvolutionPhonetique.evolution_phonetique("DÍE"))          #di
# print(EvolutionPhonetique.evolution_phonetique("MÁYOR"))            #maire 2
# print(EvolutionPhonetique.evolution_phonetique("SĘNYOR"))           #seindre 2
# print(EvolutionPhonetique.evolution_phonetique("VÍNYA"))        #vigne
# print(EvolutionPhonetique.evolution_phonetique("BĘNE"))    #bien 2
# print(EvolutionPhonetique.evolution_phonetique("HỌMO"))     #uem 2
# print(EvolutionPhonetique.evolution_phonetique("CÁNE"))     #chien 2
# print(EvolutionPhonetique.evolution_phonetique("CỌMES"))    #cuens 2
# print(EvolutionPhonetique.evolution_phonetique("PLẸNA"))    #pleine 2
# print(EvolutionPhonetique.evolution_phonetique("PỌMA"))     #pome 2
# print(EvolutionPhonetique.evolution_phonetique("PỌNTE"))    #pont 2
# print(EvolutionPhonetique.evolution_phonetique("ẸNTRAT"))     #entre 2
# print(EvolutionPhonetique.evolution_phonetique("NỌMEN"))      #nom 2
# print(EvolutionPhonetique.evolution_phonetique("NÁNU"))        #nain 2
# print(EvolutionPhonetique.evolution_phonetique("NÁSUS"))        #nes 2
# print(EvolutionPhonetique.evolution_phonetique("GRÁNU"))       #grain 2
# print(EvolutionPhonetique.evolution_phonetique("GRÁDUS"))   #gre 2
# print(EvolutionPhonetique.evolution_phonetique("CÁNIS"))    #chien 2
# print(EvolutionPhonetique.evolution_phonetique("CÁSUS"))    #cas 2
# print(EvolutionPhonetique.evolution_phonetique("HĘRĪ"))         #ier 2
# print(EvolutionPhonetique.evolution_phonetique("MĘĪ"))          #mi 2
# print(EvolutionPhonetique.evolution_phonetique("LĘGIT"))        #lit 2
# print(EvolutionPhonetique.evolution_phonetique("ĘXIT"))         #ist 2
# print(EvolutionPhonetique.evolution_phonetique("NǪCTE"))        #nuit 2
# print(EvolutionPhonetique.evolution_phonetique("CǪXA"))         #cuisse 2
# print(EvolutionPhonetique.evolution_phonetique("LǪNGE"))        #loin 2
# print(EvolutionPhonetique.evolution_phonetique("DĘCEM"))        #dis 2
# print(EvolutionPhonetique.evolution_phonetique("NǪCET"))        #nuist 2
# print(EvolutionPhonetique.evolution_phonetique("TǪRCET"))       #tort 2
# print(EvolutionPhonetique.evolution_phonetique("DĘU"))          #dieu 2
# print(EvolutionPhonetique.evolution_phonetique("MĘUM"))         #mien 2
# print(EvolutionPhonetique.evolution_phonetique("ĘO"))           #je 2
# print(EvolutionPhonetique.evolution_phonetique("BRĘVE"))        #brief 2
# print(EvolutionPhonetique.evolution_phonetique("LĘVE"))         #lief 2
# print(EvolutionPhonetique.evolution_phonetique("GRĘVE"))        #grief 2
# print(EvolutionPhonetique.evolution_phonetique("BǪVE"))         #buef 2
# print(EvolutionPhonetique.evolution_phonetique("NǪVE"))         #nuef 2
# print(EvolutionPhonetique.evolution_phonetique("ǪPUS"))         #ues 2
# print(EvolutionPhonetique.evolution_phonetique("CẸSTĪ"))        #cist 2
# print(EvolutionPhonetique.evolution_phonetique("FỌSTI"))        #fust 2
# print(EvolutionPhonetique.evolution_phonetique("TỌTTĪ"))        #tuit 2
# print(EvolutionPhonetique.evolution_phonetique("FỌĪ"))          #fui 2
# print(EvolutionPhonetique.evolution_phonetique("LẸGAT"))        #leie 2
# print(EvolutionPhonetique.evolution_phonetique("NǪCTE"))        #nuit 2
# print(EvolutionPhonetique.evolution_phonetique("LǪCAT"))        #loue 2
# print(EvolutionPhonetique.evolution_phonetique("LỌPA"))        #louve 2
# print(EvolutionPhonetique.evolution_phonetique("DỌGA"))        #douve 2
# print(EvolutionPhonetique.evolution_phonetique("SỌCA"))        #soue 2
# print(EvolutionPhonetique.evolution_phonetique("CẸRA"))        #cire 2
# print(EvolutionPhonetique.evolution_phonetique("CÁPRA"))        #chievre 2
# print(EvolutionPhonetique.evolution_phonetique("VẸRDES"))      #verz 2
# print(EvolutionPhonetique.evolution_phonetique("MỌNTE"))      #mont 2
# print(EvolutionPhonetique.evolution_phonetique("TÁNTOS"))      #tanz 2
# print(EvolutionPhonetique.evolution_phonetique("VẸNDIT"))      #vent 2
# print(EvolutionPhonetique.evolution_phonetique("DỌLCE"))      #douz 2
# print(EvolutionPhonetique.evolution_phonetique("GẸNTE"))      #gent 2
# print(EvolutionPhonetique.evolution_phonetique("LÁRGA"))      #large 2
# print(EvolutionPhonetique.evolution_phonetique("GÁNTA"))      #jante 2
# print(EvolutionPhonetique.evolution_phonetique("VÍLLA"))         #vile 2
# print(EvolutionPhonetique.evolution_phonetique("WÁRJAN"))         #garir 2
# print(EvolutionPhonetique.evolution_phonetique("WÁRDON"))         #garder 2
# print(EvolutionPhonetique.evolution_phonetique("VĘSPA"))         #guespe 2
# print(EvolutionPhonetique.evolution_phonetique("PỌNRE"))         #pondre 2
# print(EvolutionPhonetique.evolution_phonetique("SPÍNLA"))         #espingle 2
# print(EvolutionPhonetique.evolution_phonetique("SẸNIR"))         #sendra 2 #??
# print(EvolutionPhonetique.evolution_phonetique("MǪLRE"))         #moldre 2
# print(EvolutionPhonetique.evolution_phonetique("CǪSRE"))         #cosdre 2
# print(EvolutionPhonetique.evolution_phonetique("PRẸSRUNT"))         #prisdrent 2
# print(EvolutionPhonetique.evolution_phonetique("ÍSLA"))         #isle 2
# print(EvolutionPhonetique.evolution_phonetique("ĘSSRE"))         #estre 2
# print(EvolutionPhonetique.evolution_phonetique("DÍXRUNT"))         #distrent 2
# print(EvolutionPhonetique.evolution_phonetique("MÁRMR"))         #marbre 2
# print(EvolutionPhonetique.evolution_phonetique("PRÚNA"))         #prune 2
# print(EvolutionPhonetique.evolution_phonetique("BRÁNCA"))         #branche 2
# print(EvolutionPhonetique.evolution_phonetique("ỌMBRA"))         #ombre 2
# print(EvolutionPhonetique.evolution_phonetique("FRÁTER"))         #frere 2
# print(EvolutionPhonetique.evolution_phonetique("DRÁPPU"))         #drap 2
# print(EvolutionPhonetique.evolution_phonetique("MỌRDRE"))         #mordre 2
# print(EvolutionPhonetique.evolution_phonetique("CRỌCE"))         #croiz 2
# print(EvolutionPhonetique.evolution_phonetique("GRÁNDE"))         #grant 2
# print(EvolutionPhonetique.evolution_phonetique("BLÁNCA"))         #blanche 2
# print(EvolutionPhonetique.evolution_phonetique("FLỌRE"))         #flour 2
# print(EvolutionPhonetique.evolution_phonetique("CLÁVE"))         #clef 2
# print(EvolutionPhonetique.evolution_phonetique("GLÁNDE"))         #glant 2
# print(EvolutionPhonetique.evolution_phonetique("ỌNGLA"))         #ongle 2
# print(EvolutionPhonetique.evolution_phonetique("CHÁRTLA"))         #chartre 2
# print(EvolutionPhonetique.evolution_phonetique("ÁMPLU"))         #ample 2
# print(EvolutionPhonetique.evolution_phonetique("DJỌRNU"))    #jorn 2
# print(EvolutionPhonetique.evolution_phonetique("CEỌC"))    #ço 2
# print(EvolutionPhonetique.evolution_phonetique("MÁSCLU"))         #masle 2
# print(EvolutionPhonetique.evolution_phonetique("CẸRCLU"))         #cercle 2
# print(EvolutionPhonetique.evolution_phonetique("CỌNGRU"))         #congre 2
# print(EvolutionPhonetique.evolution_phonetique("PLÁNGRE"))    #plaindre 2
# print(EvolutionPhonetique.evolution_phonetique("SỌRGRE"))    #sordre 2
# print(EvolutionPhonetique.evolution_phonetique("FỌLGRE"))    #foudre 2
# print(EvolutionPhonetique.evolution_phonetique("ÁSPRU"))         #aspre 2
# print(EvolutionPhonetique.evolution_phonetique("VÁDU"))         #gué 2
# print(EvolutionPhonetique.evolution_phonetique("SÁLVU"))         #salf 2
# print(EvolutionPhonetique.evolution_phonetique("SĘRVUS"))         #cers 2
# print(EvolutionPhonetique.evolution_phonetique("NǪVU"))         #nuef 2
# print(EvolutionPhonetique.evolution_phonetique("RÍVU"))         #ru 2
# print(EvolutionPhonetique.evolution_phonetique("PSÁLMU"))    #salme 2
# print(EvolutionPhonetique.evolution_phonetique("CÁRU"))        #chier 2
# print(EvolutionPhonetique.evolution_phonetique("CẸNTU"))      #cent 2
# print(EvolutionPhonetique.evolution_phonetique("ǪRBU"))      #orb 2
# print(EvolutionPhonetique.evolution_phonetique("PỌGNU"))        #poing 2
# print(EvolutionPhonetique.evolution_phonetique("LĘCTU"))        #lit 2
# print(EvolutionPhonetique.evolution_phonetique("ǪCLU"))         #ueil 2
# print(EvolutionPhonetique.evolution_phonetique("LĘCTU"))        #lit 2
# print(EvolutionPhonetique.evolution_phonetique("FĘRRU"))        #fer
# print(EvolutionPhonetique.evolution_phonetique("PǪRTU"))        #port
# print(EvolutionPhonetique.evolution_phonetique("TỌTTU"))        #tot
# print(EvolutionPhonetique.evolution_phonetique("FĘRU"))         #fier
# print(EvolutionPhonetique.evolution_phonetique("CĘLU"))         #ciel
# print(EvolutionPhonetique.evolution_phonetique("DRẸCTU"))       #dreit
# print(EvolutionPhonetique.evolution_phonetique("CẸSTU"))        #cest
# print(EvolutionPhonetique.evolution_phonetique("ǪCLU"))         #ueil
# print(EvolutionPhonetique.evolution_phonetique("FÍLYU"))        #fil
# print(EvolutionPhonetique.evolution_phonetique("BỌNU"))     #bon 2
# print(EvolutionPhonetique.evolution_phonetique("MÁNU"))     #main 2
# print(EvolutionPhonetique.evolution_phonetique("VÍNU"))     #vin 2
# print(EvolutionPhonetique.evolution_phonetique("VĘCLU"))        #vieil 2
# print(EvolutionPhonetique.evolution_phonetique("MỌNDU"))      #mont 2
# print(EvolutionPhonetique.evolution_phonetique("CÁPU"))         #chief 2
# print(EvolutionPhonetique.evolution_phonetique("LÁCU"))         #lai 2
# print(EvolutionPhonetique.evolution_phonetique("LǪCU"))         #lieu 2
# print(EvolutionPhonetique.evolution_phonetique("LǪCU"))         #lieu 2
# print(EvolutionPhonetique.evolution_phonetique("PAUCÚ"))         #pou 2
# print(EvolutionPhonetique.evolution_phonetique("VÍSU"))         #vis 2
# print(EvolutionPhonetique.evolution_phonetique("PRÁTU"))         #pre #2
# print(EvolutionPhonetique.evolution_phonetique("CÁMPU"))         #champ 2
# print(EvolutionPhonetique.evolution_phonetique("FÁBRU"))         #fevre 2
# print(EvolutionPhonetique.evolution_phonetique("RÍSU"))         #ris 2
# print(EvolutionPhonetique.evolution_phonetique("BỌNU"))         #bon 2
# print(EvolutionPhonetique.evolution_phonetique("SǪCRU"))         #suire 2
# print(EvolutionPhonetique.evolution_phonetique("DỌPLU"))         #doble 2
# print(EvolutionPhonetique.evolution_phonetique("ÁPTU"))         #ate 2
# print(EvolutionPhonetique.evolution_phonetique("SCRÍPTU"))         #escrit 2
# print(EvolutionPhonetique.evolution_phonetique("ẸPSU"))         #es 2
# print(EvolutionPhonetique.evolution_phonetique("DẸBTU"))         #det 2
# print(EvolutionPhonetique.evolution_phonetique("PỌGNU"))         #poing 2
# print(EvolutionPhonetique.evolution_phonetique("GẸNTU"))         #gent 2
# print(EvolutionPhonetique.evolution_phonetique("ÁRCU"))         #arc 2
# print(EvolutionPhonetique.evolution_phonetique("DJỌRNU"))         #jorn 2
# print(EvolutionPhonetique.evolution_phonetique("DAMNU"))         #dam 2
# print(EvolutionPhonetique.evolution_phonetique("HÁLTU"))         #haut 2
# print(EvolutionPhonetique.evolution_phonetique("PĘSSMU"))         #pesme 2
# print(EvolutionPhonetique.evolution_phonetique("CÁSSNU"))         #chasne 2
# print(EvolutionPhonetique.evolution_phonetique("PESSLU"))         #pesle 2
# print(EvolutionPhonetique.evolution_phonetique("SỌMMU"))         #som 2
# print(EvolutionPhonetique.evolution_phonetique("CÁRRU"))         #char 2
# print(EvolutionPhonetique.evolution_phonetique("ÁNNU"))         #an 2
# print(EvolutionPhonetique.evolution_phonetique("RẸGDU"))         #reide 2
# print(EvolutionPhonetique.evolution_phonetique("PLÁNCTU"))    #plaint 2
# print(EvolutionPhonetique.evolution_phonetique("CỌGNTU"))    #cointe 2
# print(EvolutionPhonetique.evolution_phonetique("PÁLMA"))         #paume 2
# print(EvolutionPhonetique.evolution_phonetique("SPÍNA"))    #espine 2
# print(EvolutionPhonetique.evolution_phonetique("STÁRE"))    #ester 2
# print(EvolutionPhonetique.evolution_phonetique("SCÁLA"))    #eschiele 2
# print(EvolutionPhonetique.evolution_phonetique("SLÁTHA"))    #esclate 2
# print(EvolutionPhonetique.evolution_phonetique("STRẸNA"))    #estreine 2
# print(EvolutionPhonetique.evolution_phonetique("CỌPPA"))         #cope 2
# print(EvolutionPhonetique.evolution_phonetique("GỌTTA"))         #gote 2
# print(EvolutionPhonetique.evolution_phonetique("BỌCCA"))         #boche 2
# print(EvolutionPhonetique.evolution_phonetique("CÚPA"))         #cuve 2
# print(EvolutionPhonetique.evolution_phonetique("VÍTA"))         #vie 2
# print(EvolutionPhonetique.evolution_phonetique("BÁCA"))         #baie 2
# print(EvolutionPhonetique.evolution_phonetique("ÁLBA"))         #aube 2
# print(EvolutionPhonetique.evolution_phonetique("TỌMBA"))         #tombe 2
# print(EvolutionPhonetique.evolution_phonetique("CỌBAT"))        #couve 2
# print(EvolutionPhonetique.evolution_phonetique("FÁBA"))         #feve 2
# print(EvolutionPhonetique.evolution_phonetique("NÚBA"))         #nue 2
# print(EvolutionPhonetique.evolution_phonetique("TRÁBE"))         #tref 2
# print(EvolutionPhonetique.evolution_phonetique("DẸBET"))         #deit 2
# print(EvolutionPhonetique.evolution_phonetique("SẸBU"))         #sui 2 #??
# print(EvolutionPhonetique.evolution_phonetique("PRǪBO"))         #pruis 2
# print(EvolutionPhonetique.evolution_phonetique("RÍPA"))         #rive 2
# print(EvolutionPhonetique.evolution_phonetique("LỌPA"))         #louve 2
# print(EvolutionPhonetique.evolution_phonetique("NĘPOS"))         #nies 2
# print(EvolutionPhonetique.evolution_phonetique("PRǪPE"))         #pruef 2
# print(EvolutionPhonetique.evolution_phonetique("LỌPUS"))         #lous 2
# print(EvolutionPhonetique.evolution_phonetique("PẸCE"))         #peiz 2
# print(EvolutionPhonetique.evolution_phonetique("CRỌCIS"))         #croiz 2
# print(EvolutionPhonetique.evolution_phonetique("FẸCIT"))         #fist 2
# print(EvolutionPhonetique.evolution_phonetique("LÚCET"))        #luist 2
# print(EvolutionPhonetique.evolution_phonetique("FÁGIT"))         #fait 2
# print(EvolutionPhonetique.evolution_phonetique("LẸGE"))         #lei 2
# print(EvolutionPhonetique.evolution_phonetique("MÁGIS"))         #mais 2
# print(EvolutionPhonetique.evolution_phonetique("PLÁGA"))         #plaie 2
# print(EvolutionPhonetique.evolution_phonetique("RÚGA"))         #rue 2
# print(EvolutionPhonetique.evolution_phonetique("BRÁCAS"))         #braies 2
# print(EvolutionPhonetique.evolution_phonetique("AUCA"))         #oe 2
# print(EvolutionPhonetique.evolution_phonetique("PLẸCO"))         #plei 2
# print(EvolutionPhonetique.evolution_phonetique("VÍTA"))         #vie #2
# print(EvolutionPhonetique.evolution_phonetique("PǪTET"))         #puet #2
# print(EvolutionPhonetique.evolution_phonetique("FẸDE"))         #fei #2
# print(EvolutionPhonetique.evolution_phonetique("VẸDET"))         #veit #2
# print(EvolutionPhonetique.evolution_phonetique("ÁRDET"))      #art 2
# print(EvolutionPhonetique.evolution_phonetique("AUDET"))        #ot
# print(EvolutionPhonetique.evolution_phonetique("PẸDES"))         #piez #2
# print(EvolutionPhonetique.evolution_phonetique("RǪSA"))         #rose 2
# print(EvolutionPhonetique.evolution_phonetique("CAUSA"))         #chose 2
# print(EvolutionPhonetique.evolution_phonetique("PRẸSIT"))         #prist 2
# print(EvolutionPhonetique.evolution_phonetique("VẸNIT"))         #vient 2
# print(EvolutionPhonetique.evolution_phonetique("CÁNIS"))         #chiens 2
# print(EvolutionPhonetique.evolution_phonetique("SẸNES"))         #sens 2
# print(EvolutionPhonetique.evolution_phonetique("VÍVA"))         #vive 2
# print(EvolutionPhonetique.evolution_phonetique("BLÁWA"))         #bleve 2
# print(EvolutionPhonetique.evolution_phonetique("PAVỌR"))         #peour 2
# print(EvolutionPhonetique.evolution_phonetique("NÁVE"))         #nef 2
# print(EvolutionPhonetique.evolution_phonetique("VÍVIT"))         #vit 2
# print(EvolutionPhonetique.evolution_phonetique("CLÁVES"))         #cles 2
# print(EvolutionPhonetique.evolution_phonetique("MǪVET"))         #muet 2
# print(EvolutionPhonetique.evolution_phonetique("CLÁVOS"))         #clous 2
# print(EvolutionPhonetique.evolution_phonetique("CÁPRA"))         #chievre 2
# print(EvolutionPhonetique.evolution_phonetique("LÁBRA"))         #levre 2
# print(EvolutionPhonetique.evolution_phonetique("PÁTRE"))         #pere 2
# print(EvolutionPhonetique.evolution_phonetique("RỌPTA"))         #rote 2
# print(EvolutionPhonetique.evolution_phonetique("CÁPSA"))         #chasse 2
# print(EvolutionPhonetique.evolution_phonetique("SỌBTUS"))         #soz 2
# print(EvolutionPhonetique.evolution_phonetique("CÍVTE"))         #cit 2
# print(EvolutionPhonetique.evolution_phonetique("PÚTDA"))         #pute 2
# print(EvolutionPhonetique.evolution_phonetique("CÁNTAT"))         #chante 2
# print(EvolutionPhonetique.evolution_phonetique("QUẸ"))         #quei 2
# print(EvolutionPhonetique.evolution_phonetique("FĘSTA"))         #feste 2
# print(EvolutionPhonetique.evolution_phonetique("ÁPUD"))         #o 2
# print(EvolutionPhonetique.evolution_phonetique("CÁNTAS"))         #chantes 2
# print(EvolutionPhonetique.evolution_phonetique("SÁGMA"))         #some 2
# print(EvolutionPhonetique.evolution_phonetique("FÁCTA"))         #faite 2
# print(EvolutionPhonetique.evolution_phonetique("ĘXIT"))         #ist 2
# print(EvolutionPhonetique.evolution_phonetique("FRẸGDA"))         #freide 2
# print(EvolutionPhonetique.evolution_phonetique("SẸGNU"))         #seing 2
# print(EvolutionPhonetique.evolution_phonetique("LẸGNA"))         #leigne 2
# print(EvolutionPhonetique.evolution_phonetique("IÁM"))         #ja 2
# print(EvolutionPhonetique.evolution_phonetique("CỌMTE"))         #comte 2
# print(EvolutionPhonetique.evolution_phonetique("RỌMCE"))         #ronce 2
# print(EvolutionPhonetique.evolution_phonetique("NỌMEN"))         #nom 2
# print(EvolutionPhonetique.evolution_phonetique("MỌNTE"))         #mont 2
# print(EvolutionPhonetique.evolution_phonetique("GRÁNDE"))         #grant 2
# print(EvolutionPhonetique.evolution_phonetique("ỌNDA"))         #onde 2
# print(EvolutionPhonetique.evolution_phonetique("ÁNMA"))         #anme 2
# print(EvolutionPhonetique.evolution_phonetique("PỌNRE"))         #pondre 2
# print(EvolutionPhonetique.evolution_phonetique("SPÍNLA"))         #espingle 2
# print(EvolutionPhonetique.evolution_phonetique("VẸNĪ"))         #vin 2
# print(EvolutionPhonetique.evolution_phonetique("DỌMNA"))         #dame 2
# print(EvolutionPhonetique.evolution_phonetique("CǪRPUS"))         #cors 2
# print(EvolutionPhonetique.evolution_phonetique("PǪRTA"))         #porte 2
# print(EvolutionPhonetique.evolution_phonetique("VẸRDE"))         #vert 2
# print(EvolutionPhonetique.evolution_phonetique("MĘRCE"))         #merz 2
# print(EvolutionPhonetique.evolution_phonetique("LÁRGA"))         #large 2
# print(EvolutionPhonetique.evolution_phonetique("ÁRMA"))         #arme 2
# print(EvolutionPhonetique.evolution_phonetique("MĘRLA"))         #merle 2
# print(EvolutionPhonetique.evolution_phonetique("TÁLPA"))         #taupe 2
# print(EvolutionPhonetique.evolution_phonetique("CÁLDA"))         #chaude 2
# print(EvolutionPhonetique.evolution_phonetique("DỌLCE"))         #douz 2
# print(EvolutionPhonetique.evolution_phonetique("SÁLSA"))         #sausse 2
# print(EvolutionPhonetique.evolution_phonetique("SPỌSA"))         #espose 2
# print(EvolutionPhonetique.evolution_phonetique("MẸSE"))         #meis 2
# print(EvolutionPhonetique.evolution_phonetique("ÁLNA"))         #aune 2
# print(EvolutionPhonetique.evolution_phonetique("MǪLRE"))         #moldre 2
# print(EvolutionPhonetique.evolution_phonetique("CỌPPA"))         #cope 2
# print(EvolutionPhonetique.evolution_phonetique("HÁPPJA"))         #hache 2
# print(EvolutionPhonetique.evolution_phonetique("GỌTTA"))         #gote 2
# print(EvolutionPhonetique.evolution_phonetique("MẸTTRE"))         #metre 2
# print(EvolutionPhonetique.evolution_phonetique("LÁSSA"))         #lasse 2
# print(EvolutionPhonetique.evolution_phonetique("ĘSSRE"))         #estre 2
# print(EvolutionPhonetique.evolution_phonetique("BỌCCLA"))         #bocle 2
# print(EvolutionPhonetique.evolution_phonetique("SỌMMA"))         #some 2
# print(EvolutionPhonetique.evolution_phonetique("TĘRRA"))         #terre 2
# print(EvolutionPhonetique.evolution_phonetique("PẸNNA"))         #pene 2 #??
# print(EvolutionPhonetique.evolution_phonetique("SĘLLA"))         #sele 2
# print(EvolutionPhonetique.evolution_phonetique("VÁLLE"))         #val 2
# print(EvolutionPhonetique.evolution_phonetique("HǪRRDU"))         #ort 2
# print(EvolutionPhonetique.evolution_phonetique("CỌRRRE"))         #corre 2
# print(EvolutionPhonetique.evolution_phonetique("TǪLLRE"))         #toudre 2
# print(EvolutionPhonetique.evolution_phonetique("HǪSPTE"))    #oste 2
# print(EvolutionPhonetique.evolution_phonetique("HẸRPCE"))    #herce 2
# print(EvolutionPhonetique.evolution_phonetique("SǪLVRE"))    #soudre 2
# print(EvolutionPhonetique.evolution_phonetique("VǪLVTA"))    #voute 2
# print(EvolutionPhonetique.evolution_phonetique("PĘCTNE"))    #pigne 2
# print(EvolutionPhonetique.evolution_phonetique("TẸNDTA"))    #tente 2
# print(EvolutionPhonetique.evolution_phonetique("PĘRTCA"))    #perche 2
# print(EvolutionPhonetique.evolution_phonetique("PĘRDTA"))    #perte 2
# print(EvolutionPhonetique.evolution_phonetique("CRẸSCRE"))    #creistre 2
# print(EvolutionPhonetique.evolution_phonetique("PRINCPE"))    #prince 2
# print(EvolutionPhonetique.evolution_phonetique("SÁNCTA"))    #sainte 2
# print(EvolutionPhonetique.evolution_phonetique("PLÁNXI"))    #plains 2
# print(EvolutionPhonetique.evolution_phonetique("VẸNCRE"))    #veintre 2
# print(EvolutionPhonetique.evolution_phonetique("CÁRCRE"))    #chartre 2
# print(EvolutionPhonetique.evolution_phonetique("CỌLCTA"))    #coute 2
# print(EvolutionPhonetique.evolution_phonetique("PĘRSCA"))    #pesche 2
# print(EvolutionPhonetique.evolution_phonetique("HÁLSBERG"))    #hausberc 2
# print(EvolutionPhonetique.evolution_phonetique("SẸNIR"))    #seindre 2
# print(EvolutionPhonetique.evolution_phonetique("MĘLIR"))    #mieudre 2

# print(EvolutionPhonetique.evolution_phonetique("BÚTJRU"))         #burre 3
# print(EvolutionPhonetique.evolution_phonetique("SUÁVE"))        #soef 3
# print(EvolutionPhonetique.evolution_phonetique("AVẸA"))         #aveie
# print(EvolutionPhonetique.evolution_phonetique("ENTĘGRO"))      #entier
# print(EvolutionPhonetique.evolution_phonetique("COLǪBRA"))      #coluevre
# print(EvolutionPhonetique.evolution_phonetique("PALPĘTRA"))     #paupiere
# print(EvolutionPhonetique.evolution_phonetique("PARẸTE"))       #parei
# print(EvolutionPhonetique.evolution_phonetique("RECẸPET"))      #receit
# print(EvolutionPhonetique.evolution_phonetique("EMPLẸCAT"))     #empleie
# print(EvolutionPhonetique.evolution_phonetique("DESPLÁCET"))    #desplaist
# print(EvolutionPhonetique.evolution_phonetique("CONTĘNET"))     #contient
# print(EvolutionPhonetique.evolution_phonetique("PESÁRE"))       #peser
# print(EvolutionPhonetique.evolution_phonetique("TẸNWERONT"))    #tindrent
# print(EvolutionPhonetique.evolution_phonetique("YENWÁRYO"))     #janvier
# print(EvolutionPhonetique.evolution_phonetique("HÁBWERUNT"))    #ourent
# print(EvolutionPhonetique.evolution_phonetique("BÁTTWERE"))     #batre
# print(EvolutionPhonetique.evolution_phonetique("FILYǪLO"))      #filluel
# print(EvolutionPhonetique.evolution_phonetique("LENTYǪLO"))     #linçuel
# print(EvolutionPhonetique.evolution_phonetique("MOLYĘRE"))      #moilliere
# print(EvolutionPhonetique.evolution_phonetique("PRẸNDERE"))     #prendre
# print(EvolutionPhonetique.evolution_phonetique("ISCǪLA"))       #escole
# print(EvolutionPhonetique.evolution_phonetique("LAVÁRE"))       #laver
# print(EvolutionPhonetique.evolution_phonetique("AVẸRE"))        #aveir
# print(EvolutionPhonetique.evolution_phonetique("CÁVALLO"))      #cheval
# print(EvolutionPhonetique.evolution_phonetique("VILLANA"))      #vilaine
# print(EvolutionPhonetique.evolution_phonetique("FILÁRE"))       #filer
# print(EvolutionPhonetique.evolution_phonetique("FERMÁRE"))      #fermer
# print(EvolutionPhonetique.evolution_phonetique("MERCẸDE"))      #merci
# print(EvolutionPhonetique.evolution_phonetique("VEDẸRE"))       #veeir
# print(EvolutionPhonetique.evolution_phonetique("DEBẸRE"))       #deveir
# print(EvolutionPhonetique.evolution_phonetique("LEVÁRE"))       #lever
# print(EvolutionPhonetique.evolution_phonetique("ARGENTU"))      #argent
# print(EvolutionPhonetique.evolution_phonetique("ABẸRE"))        #aveir
# print(EvolutionPhonetique.evolution_phonetique("PORTÁRE"))      #porter
# print(EvolutionPhonetique.evolution_phonetique("PLORÁRE"))      #plorer
# print(EvolutionPhonetique.evolution_phonetique("NOTRÍRE"))      #norrir
# print(EvolutionPhonetique.evolution_phonetique("DURÁRE"))       #durer
# print(EvolutionPhonetique.evolution_phonetique("CRǪTULAT"))     #crolle
# print(EvolutionPhonetique.evolution_phonetique("DYỌRNO"))       #jor
# print(EvolutionPhonetique.evolution_phonetique("DYỌSSO"))       #jus
# print(EvolutionPhonetique.evolution_phonetique("LEỌNE"))        #leon
# print(EvolutionPhonetique.evolution_phonetique("CREÁRE"))       #creer
# print(EvolutionPhonetique.evolution_phonetique("KWÁGOLAT"))     #caille
# print(EvolutionPhonetique.evolution_phonetique("AỌRA"))         #ore
# print(EvolutionPhonetique.evolution_phonetique("LAÍCU"))        #lai
# print(EvolutionPhonetique.evolution_phonetique("LẸALE"))        #leal
# print(EvolutionPhonetique.evolution_phonetique("NEẸNTE"))       #nient
# print(EvolutionPhonetique.evolution_phonetique("VAÍNA"))        #gaine
# print(EvolutionPhonetique.evolution_phonetique("PAẸNSE"))       #pais
# print(EvolutionPhonetique.evolution_phonetique("BAÁRE"))        #baer
# print(EvolutionPhonetique.evolution_phonetique("PAỌRE"))        #paour
# print(EvolutionPhonetique.evolution_phonetique("AỌSTO"))        #aost
# print(EvolutionPhonetique.evolution_phonetique("AÚRO"))         #eur
# print(EvolutionPhonetique.evolution_phonetique("HAÚTU"))        #eu
# print(EvolutionPhonetique.evolution_phonetique("MAÚRU"))        #meur
# print(EvolutionPhonetique.evolution_phonetique("PLAÚTU"))       #pleu
# print(EvolutionPhonetique.evolution_phonetique("MOLTÚRA"))      #mouture
# print(EvolutionPhonetique.evolution_phonetique("AEÁTE"))        #ae
# print(EvolutionPhonetique.evolution_phonetique("PEỌNE"))        #pion
# print(EvolutionPhonetique.evolution_phonetique("THWAHLJA"))     #toaille
# print(EvolutionPhonetique.evolution_phonetique("PRÍNCIPE"))         #prince 3
# print(EvolutionPhonetique.evolution_phonetique("TĘPIDU"))           #tiede 3
# print(EvolutionPhonetique.evolution_phonetique("SÁPIDU"))           #sade 3
# print(EvolutionPhonetique.evolution_phonetique("DIXĘRUNT"))         #distrent 3
# print(EvolutionPhonetique.evolution_phonetique("HǪMINE"))           #ome 3
# print(EvolutionPhonetique.evolution_phonetique("RHǪDANU"))          #Rosne 3
# print(EvolutionPhonetique.evolution_phonetique("ÁSENU"))            #asne 3
# print(EvolutionPhonetique.evolution_phonetique("CÁSSANU"))          #chasne 3
# print(EvolutionPhonetique.evolution_phonetique("ǪRDINE"))           #ordre 3
# print(EvolutionPhonetique.evolution_phonetique("RỌBORE"))           #rouvre 3
# print(EvolutionPhonetique.evolution_phonetique("FỌLGERE"))          #foldre 3
# print(EvolutionPhonetique.evolution_phonetique("ÁNGELU"))           #ange 3
# print(EvolutionPhonetique.evolution_phonetique("FLẸBILE"))          #feible 3
# print(EvolutionPhonetique.evolution_phonetique("PǪPULU"))           #pueble 3
# print(EvolutionPhonetique.evolution_phonetique("SÁBIU"))            #saive 3
# print(EvolutionPhonetique.evolution_phonetique("FĘMITA"))   #fiente 3
# print(EvolutionPhonetique.evolution_phonetique("ÍNFANTE"))  #enfant 3
# print(EvolutionPhonetique.evolution_phonetique("FẸMNA"))   #feme 3
# print(EvolutionPhonetique.evolution_phonetique("DỌMNA"))   #dame 3
# print(EvolutionPhonetique.evolution_phonetique("PERDĘSTI"))     #perdies 3
# print(EvolutionPhonetique.evolution_phonetique("PǪTWI"))        #poi 3
# print(EvolutionPhonetique.evolution_phonetique("VǪLWI"))        #voil 3
# print(EvolutionPhonetique.evolution_phonetique("PERDĘI"))       #perdi 3
# print(EvolutionPhonetique.evolution_phonetique("LAĘI"))         #li 3
# print(EvolutionPhonetique.evolution_phonetique("PĘJOR"))        #pire 3
# print(EvolutionPhonetique.evolution_phonetique("MĘDJU"))        #mi 3
# print(EvolutionPhonetique.evolution_phonetique("TRǪJA"))        #truie 3
# print(EvolutionPhonetique.evolution_phonetique("PǪDJU"))        #pui 3
# print(EvolutionPhonetique.evolution_phonetique("PLǪWJA"))       #pluie 3
# print(EvolutionPhonetique.evolution_phonetique("MĘLJOR"))       #mieldre 3
# print(EvolutionPhonetique.evolution_phonetique("PǪSTJUS"))      #puis 3
# print(EvolutionPhonetique.evolution_phonetique("FǪLJA"))        #fueille 3
# print(EvolutionPhonetique.evolution_phonetique("CǪGNJTU"))      #cointe 3
# print(EvolutionPhonetique.evolution_phonetique("PRĘTJAT"))      #prise 3
# print(EvolutionPhonetique.evolution_phonetique("TĘRTJA"))       #tierce 3
# print(EvolutionPhonetique.evolution_phonetique("NĘPTJA"))       #niece 3
# print(EvolutionPhonetique.evolution_phonetique("PĘTTJA"))       #piece 3
# print(EvolutionPhonetique.evolution_phonetique("FǪRTJA"))       #force 3
# print(EvolutionPhonetique.evolution_phonetique("SCǪRTJA"))      #escorce 3
# print(EvolutionPhonetique.evolution_phonetique("NǪPTJAS"))      #noces 3
# print(EvolutionPhonetique.evolution_phonetique("CRǪCCJA"))      #croce 3
# print(EvolutionPhonetique.evolution_phonetique("SĘQWO"))        #siu 3
# print(EvolutionPhonetique.evolution_phonetique("ĘQWA"))         #ive 3
# print(EvolutionPhonetique.evolution_phonetique("VẸNWI"))        #vin 3
# print(EvolutionPhonetique.evolution_phonetique("VǪLWI"))        #voil 3
# print(EvolutionPhonetique.evolution_phonetique("PǪTWI"))        #poi 3
# print(EvolutionPhonetique.evolution_phonetique("HÁBWI"))        #oi 3
# print(EvolutionPhonetique.evolution_phonetique("DẸGITU"))       #dei 3
# print(EvolutionPhonetique.evolution_phonetique("CỌGITO"))       #cui 3
# print(EvolutionPhonetique.evolution_phonetique("FỌGIO"))        #fui 3
# print(EvolutionPhonetique.evolution_phonetique("CẸLIU"))        #cil 3
# print(EvolutionPhonetique.evolution_phonetique("ẸBRIU"))        #ivre 3
# print(EvolutionPhonetique.evolution_phonetique("ỌSTIU"))        #uis 3
# print(EvolutionPhonetique.evolution_phonetique("PỌTEU"))        #puis 3
# print(EvolutionPhonetique.evolution_phonetique("STĘTUI"))        #estui 3
# print(EvolutionPhonetique.evolution_phonetique("SĘQUIT"))        #siut 3
# print(EvolutionPhonetique.evolution_phonetique("NǪCUI"))        #nui 3
# print(EvolutionPhonetique.evolution_phonetique("PLACẸRE"))        #plaisir 3
# print(EvolutionPhonetique.evolution_phonetique("MERCẸDE"))        #merci 3
# print(EvolutionPhonetique.evolution_phonetique("PAGẸSE"))        #païs 3
# print(EvolutionPhonetique.evolution_phonetique("MERCÁTU"))        #marchie 3
# print(EvolutionPhonetique.evolution_phonetique("LAXÁRE"))        #laissier 3
# print(EvolutionPhonetique.evolution_phonetique("TRACTÁRE"))        #traitier 3
# print(EvolutionPhonetique.evolution_phonetique("CABÁLLU"))        #cheval 3
# print(EvolutionPhonetique.evolution_phonetique("GALÍNA"))        #geline 3
# print(EvolutionPhonetique.evolution_phonetique("DẸBUĪ"))        #dui 3
# print(EvolutionPhonetique.evolution_phonetique("MERCÁTU"))      #marchié 3
# print(EvolutionPhonetique.evolution_phonetique("GAUDÍRE"))      #joïr 3
# print(EvolutionPhonetique.evolution_phonetique("LÍNEU"))      #linge 3
# print(EvolutionPhonetique.evolution_phonetique("CẸREU"))      #cerge 3
# print(EvolutionPhonetique.evolution_phonetique("SERVÍRE"))         #servir 3
# print(EvolutionPhonetique.evolution_phonetique("VǪLUĪ"))         #volt 3
# print(EvolutionPhonetique.evolution_phonetique("VASTÁRE"))         #gaster 3
# print(EvolutionPhonetique.evolution_phonetique("VÍPRA"))         #guivre 3
# print(EvolutionPhonetique.evolution_phonetique("MĘLJOR"))         #mieldre 3
# print(EvolutionPhonetique.evolution_phonetique("PẸSILE"))         #peisle 3
# print(EvolutionPhonetique.evolution_phonetique("CÁRCRE"))         #chartre 3
# print(EvolutionPhonetique.evolution_phonetique("MỌLGRE"))         #moldre 3
# print(EvolutionPhonetique.evolution_phonetique("PLANCẸRE"))         #plaisir 3
# print(EvolutionPhonetique.evolution_phonetique("AMBLÁRE"))         #ambler 3
# print(EvolutionPhonetique.evolution_phonetique("SUFFLÁRE"))         #sofler 3
# print(EvolutionPhonetique.evolution_phonetique("MESCLÁRE"))         #mesler 3
# print(EvolutionPhonetique.evolution_phonetique("APǪSTLU"))         #apostre 3

# print(EvolutionPhonetique.evolution_phonetique("MERCẸDE"))      #merci 3
# print(EvolutionPhonetique.evolution_phonetique("ARGẸNTU"))      #argent 3
# print(EvolutionPhonetique.evolution_phonetique("CANTÁRE"))      #chanter 3
# print(EvolutionPhonetique.evolution_phonetique("MEMRÁRE"))         #membrer 3
# print(EvolutionPhonetique.evolution_phonetique("SIMLÁRE"))         #sembler 3
# print(EvolutionPhonetique.evolution_phonetique("PLÁNGRE"))         #plaindre 3
# print(EvolutionPhonetique.evolution_phonetique("VẸNCRE"))         #veintre 3
# print(EvolutionPhonetique.evolution_phonetique("SỌRGRE"))         #sordre 3
# print(EvolutionPhonetique.evolution_phonetique("OFFRÍRE"))         #ofrir 3
# print(EvolutionPhonetique.evolution_phonetique("INTRÁRE"))         #entrer 3
# print(EvolutionPhonetique.evolution_phonetique("SLÁITAN"))         #esclater 3
# print(EvolutionPhonetique.evolution_phonetique("DWỌDCĪ"))    #doze 2
# print(EvolutionPhonetique.evolution_phonetique("ỌNDCI"))         #onze 2
# print(EvolutionPhonetique.evolution_phonetique("DWỌDCĪ"))         #dotze 2
# print(EvolutionPhonetique.evolution_phonetique("QUÁNDO"))    #cant 3
# print(EvolutionPhonetique.evolution_phonetique("CORDWẸSE"))    #corveis 3
# print(EvolutionPhonetique.evolution_phonetique("PÁSQWA"))    #Pasque 2
# print(EvolutionPhonetique.evolution_phonetique("ỌNQWA"))    #onque 2
# print(EvolutionPhonetique.evolution_phonetique("LẸNGWA"))    #langue 2
# print(EvolutionPhonetique.evolution_phonetique("SỌÁVE"))    #souef 3
# print(EvolutionPhonetique.evolution_phonetique("ZELỌSU"))    #gelos 3
# print(EvolutionPhonetique.evolution_phonetique("ÁNCSJA"))    #ainse 3
# print(EvolutionPhonetique.evolution_phonetique("LANCEA"))    #lance 3
# print(EvolutionPhonetique.evolution_phonetique("ǪRDU"))    #orge 3
# print(EvolutionPhonetique.evolution_phonetique("ǪSTRA"))    #uistre 3
# print(EvolutionPhonetique.evolution_phonetique("ǪFFRJO"))    #ofre 3
# print(EvolutionPhonetique.evolution_phonetique("PTISÁNA"))    #tisane 3
# print(EvolutionPhonetique.evolution_phonetique("SMÁRÁGDA"))    #esmeraude 3
# print(EvolutionPhonetique.evolution_phonetique("SCRÍBRE"))    #escrivre 3
# print(EvolutionPhonetique.evolution_phonetique("CABÁLLU"))         #cheval 3
# print(EvolutionPhonetique.evolution_phonetique("ABÚTU"))         #eu 3
# print(EvolutionPhonetique.evolution_phonetique("PROBÁRE"))         #prover 3
# print(EvolutionPhonetique.evolution_phonetique("DẸBTU"))         #dete 3
# print(EvolutionPhonetique.evolution_phonetique("BẸBRE"))         #beivre 3
# print(EvolutionPhonetique.evolution_phonetique("FLẸBLE"))         #feible 3
# print(EvolutionPhonetique.evolution_phonetique("CAPẸLLU"))         #chevel 3
# print(EvolutionPhonetique.evolution_phonetique("SAPÚTU"))         #seu 3
# print(EvolutionPhonetique.evolution_phonetique("TROPÁRE"))         #trover 3
# print(EvolutionPhonetique.evolution_phonetique("SẸPE"))         #seif 2
# print(EvolutionPhonetique.evolution_phonetique("CÁNNPU"))         #chanvre 2
# print(EvolutionPhonetique.evolution_phonetique("SẸNAPI"))         #senv(r)e 3 #??
# print(EvolutionPhonetique.evolution_phonetique("TĘPJDU"))         #tiede 3
# print(EvolutionPhonetique.evolution_phonetique("PẸPRE"))         #peivre 3
# print(EvolutionPhonetique.evolution_phonetique("PǪPLU"))         #pueple 2
# print(EvolutionPhonetique.evolution_phonetique("PLACÍRE"))         #plaisir 3
# print(EvolutionPhonetique.evolution_phonetique("VECÍNU"))         #veisin 3
# print(EvolutionPhonetique.evolution_phonetique("ABWEMUS"))     #eumes
# print(EvolutionPhonetique.evolution_phonetique("FACEMUS"))         #faisons 3
# print(EvolutionPhonetique.evolution_phonetique("FÁGJMUS"))         #faimes 3
# print(EvolutionPhonetique.evolution_phonetique("AUCĘLLO"))         #oisel 3
# print(EvolutionPhonetique.evolution_phonetique("RỌMICE"))       #ronce 3
# print(EvolutionPhonetique.evolution_phonetique("PÚLICE"))         #pu(l)ce 3
# print(EvolutionPhonetique.evolution_phonetique("MỌCDU"))         #moide 2
# print(EvolutionPhonetique.evolution_phonetique("DĘCJMU"))         #disme 3
# print(EvolutionPhonetique.evolution_phonetique("CÍCJNU"))         #cisne 3
# print(EvolutionPhonetique.evolution_phonetique("FẸCERUNT"))         #fistrent 3
# print(EvolutionPhonetique.evolution_phonetique("DÍCERE"))         #dire 3
# print(EvolutionPhonetique.evolution_phonetique("GRÁCJLE"))         #graile 3
# print(EvolutionPhonetique.evolution_phonetique("MAGẸSTRU"))         #maistre 3
# print(EvolutionPhonetique.evolution_phonetique("REGÍNA"))         #reine 3
# print(EvolutionPhonetique.evolution_phonetique("PAGẸSE"))         #pais 3
# print(EvolutionPhonetique.evolution_phonetique("RẸGJDU"))         #reide 3
# print(EvolutionPhonetique.evolution_phonetique("FRÍGERE"))         #frire 3
# print(EvolutionPhonetique.evolution_phonetique("FRÁGJLE"))         #fraile 3
# print(EvolutionPhonetique.evolution_phonetique("FRÁXJNU"))          #fraisne 3
# print(EvolutionPhonetique.evolution_phonetique("NEGÁRE"))         #neiier 3
# print(EvolutionPhonetique.evolution_phonetique("ROGÁRE"))         #rover 3
# print(EvolutionPhonetique.evolution_phonetique("AMÍCA"))         #amie 3
# print(EvolutionPhonetique.evolution_phonetique("PRECÁRE"))         #preiier 3
# print(EvolutionPhonetique.evolution_phonetique("MÁNJCA"))         #manche 3
# print(EvolutionPhonetique.evolution_phonetique("GRÁNJCA"))         #granche 3
# print(EvolutionPhonetique.evolution_phonetique("PĘRTJCA"))         #perche 3
# print(EvolutionPhonetique.evolution_phonetique("LOCÁRE"))         #loer 3
# print(EvolutionPhonetique.evolution_phonetique("CARRÚCA"))         #charrue 3
# print(EvolutionPhonetique.evolution_phonetique("FAGỌNT"))         #font 2
# print(EvolutionPhonetique.evolution_phonetique("FAGỌ"))         #fou 2
# print(EvolutionPhonetique.evolution_phonetique("FRAGỌRE"))         #freour 3
# print(EvolutionPhonetique.evolution_phonetique("AGỌRU"))         #eur 3
# print(EvolutionPhonetique.evolution_phonetique("AGỌSTU"))         #aost 3
# print(EvolutionPhonetique.evolution_phonetique("FRAGRÁRE"))         #flairier 3
# print(EvolutionPhonetique.evolution_phonetique("IỌGU"))         #jou 3
# print(EvolutionPhonetique.evolution_phonetique("CASTÍGO"))         #chasti 3
# print(EvolutionPhonetique.evolution_phonetique("SECÚRU"))         #seur 3
# print(EvolutionPhonetique.evolution_phonetique("PLACÚTU"))         #pleu 3
# print(EvolutionPhonetique.evolution_phonetique("CUCÚLUS"))         #couls 3
# print(EvolutionPhonetique.evolution_phonetique("LUCỌRE"))         #luour 3
# print(EvolutionPhonetique.evolution_phonetique("AMÍCU"))         #ami 3
# print(EvolutionPhonetique.evolution_phonetique("CĘCU"))         #cieu 3
# print(EvolutionPhonetique.evolution_phonetique("SABÚCU"))         #seu 3
# print(EvolutionPhonetique.evolution_phonetique("MĘDCU"))         #mire 3 ??
# print(EvolutionPhonetique.evolution_phonetique("MỌNICU"))         #moine 3
# print(EvolutionPhonetique.evolution_phonetique("CLẸRCU"))         #clerc 3
# print(EvolutionPhonetique.evolution_phonetique("PǪRTCU"))         #porche 3
# print(EvolutionPhonetique.evolution_phonetique("CATẸNA"))         #chaeine #3
# print(EvolutionPhonetique.evolution_phonetique("POTẸRE"))         #poeir #3
# print(EvolutionPhonetique.evolution_phonetique("AMÁTUS"))         #amez #3
# print(EvolutionPhonetique.evolution_phonetique("CỌMTE"))         #comte #3
# print(EvolutionPhonetique.evolution_phonetique("MǪWTA"))         #muete #3
# print(EvolutionPhonetique.evolution_phonetique("FẸMTA"))         #fiente #3
# print(EvolutionPhonetique.evolution_phonetique("TẸNDTA"))         #tente #3
# print(EvolutionPhonetique.evolution_phonetique("DẸBTU"))         #dete #3
# print(EvolutionPhonetique.evolution_phonetique("CỌBTU"))         #cote #3
# print(EvolutionPhonetique.evolution_phonetique("VǪCTA"))         #vuide #3
# print(EvolutionPhonetique.evolution_phonetique("PÚTDA"))         #pute #3
# print(EvolutionPhonetique.evolution_phonetique("NẸTDA"))         #nete #3
# print(EvolutionPhonetique.evolution_phonetique("RẸTNA"))         #resne #3
# print(EvolutionPhonetique.evolution_phonetique("SPÁTLA"))         #espalle #3
# print(EvolutionPhonetique.evolution_phonetique("AUDÍRE"))         #oïr #3
# print(EvolutionPhonetique.evolution_phonetique("VEDẸRE"))         #veeir #3
# print(EvolutionPhonetique.evolution_phonetique("LAUDÁRE"))         #loer #3
# print(EvolutionPhonetique.evolution_phonetique("NẸTDO"))         #net #3
# print(EvolutionPhonetique.evolution_phonetique("SÁPDU"))         #sade #3
# print(EvolutionPhonetique.evolution_phonetique("RẸGDU"))         #reide #3
# print(EvolutionPhonetique.evolution_phonetique("PẸDTU"))         #pet #3
# print(EvolutionPhonetique.evolution_phonetique("SĘDCU"))         #siege #3
# print(EvolutionPhonetique.evolution_phonetique("BỌDNA"))         #bonne #3
# print(EvolutionPhonetique.evolution_phonetique("PẸDERE"))         #peire #3
# print(EvolutionPhonetique.evolution_phonetique("MǪDLU"))         #molle #3
# print(EvolutionPhonetique.evolution_phonetique("PROFỌNDUS"))         #parfons 3
# print(EvolutionPhonetique.evolution_phonetique("SCRǪFLAS"))         #escroeles 2
# print(EvolutionPhonetique.evolution_phonetique("DEFǪRUS"))         #deors 3
# print(EvolutionPhonetique.evolution_phonetique("PESÁRE"))         #peser 3
# print(EvolutionPhonetique.evolution_phonetique("DEFẸSU"))         #defeis 3
# print(EvolutionPhonetique.evolution_phonetique("PǪSTA"))         #poste 3
# print(EvolutionPhonetique.evolution_phonetique("ÁSNU"))         #asne 3
# print(EvolutionPhonetique.evolution_phonetique("ÍSLA"))         #isle 3
# print(EvolutionPhonetique.evolution_phonetique("CỌSRE"))         #cosdre 3
# print(EvolutionPhonetique.evolution_phonetique("LAVÁRE"))         #laver 3
# print(EvolutionPhonetique.evolution_phonetique("NOVĘLLU"))         #novel 3
# print(EvolutionPhonetique.evolution_phonetique("JỌWNE"))         #juene 3
# print(EvolutionPhonetique.evolution_phonetique("VÍVRE"))         #vivre 3
# print(EvolutionPhonetique.evolution_phonetique("APRÍLE"))         #avril 3
# print(EvolutionPhonetique.evolution_phonetique("LĘPRE"))         #lievre 3
# print(EvolutionPhonetique.evolution_phonetique("PẸPRE"))         #peivre 3
# print(EvolutionPhonetique.evolution_phonetique("BẸBRE"))         #beivre 3
# print(EvolutionPhonetique.evolution_phonetique("VÍVRE"))         #vivre 3
# print(EvolutionPhonetique.evolution_phonetique("FABREGA"))         #forge 3
# print(EvolutionPhonetique.evolution_phonetique("LATRỌNE"))         #larron 3
# print(EvolutionPhonetique.evolution_phonetique("RÁDRE"))         #rere 3
# print(EvolutionPhonetique.evolution_phonetique("CRẸDERE"))         #creire 3
# print(EvolutionPhonetique.evolution_phonetique("CǪCRE"))         #cuire 3
# print(EvolutionPhonetique.evolution_phonetique("CẸCRE"))         #ceire 3
# print(EvolutionPhonetique.evolution_phonetique("TRÁERE"))         #traire 3
# print(EvolutionPhonetique.evolution_phonetique("PǪPLU"))         #pueple 3
# print(EvolutionPhonetique.evolution_phonetique("ĘBLU"))         #ieble 3
# print(EvolutionPhonetique.evolution_phonetique("TABLA"))         #table 3
# print(EvolutionPhonetique.evolution_phonetique("VĘTLU"))         #vieil 3
# print(EvolutionPhonetique.evolution_phonetique("SĘTLA"))         #seille 3
# print(EvolutionPhonetique.evolution_phonetique("MỌDLU"))         #mole 2
# print(EvolutionPhonetique.evolution_phonetique("ǪCLU"))         #ueil 2
# print(EvolutionPhonetique.evolution_phonetique("HÁBWIT"))         #ot 2
# print(EvolutionPhonetique.evolution_phonetique("CRẸDWĪ"))         #crui 2
# print(EvolutionPhonetique.evolution_phonetique("STÚIT"))         #estut 2
# print(EvolutionPhonetique.evolution_phonetique("CRẸDWĪ"))         #crui 2
# print(EvolutionPhonetique.evolution_phonetique("ÁQWA"))         #eve 2
# print(EvolutionPhonetique.evolution_phonetique("ĘQWA"))         #ive 2
# print(EvolutionPhonetique.evolution_phonetique("SĘQWIT"))         #siut 2
# print(EvolutionPhonetique.evolution_phonetique("SĘQWO"))         #siu  2
# print(EvolutionPhonetique.evolution_phonetique("PLÁCWIT"))         #plot 2
# print(EvolutionPhonetique.evolution_phonetique("LẸGWĪ"))         #lui 2
# print(EvolutionPhonetique.evolution_phonetique("SẸPJA"))         #seche 3
# print(EvolutionPhonetique.evolution_phonetique("RABJA"))         #rage 3
# print(EvolutionPhonetique.evolution_phonetique("PLǪVJA"))         #pluie 3
# print(EvolutionPhonetique.evolution_phonetique("APJU"))         #ache 3
# print(EvolutionPhonetique.evolution_phonetique("SABJU"))         #sage 3
# print(EvolutionPhonetique.evolution_phonetique("ROBJU"))         #roge 3
# print(EvolutionPhonetique.evolution_phonetique("PRĘTJU"))         #pris 3
# print(EvolutionPhonetique.evolution_phonetique("PǪDJU"))         #pui 3
# print(EvolutionPhonetique.evolution_phonetique("MĘDJU"))         #mi 3
# print(EvolutionPhonetique.evolution_phonetique("FACJA"))         #face 3
# print(EvolutionPhonetique.evolution_phonetique("FACJO"))         #faz 3
# print(EvolutionPhonetique.evolution_phonetique("LAQJU"))         #laz 3
# print(EvolutionPhonetique.evolution_phonetique("CỌPRJU"))         #cuivre 3
# print(EvolutionPhonetique.evolution_phonetique("ǪPRJU"))         #uevre 3
# print(EvolutionPhonetique.evolution_phonetique("ẸBRJU"))         #ivre 3
# print(EvolutionPhonetique.evolution_phonetique("CAPTÍVU"))         #chaitif 3
# print(EvolutionPhonetique.evolution_phonetique("REPTÁRE"))         #reter 3
# print(EvolutionPhonetique.evolution_phonetique("DOBTÁRE"))         #doter 3
# print(EvolutionPhonetique.evolution_phonetique("SOBTÍLE"))         #sotil 3
# print(EvolutionPhonetique.evolution_phonetique("CIVTÁTE"))         #cité 3
# print(EvolutionPhonetique.evolution_phonetique("ADÁPTU"))         #aate 3
# print(EvolutionPhonetique.evolution_phonetique("ÁLIUD"))         #el 3
# print(EvolutionPhonetique.evolution_phonetique("CASTĘLLU"))         #chastel 3
# print(EvolutionPhonetique.evolution_phonetique("LAXÁRE"))         #laissier 3
# print(EvolutionPhonetique.evolution_phonetique("SMARÁGDA"))         #esmeraude 3
# print(EvolutionPhonetique.evolution_phonetique("AGNĘLLU"))         #aignel 3
# print(EvolutionPhonetique.evolution_phonetique("EXPLẸCTU"))         #espleit 3
# print(EvolutionPhonetique.evolution_phonetique("PIGMĘNTU"))         #piment 3
# print(EvolutionPhonetique.evolution_phonetique("VẸNCRE"))         #veintre 3
# print(EvolutionPhonetique.evolution_phonetique("MỌNICU"))         #moine 3
# print(EvolutionPhonetique.evolution_phonetique("MÁNJCA"))         #manche 3
# print(EvolutionPhonetique.evolution_phonetique("LENGWA"))         #langue 2
# print(EvolutionPhonetique.evolution_phonetique("PESÁRE"))         #peser 3
# print(EvolutionPhonetique.evolution_phonetique("COVĘNTU"))         #covent 3
# print(EvolutionPhonetique.evolution_phonetique("PENSÁRE"))         #penser 3
# print(EvolutionPhonetique.evolution_phonetique("INFĘRNU"))         #enfer 3
# print(EvolutionPhonetique.evolution_phonetique("MEMRÁRE"))         #membrer 3
# print(EvolutionPhonetique.evolution_phonetique("SIMLÁRE"))         #sembler 3
# print(EvolutionPhonetique.evolution_phonetique("SÍMJU"))         #singe 3
# print(EvolutionPhonetique.evolution_phonetique("LÍNJU"))         #linge 3
# print(EvolutionPhonetique.evolution_phonetique("SERVÍRE"))         #servir 3
# print(EvolutionPhonetique.evolution_phonetique("VERSÁRE"))         #verser 3
# print(EvolutionPhonetique.evolution_phonetique("CẸRJU"))         #cerge 3
# print(EvolutionPhonetique.evolution_phonetique("SALVÁRE"))         #sauver 3
# print(EvolutionPhonetique.evolution_phonetique("FALCONE"))         #faucon 3
# print(EvolutionPhonetique.evolution_phonetique("BỌLGRU"))         #bougre 3
# print(EvolutionPhonetique.evolution_phonetique("VǪLUĪ"))         #voil 3
# print(EvolutionPhonetique.evolution_phonetique("ǪLEU"))         #oile 3
# print(EvolutionPhonetique.evolution_phonetique("CLOPPCÁRE"))         #clochier 3
# print(EvolutionPhonetique.evolution_phonetique("SOFFLÁRE"))         #sofler 3
# print(EvolutionPhonetique.evolution_phonetique("ABBÁTE"))         #abe 3
# print(EvolutionPhonetique.evolution_phonetique("MÁTTIA"))         #mace 3
# print(EvolutionPhonetique.evolution_phonetique("CARRCÁRE"))         #chargier 3
# print(EvolutionPhonetique.evolution_phonetique("PĘJOR"))         #pire 3
# print(EvolutionPhonetique.evolution_phonetique("TENNTÍRE"))         #tentir 3
# print(EvolutionPhonetique.evolution_phonetique("COLLCÁRE"))         #couchier 3
# print(EvolutionPhonetique.evolution_phonetique("FUGTÍVU"))         #fuitif 3
# print(EvolutionPhonetique.evolution_phonetique("TEMPTÁRE"))    #tenter 3
# print(EvolutionPhonetique.evolution_phonetique("COMPTÁRE"))    #conter 3
# print(EvolutionPhonetique.evolution_phonetique("EXCARPSU"))    #eschars 3
# print(EvolutionPhonetique.evolution_phonetique("AMBDÚĪ"))    #andui 3
# print(EvolutionPhonetique.evolution_phonetique("PLOMBCÁRE"))    #plongier 3
# print(EvolutionPhonetique.evolution_phonetique("COCỌRBTA"))    #coorde 3
# print(EvolutionPhonetique.evolution_phonetique("ESTMÁRE"))    #esmer 3
# print(EvolutionPhonetique.evolution_phonetique("MASTCÁRE"))    #maschier 3
# print(EvolutionPhonetique.evolution_phonetique("MUNDBỌRO"))    #mainbor 3 #???
# print(EvolutionPhonetique.evolution_phonetique("ANTCĘSSOR"))    #ancestre 3
# print(EvolutionPhonetique.evolution_phonetique("STANTCÁRE"))    #estanchier 3
# print(EvolutionPhonetique.evolution_phonetique("MANDCÁRE"))    #mangier 3
# print(EvolutionPhonetique.evolution_phonetique("TARDCÁRE"))    #targier 3
# print(EvolutionPhonetique.evolution_phonetique("EPẸSCPU"))    #evesque 3
# print(EvolutionPhonetique.evolution_phonetique("LONGTÁNE"))    #lointain 3
# print(EvolutionPhonetique.evolution_phonetique("IỌXTA"))    #joste 3
# print(EvolutionPhonetique.evolution_phonetique("PRǪXIMU"))    #pruisme 3
# print(EvolutionPhonetique.evolution_phonetique("FRÁXINU"))    #fraisne 3
# print(EvolutionPhonetique.evolution_phonetique("DÍXERUNT"))    #distrent 3
# print(EvolutionPhonetique.evolution_phonetique("MONSTRÁRE"))    #mostrer 3
# print(EvolutionPhonetique.evolution_phonetique("VẸNURUNT"))    #vindrent 3
# print(EvolutionPhonetique.evolution_phonetique("MǪLRE"))         #mol|dre 3

def test():
    #Impotation du dictionnaire de tous les mots du texte
    # from dictionary import dict
    from dictionary_Mariale import dict_Marie
    keys = dict_Marie.keys()
    values = dict_Marie.values()
    # print(keys)
    # print(values)

    every_word = open('every_word.txt', 'w', encoding = 'utf-8')
    catch = open('catch.txt', 'w+', encoding = 'utf-8')
    dont_catch = open('dont_catch.txt', 'w+', encoding = 'utf-8')

    # print(len(dict_Marie))

    compteur = 0



    for key in keys:
        print_final = EvolutionPhonetique.evolution_phonetique(key)

        every_word.write('\n %s > %s \n \n' % (key, print_final) + '----------------------------------------- \n' )
        # print(key)
        # print(dict_Marie[key])
        # print(print_final)



        if print_final == dict_Marie[key]:
            catch.write('\n %s > %s == %s \n \n' % (key, print_final, dict_Marie[key]) + '----------------------------------------- \n')
        else:
            dont_catch.write(('\n %s > %s != %s \n \n' % (key, print_final, dict_Marie[key]) + '----------------------------------------- \n'))







test()



# while compteur < len(dict_Marie):
    # for key in keys:
        # compteur += 1
        # print(compteur)
        # print('--------------------------------------------')
        # print(key)
        # print_final = EvolutionPhonetique.evolution_phonetique(key)
        # print(value)
        # print(print_final)
        # final.write('%s > %s \n' % (key, print_final))
        # final.write('%s \n' % print_final)
        # return key
        # print(compteur)
