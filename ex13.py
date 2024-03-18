class Animal():
    def __init__(self, atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar():
        pass
    def mourem():
        pass
    def quisco():
        print("Soc un animal")

class Cavall(Animal):
    def xerrar():
        print("Iíííííí")
    def mourem():
        print("Em moc a trot")
    def quisco():
        print("Soc un Cavall")
    

class Dofi(Animal):
    def xerrar(self):
        print("IchIchIchI")
    def mourem(self):
        print("Em moc nadant")
    def quisco(self):
        print("Soc un Dofí")

class Abella(Animal):
    def xerrar(self):
        print("sssssssss")
    def mourem(self):
        print("Em moc volant")
    def quisco(self):
        print("Soc una Abella")
    def picar(self):
        print("Si m'enprenyes et picaré!")
    
class Huma(Animal):
    def __init__(self, nom, atribut, edat,):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        print("Hola! Nosaltres utilitzem un idioma per xerrar")
    def mourem(self):
        print("Em moc caminant")
    def quisco(self):
        print("Soc un Humá")
   
    
class Centaure(Huma, Cavall):
    def xerrar(self):
        print("Hola! Nosaltres utilitzem un idioma per xerrar")
    def mourem(self):
        print("Em moc a trot")
    def quisco(self):
        print("Soc un Centaure")

class Fiet(Huma):
    def __init__(self, nom, atribut, edat, llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares
    def xerrar(self):
        print("Ueeeeueee")
    def mourem(self):
        print("Em moc a gatetjant")
    def quisco(self):
        print("Soc un Fiet")
    def nompares(self):
        for e in self.pares:
            print(e.nom)

class xou():
    def xerrar(self):
        print("xou")
    def mourem(self):
        print("Em moc fent xou")
    def quisco(self):
        print("Soc un xou")


#Programa Principal


a = [Cavall("Marró", "4"), Dofi("Gris","10"),Abella("Nefre i groga", "0,5"),Huma("Sibília", "Cristià","7"), Centaure("Fiona", "Marró", "18"), Fiet("Jordi","Moreno", "9",["Fiona","Marc"]),xou()]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()