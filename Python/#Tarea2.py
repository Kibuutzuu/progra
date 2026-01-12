#Tarea2
def mas_visitadas(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    memoria = archivo.readlines()
    archivo.close()
    dic = {}
    lista_a_ordenar = []
    for lineas in memoria:
        dato = lineas.strip().split(":")
        año = dato[0]
        persona = dato[1]
        ciudades = dato[2]
        lista_ciudades = ciudades.split(",")
        for ciudad in lista_ciudades:
            
            if ciudad not in dic:
                dic[ciudad] = 0
            dic[ciudad]+=1
    for llave, valor in dic.items():
        lista_a_ordenar.append((valor,llave))
    
    lista_ordenada = sorted(lista_a_ordenar, reverse=True)
    lista_ordenada = lista_ordenada[:3]
    nombre = "mas_visitadas.txt"
    most = open(nombre, "w")
    for contador,city in lista_ordenada:
        formato = f"Se visito {contador} veces {city}\n"
        most.write(formato)
    most.close()
    return len(dic)
print(mas_visitadas("viajes.txt"))