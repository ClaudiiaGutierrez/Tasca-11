def adjuntar(l,d,c):
    a = []
    for i in range(len(l)):
        a.append(l[i]+c+d[i])
        print("La unio de les lliestes {} i {} és {}".format(l,d,a))
#Programa Principal
l=["Super", "Hiper","Mini", "Maxi"]
d=["Women", "bole", "Mouse", "Boom" ]
adjuntar(l,d,"-")

