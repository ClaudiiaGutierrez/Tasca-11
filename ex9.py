def pot(p):
    r = [x**p for x in range(1,10)]
    print("Les potencias elevades a {} dels 10 primers números és {}".format(r,p))

#Programa Principal
p= int(input("Introdueixi un número al qual voleu elevar la resta: "))
pot(p)