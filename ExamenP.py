"Ex1"
def menu():
    op=0
    while op <0 >14:
        print("""
            Programador Principal
            1.Estructures condicionals,if
            2.Estructures condicionals, match
            3.Estructures iteratives, for e in b
            4.Estructures iteratives, for i in range(x)
            5.Estructures interatives, for i,e in enumerate(a)
            6.Funció amb paràmetres
            7.Funció lambda
            8.Funció list comprehesion
            9.Funció map
            10.Funció zip
            11.Funció filtrer
            12.Classes i Objectes
            13.Fitxers
            14.Sortir
            """)
    op = int(input("Introdueix una opció: "))
    if op<1 >14:
     print("Opció no vàlida,  torni a elegir una opció \n")
    else: 
        return(op)


"Ex2"
#Programa principal
op = 0
while a!=14:
    op=menu
    match(op):
        case 1:
            ex1()
        case 2:
            ex2()
        case 3:
            ex3()
        case 4:
            ex4()
        case 5:
            ex5()
        case 6:
            l=["hola","adeu","hello","bye","alt","baix"]
            c="a"
            ex6(l,c)
        case 7:
            ex7()
        case 8:
            ex8()
        case 9:
            ex9()
        case 10:
            ex10()
        case 11:
            ex11()
        case 12:
            ex12
        case 13:
            ex13()
        case 14:
            print("Prograama acabat, que ho passi molt bé i gràcies per utilizar-me!")
            




"Ex3"
def ex1():
    a = int(input("Introdueix el primer nombre: "))
    b = int(input("Introdueix el segon nombre: "))
    if a>b:
        print("{} és major que {}".format(a,b))
    if b<a:
        print("{} és major que {}".format(b,a))
    else:
        print("{} i {} són igual")

    


"Ex4"
def ex2():
    vocal = int(input("Introduix en una vocal: ")(a,e,i,o,u))
    match(vocal):
        case 'a':
            print("La vocal introduïda és una a")
        case 'e':
            print("La vocal introduïda és una e")
        case 'i':
            print("La vocal introduïda és una i")
        case 'o':
            print("La vocal introduïda és una o")
        case 'u':
            print("La vocal introduïda és una u")
        case other:
            print("Opció no vàlida!")

"Ex5"
def ex3():
    a = []
    b = []
    for i in range(3):
        a.append(input("Introodueix la paraula: "))
    for e in a:
        b.append(len(e))
print("Les longituds de la lista {} són {}".format(a,b))


"Ex6"
def ex4():
    for e in range(1, 10, 2):
        print(i)

"Ex7"
def ex5():
    a = [1, 2, 3, 4, 5]
    d = {}
for i,e in enumerate():
    print()


"Ex 8"
def ex6(l,c):
    b = []
    for e in l:
        if c in e:
            b.append(c,e)
    print("De la llista {}".format(l,b,c))

"Ex9"
def ex7():
    a = [3, 4, 6, 8, 9]
    b = list(map(lambda x:x+10,a))
    print(b)

"Ex10"
def ex8():
    a = [3, 4, 6, 8, 9]
    b = [e**2]

"Ex 11"
def ex9():
    a = ("Piano","Bateria", "Clarinete", "Saxo", "Saxo", "Cello")
    b = list(map(lambda x:x[::-1],a))
    print(b)




"Ex 12"
def ex10():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    c = list(zip(a,b))
    print (c)


"Ex 13"
def ex11():
    a = [1, 2, 3, 4, 5]
    b = list(filter(lambda x: x%2==1,a))
    print(b)

"Ex14"
class Ordinador():
    def __init__(self, tipus, pantalla):
        self.tipus=tipus
        self.pantalla=pantalla
    

def gettipus(self):
    print("Retorna self.tipus")

def getpantalla(self):
    print("Retorna self.pantalla")


"Ex 15"
class Portatil():
    def __init_(self,tipus,pantalla):
        self.tipus="portatil"
        self.pantalla="Té 15"

def gettipus(self):
    print("És un portatil".format)

def getpantalla(self):
    print("La pantalla es de 15".format())


"Ex16"
class Tablet():
    def __init__(self,tipus,pantalla):
        self.tipus()
        self.pantalla()
def gettipus(self):
    print("Es un tablet".format)

def getpantalla(self):
    print("La pantalla es de 15".format)
"Ex17"
class Servidor():
    def __init__(self,tipus,pantalla):
        self.tipus()
        self.pantalla()
def gettipus(self):
    print("Es un servidor".format)

def getpantalla(self):
    print("La pantalla es de 25 pulgades".format)

"Ex 18"
class PC():
    def __init__(self,tipus,pantalla):
        self.tipus()
        self.pantalla()
def gettipus(self):
    print("Es un PC")
def getPantalal(self)_
    print("Te 27 pulgades")

"Ex19"
def ex12():
    a = [Portatil(),Tablet(),Servidor(),PC()]
    for e in a:
        e.getTipus()
        e.getPantalla()
    

"Ex 20"
def ex13():
    with open("/home/cicles/AO/ex20.txt", "w") as f:
        for i in range(10):
            f.write(i+"/n")
    with open("/home/cicles/AO/ex20.txt", "w") as f: 
        for i in f:
            print(i) 