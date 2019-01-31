import re
import collections

def read_one_string_file():

    liste = open('liste.txt', 'w+')

    #Tentative d'ouverture du fichier
    try:
        #Ouvre et lit le fichier texte
        with open('text_inter.txt', 'r') as file:

            #Suppression de la ponctuation et des retours à la ligne
            for line in file:
                # print(line)

                words = line.split()
                word_counts = collections.Counter(words)
                for word, count in sorted(word_counts.items()):
                    # print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))

                    liste.write(' %s %d \n' % (word, count))

    except IOError:
        print("Couldn't open file.")
        return


read_one_string_file()
