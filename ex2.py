from operator import add
from functools import reduce

def Passar_a_numero(llista):
    b=list(map(lambda x:str(x),llista))
    c=reduce(lambda x,y : x+y,b)
    print("La llista {} és el número {}".format(llista,c))

#ProgramaPrincipal
l=[3,7,4,1]
Passar_a_numero(l)


