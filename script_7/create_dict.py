def create_dictionary():
        dictionary = open('dictionary_Mariale_T.py', 'w+', encoding = 'utf-8')

        #Tentative d'ouverture du fichier
        try:
            #Ouvre et lit le fichier texte
            with open('liste_Mariale.txt', 'r') as file:
                dictionary.write('dict = { \n')
                for line in file:
                    # print(line)


                    for char in "\n":
                        line = line.replace(char, '')


                        test = line.strip()
                        # print(line)

                        dictionary.write('" " : "%s",\n' % test)

                dictionary.write('}')
        except IOError:
            print("Couldn't open file.")
            return

create_dictionary()
