import re
import collections

# d = {'key':'value'}
# d['mynewkey'] = 'mynewvalue'
# d['mynewemptykey'] = ''
#
# print(d)

s = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
#
# word = r'/\b(\w+)\b/g'
#
# match = re.search(word, s)
#
# if match:
#     process(match)


words = s.split()

#Création d'un dictionnaire pour avoir en tête les mots déjà utilisés
# counts = {}
# for word in words:
#     if word not in counts:
#         counts[word] = 0
#     counts[word] += 1

#Dictionnaire dans lequel la ke est le mot et la value est le nombre
# counts = collections.defaultdict(int)
# for word in words:
#     counts[word] += 1

word_counts = collections.Counter(words)
for word, count in sorted(word_counts.items()):
    print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
