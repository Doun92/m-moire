def create_dictionary():
        dictionary = open('dictionary.txt', 'w+')
        dict = {

        }

        #Tentative d'ouverture du fichier
        try:
            #Ouvre et lit le fichier texte
            with open('liste.txt', 'r') as file:
                for line in file:
                    # print(line)

                    for char in "\n":
                        line = line.replace(char, '')

                    print("Entrez l'étymon latin du terme suivant : " + line )
                    x = input()

                    dict.update( {x : line})

                    # print(line)
                    print(dict)
                    dictionary.write(str(dict))

        except IOError:
            print("Couldn't open file.")
            return

create_dictionary()
