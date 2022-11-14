# Créé par bilalhaddou, le 07/09/2022 en Python 3.7
from turtle import*
from random import*
nb=0
nb_occurence=0
def occurences(t,v):
    for i in range(len(t)):
        nb=t(i)
        if nb==v:
            nb_occurence=nb_occurence+1
        print(nb_occurence)




