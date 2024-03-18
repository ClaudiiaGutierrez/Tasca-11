def imprimir_fitxer(m):
    a = []
    with open (m,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def afegir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.writelines(e+"\n")
        
#Programa Principal
fitxer = "/home/cicles/AO/Tasca-11/ex11.txt"
imprimir_fitxer(fitxer)
llista = ["Jordi", "Claudia", "David", "Ayoub", "Oscar", "Paula", "Sebas", "Anas"]
afegir_fitxer(fitxer,llista)
imprimir_fitxer(fitxer)