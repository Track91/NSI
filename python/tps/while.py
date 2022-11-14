# 2
import math
import random

def ex1():
    nombre = int(input('Entrez le nombre: '))
    maxi = []
    tour = 0
    while nombre!=1:
        tour+=1
        if nombre%2 == 0:
            nombre /= 2
        else:
            nombre = nombre*3 +1
        print(nombre)
        maxi.append(nombre)
    print("Le maximum est ", max(maxi))
    print('Il a fallu ', tour, ' tours.')


def digramme(a, b, t):

    for i in range(len(t)):
        if a == t[i] and b == t[i+1]:
            return True


def sous_mot(a, b, t):
    c =0
    for i in range(len(t)):
        if a == t[i]:
            c+=1
        elif b == t[i] and c>=1:
            return True

def sous_mot_tab(tab1, tab2):
    if sorted(tab1) == tab2:
        return True



def exjsp():
    number = random.randint(0, 1000)
    a = 0
    i=0
    while True:
        i+=1
        a = int(input('Entrez le nombre : '))
        if a > number:
            print("C'est plus petit ")
        elif a < number:
            print("C'est plus grand")
        else:
            print('trouvé en ', i, ' essais')
            break

def game():
    nb_allumettes = 21
    while True:
        print(f'il y a {nb_allumettes} allumettes ')
        try:
            a = int(input('Combien en prenez-vous ?: '))
        except:
            print('Entrez un chiffre ')
            a = 9
        b = random.randint(1, 3)
        
        if not a in [1, 2, 3]:
            print('Entrez un nombre compris entre 1 et 3')
            a = 0
            b = 0
        nb_allumettes -= a
        if b > nb_allumettes and b >1:
            b = 1
        
        if nb_allumettes <= 0:
            print('Vous avez perdu')
            break
        if b != 0:
            print('Je prend ' + str(b) + " allumettes ")
        
        nb_allumettes -= b
        if nb_allumettes <=0:
            print('Vous avez gagné')
            break

def game_init():
    while True:
        
        a = input('rejouer ? (oui/non): ')
        if a == 'oui':
            game()
        else:
            break


def plus_grande_sequence(e, tab):
    tour = 0
    occurence = 0
    max = 0
    while tour < len(tab):

        if e == tab[tour]:
            
            if tab[tour-1] != e:
                occurence = 1
            else:              
                occurence +=1
            if occurence > max:
                max = occurence

        tour +=1
       
    return max


def pgs(tab):
    max = 0   
    for e in tab:
        if plus_grande_sequence(e, tab) > max:
            max = plus_grande_sequence(e, tab)
            a = e

    return (f"{a} est l'élément avec la plus grande séquence d'occurence consécutive qui s'élève au nombre de {max}")


exjsp()
print(pgs([0, 1, 1, 1, 4, 1, 1, 1, 1, ]))