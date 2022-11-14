from turtle import *
import random

#Screen().bgpic('images/tk3945.gif')
bgcolor('#69d7ff')  
color0 = ["red", "blue", "orange", "green", "black", "white", "purple", "pink", "grey", "yellow"] # liste couleurs
speed("fastest")

def tige(longueur, largeur): # fonction tige
    '''dessine la tige,  en creant un rectange avec un longueur et largeur aleatoire et un petit bout derriere pour faire realiste'''
    color('green')  # remplissage de la tige en vert
    begin_fill()
    
    start = random.randint(50, 180-50)
    left(start)  
    left(180)
    for i in range(2):  # boucle for pour faire le bout de la tige avant ruban
        forward(random.randint(25, 50))
        left(90)
        forward(largeur)
        if i == 0:
            left(90)
    backward(largeur)
    right(90)

    for i in range(2): # reste de la tige (rectangle)
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
    end_fill()

def flower_1():  # 1ere fleur
    '''1ere fleur'''
    color(random.choice(color0))
    begin_fill()
    size_circle = random.randint(20, 30)
    for i in range (8):  # boucle 8 fois une pétale
            for i in range(2): # dessin d'une pétale

                circle(size_circle, 90)
                left(90) 
            left(45) 
    end_fill()


def flower_2():  
    '''2e fleur'''
    begin_fill()
    pencolor(random.choice(color0))
    longueur = random.randint(50, 80)
    for i in range(5):  # étoile basique
        forward(longueur)
        left(144)  # 144 trouvé à taton
    end_fill()

def flower_3():  
    ''' 3eme fleur  ==>   inspiré de la fleur 3'''
    size_circle = random.randint(7, 12)
    pencolor('#7C909C') # couleur du crayon
    for n in range(4):
        if n == 0:
            continue # pour ne pas prendre trop de temps et passer et au tour n = 1
        
        for i in range (8):  
            for i in range(2): 
                pensize(2) 
                circle(n*size_circle, 90)
                left(90) 
            left(45) 
        pencolor(random.choice(color0)) 

def flower_4(longueur):
    '''3e fleur'''
    begin_fill()
    for i in range(5): 
        circle(longueur/25 ,180) 
        right(108)
    end_fill()
    color(random.choice(color0))

def ruban():  
    '''ruban '''
    color('black')
    begin_fill()
    backward(7)
    for i in range(2): # boucle pour rectangle
        forward(14)
        left(90)
        forward(3)
        left(90)
    end_fill() 
    up()
    forward(1000) # pour degager cette foutue tortue 
    goto(0, -100)
    #write("jules <3", font=('Arial', 20, 'normal'))
    down()


def draw_flower(): 
    '''fonction pour tout assembler : on creer un tige puis 1 des 5 dessins de fleur est choisi aleatoirement à l'aide de random.choice pour chaque tour '''
    longueur = random.randint(150, 300)   # genere aleatoirement la longueur des tiges
    tige(longueur, random.randint(1, 3))
    forward(longueur)
    number = random.randint(0, 2) 
    if number == 0:  
        flower_1()
    elif number == 1:
        flower_2()
    elif number == 2:
        flower_3()
    else:
        flower_4(longueur)
    up()
    home()  # retourne aux coordonnées (0;0)
    down()

while True:
    try:
        tour = int(input('Nombre de fleurs dans le bouquet : ')) # demande à l'utilisateur combien de fleurs dans le bouquet
        break
    except:
        print('Entre un nombre chef ')


for i in range(tour):
    draw_flower()
   
ruban()

while True: # boucle while infinie pour garder la fenetre ouverte
    forward(0)