import re
import collections

def read_file():

    x_file = open('text_inter.txt', 'w+')

    #Tentative d'ouverture du fichier
    try:
        #Ouvre et lit le fichier texte
        with open('Texte_J.txt', 'r') as file:
            numLines = 0
            numWords = 0
            numChars = 0

            #Suppression de la ponctuation et des retours à la ligne
            for line in file:
                # print(line)

                for char in ":;-.,_\n\t":
                    line = line.replace(char, ' ')
                    line = line.lower()

                for char in "'":
                    line = line.replace(char, ' ')

                # for char in " ":
                    # line = line.replace(char, '\n')

                for char in "1234567890":
                    line = line.replace(char, '')


                x_file.write(line)

                # print(line)


                all_lines = "".join(line)


                # print(line)
                # print(all_lines)

                """
                # TEST
                # Il me faut transformer chaque line en une string entière (bien chercher), ensuite, ça ira mieux, tout sera faisaible, il faudra ensuite faire un dictionnaire avec ça
                words = all_lines.split()
                word_counts = collections.Counter(words)
                for word, count in sorted(word_counts.items()):
                    print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
                """

                #Liste des mots
                wordList = line.split()

                #Enlever les tableaux de la liste (mais, ça revient a même que d'avoir le texte...)
                # wrodlList_noMore = ' '.join(wordList)

                # print(wrodlList_noMore)

                #Nombre de lignes
                numLines += 1

                #Nombre de mots
                numWords += len(wordList)

                #Nombre de caractères
                numChars += len(line)

                # convert_file(line)
                #Différents prints
                # print(wordList)
                # print(line)
                # print(file)


        print('Lines: %d\nWords: %d\nCharacters: %d' % (numLines, numWords, numChars))
        # print(line)



    except IOError:
        print("Couldn't open file.")
        return



# def convert_file(file):
#     try:
#         with open('dico_mots.txt', "w+") as newFile:
#             #Création d'un nouveau fichier texte
#             # newFile = open('dico_mots.txt', "w+")
#
#             for words in file:
#                 newFile.write(''.join(line))
#
#     except IOError:
#         print("Couldn't open file.")
#         return


    """
    En gros, je dois ensuite ouvrir la x_file pour jsutement pourovir la lire et tout voir en une string.
    #Tentative d'ouverture du fichier
    try:
        #Ouvre et lit le fichier texte
        with open('text_inter.txt', 'r') as file:

            for x in file:
                print(x)

    except IOError:
        print("Couldn't open file.")
        return
    """


read_file()

"""
Maintenant, je dois remplacer chaque espace par un /n
"""
