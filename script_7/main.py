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

def test():

    #Impotation du dictionnaire de tous les mots du texte
    from dictionary import dict
    keys = dict.keys()
    # print(keys)

    final = open('final.txt', 'w', encoding = 'utf-8')

    for key in keys:
        print('--------------------------------------------')
        print(key)
        print(EvolutionPhonetique.evolution_phonetique(key))
        print_final = EvolutionPhonetique.evolution_phonetique(key)
        # final.write('%s %s \n' % (key.encode("utf-8"), print_final))
        final.write('%s > %s \n' % (key, print_final))
        # final.write('%s \n' % print_final)


test()
