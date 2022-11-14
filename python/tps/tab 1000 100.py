from random import*
nb_occurenceA=0
nb_occurenceZ=0
nb_occurenceB=0
tab=1000*[0]
for i in range(len(tab)):
    nbtab=randint(1,10)
    tab[i]=nbtab
print(tab)
for i in range(len(tab)):
    if tab[i]==10:
        nb_occurenceZ=nb_occurenceZ+1
    if tab[i]==1:
        nb_occurenceA=nb_occurenceA+1
    if tab[i]==2:
        nb_occurenceB=nb_occurenceB+1

print(nb_occurenceA,nb_occurenceZ,nb_occurenceB)




