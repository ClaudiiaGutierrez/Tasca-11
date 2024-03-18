def div(a,b):
    try:
        c= a/b
        print("La divisió de {} entre {} és {}".format(a,b,c))
    except ZeroDivisionError:
        print("El segon paràmetre de la funció no pot ser Zero")

#Programa Principal
a = int(input("Escriure el numerador: "))
b = int(input("Escriure el denominador: "))
div(a,b)