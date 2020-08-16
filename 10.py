"""

2 milyonun altındaki bütün asalların toplamını bul

"""

def asalMi(x):

    for a in range(2,x):

        if x % a == 0:
            return False

    return True

LIMIT = 2000000
SONKOK = 1414

liste = list(range(2,LIMIT))

for a in range(2,SONKOK + 1):

    if asalMi(a):

        for x in range(len(liste)):

            if liste[x] % a == 0 and asalMi(liste[x]) == False:

                # print('del', x, ' =>', a)
                liste[x] = 0


        print(a,'bitti diğer asala geçiliyor')
    
print(sum(liste))
