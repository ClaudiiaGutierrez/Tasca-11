def lenp(frase):
    r = frase.split(" ")
    l = list(map(len, r))
    print("La longitud de cada paraula de la frase {} és {}".format(frase,l))



#Pprincipal
frase = input("Escriure una frase: ")
lenp(frase)