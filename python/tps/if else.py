
# if elif else
# exercice 2

age1 = int(input('Rentrez le premier age : '))
age2 = int(input('Rentrez le second age : '))

if age1 > age2:
    diff = age1 - age2
    print("La differeance d'age est ", diff, 'ans.')
elif age1 == age2:
    print('Ils ont le meme age')
else:
    print("La difference d'age est ", age2 - age1 , "ans.")

number = 0
while number < 101:
    number += 1
    if number % 3 == 0:
        print('fizz')
    elif number % 5 ==0:
        print('buzz')
    elif number % (5*3) ==0:
        print('fizzbuzz')
    else:
        print(number)

from random import randint
points = 0
tour = 0
while tour < 10:
    tour+=1
    dé1 = randint(0, 6)
    dé2 = randint(0, 6)
    result = dé1 + dé2
    if result >= 10:
        print('regle speciale')
        points += 25
    else:
        points += dé1*dé2
    print(points)

print('le joueur a gagné', points, 'points en 10 rounds.')


import random
rules = {0 :"pierre", 1 :"feuille", 2 :'ciseau'}

while True:
    ordi = random.randint(0, 2)

    user = int(input('Entrez votre nombre (0 pour pierre, 1 pour feuille, 2 pour ciseau) : '))
    print("L'ordinateur a chosie", rules[ordi], ".")

    if user == 0 and ordi == 1:
        print("L'ordinateur gagne")
    elif user == 1 and ordi == 2:
        print("L'ordinateur gagne")
    elif user == 2 and ordi == 0:
        print("L'ordinateur gagne")
    elif user == 1 and ordi == 0:
        print("Le joueur gagne")
    elif user == 2 and ordi == 1:
        print("Le joueur gagne")
    elif user == 0 and ordi == 2:
        print("Le joueur gagne")
    elif user == ordi:
        print('egalité')
    else:
        print("Entrez un nombre valide")

    rejouer = input('Rejouer ? (oui/non): ')
    if rejouer == 'oui':
        continue
    else:
        break

