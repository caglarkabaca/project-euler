"""

akare + b kare = c kare

a + b + c = 1000

a + b + a kare + b kare = 1000

a ( 1 + a ) + b ( 1 + b ) = 1000

===
a < b < c
a kare + b kare = c kare
a + b + c = 1000

c min 501
b min 2
a min 1

"""

for c in range(1,1000):

    for b in range(1,1000):

        a = 1000 - b - c 

        if a < 0:
            break

        if a**2 + b**2 == c**2:

            if a < b and b < c:
                print(a*b*c)


"""

"""