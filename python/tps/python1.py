# 1)

'''
import turtle

longueur = int(input('Entrez la longueur: '))
largeur = int(input('Entrez la largeur: '))
aire = longueur * largeur
print("L'aire est de", aire)

turtle.forward(longueur)
turtle.left(90)
turtle.forward(largeur)
turtle.left(90)
turtle.forward(longueur)
turtle.left(90)
turtle.forward(largeur)'''

# 2)
"""
secondes = int(input('Entrez le nombre de secondes: '))
heure = secondes//3600
secondes -= heure*3600
minute = secondes//60
secondes -= minute*60
seconde = secondes
print("{}:{}:{}".format(heure, minute, seconde))"""

# 3)
import turtle
'''for i in range(6):
    turtle.forward(100)
    turtle.left(180-108)
'''
'''
turtle.left(35)
for i in range(5):
    turtle.forward(100)
    turtle.left(180-36)
'''

'''
turtle.left(60)
turtle.forward(100)
turtle.up()
turtle.left(180-60)
turtle.forward(40)
turtle.down()

'''

colors = ['red', 'orange', 'yellow', 'green' ,'blue' ,'indigo', 'purple', 'white']
turtle.speed(0)
x=0
turtle.right(90)
for i in colors:
    x += 20
    turtle.up()
    turtle.color(i)
    turtle.left(90)
    turtle.forward(2*(200-x)-20)
    turtle.left(90)
    turtle.begin_fill()
    turtle.down()
    turtle.circle(180-x, 180)
    turtle.end_fill()
turtle.forward(10000000)


