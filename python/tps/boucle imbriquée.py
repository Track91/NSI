def motif1(n):
    for i in range(n+1):
        for j in range(i):
            print("*", end='')
        print('')

def motif2(n):
    for i in range(n+1):
        for j in range(n-i):
            print("*", end='')
        print('')


def motif3(n):
    for i in range(n+1):
        for j in range(n-i):
            pass

motif3(6)