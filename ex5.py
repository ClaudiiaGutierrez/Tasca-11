def crear_diccionari(llista):
    dic={}
    for i,e in enumerate(llista):
        dic[e]=i
    print("La llista {} hem creat el diccionari {}".format(llista,dic))


#Programa Principal
llista=["Cotxe", "Casa" "Vaixell", "Colom", "Ca", "Musol", "Clara"]
crear_diccionari(llista)