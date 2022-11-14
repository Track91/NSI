# Créé par alowczyk, le 12/09/2022 en Python 3.7
import statistics
"""
number = 99
while number >= 2:
    for i in range(number):
        print('{} bottles of beer on the wall, {} bottles of beer.'.format(number, number))
        number-= 1
        print('Take one down and pass it around, {} bottles of beer on the wall.'.format(number))
print("1 of beer on the wall, 1 bottles of beer.")
print('Take one down and pass it around, no more bottles of beer on the wall.')
print('No more bottles of beer on the wall, no more bottles of beer. ')
print('Go to the store and buy some more, 99 bottles of beer on the wall.') """
'''
number = 1
result = 0
for i in range(100):
    result+=number
    number+=1

print(result)

n = int(input('entrez le nombre: '))
result = math.factorial(n)
print(result)
'''
n = int(input("Combien de notes : "))
notes = []
for i in range(n):
    note = int(input('Entre la note: '))
    notes.append(note)
print(statistics.mean(notes))