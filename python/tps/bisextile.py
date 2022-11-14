

def est_bisexuelle(a):
    if a %4 == 0 and a % 100 != 0:
        
        return 0
    else:
        
        return 1
    
a = int(input("Entrez l'année: "))

est_bisexuelle(a)

if est_bisexuelle(a) == 0:
    print('cette année contient 366 jours')
else:
    print('cette année contient 365 jours'