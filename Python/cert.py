def visitadas_por_cliente(nombre_archivo):
    diccionarioclientes = {}

    texto = open(nombre_archivo, "r")
    for cliente in texto:
        cliente = cliente.strip().split(":")
        #['2018', 'Andrea Godoy', 'Venecia,New York']
        if cliente[1] not in diccionarioclientes:
            diccionarioclientes[cliente[1]] = []
        for lugares in cliente[2].strip().split(","):
            diccionarioclientes[cliente[1]].append([cliente[0], lugares])
    
    archivofinal = open("Visitadas_por_cliente.txt", "w")

    for cliente in diccionarioclientes: #es un iterable lo de cliente, entonces no importa que lo tome 2 veces siempre y cuando no lo ocupe en otra parte xd
        viajes = diccionarioclientes[cliente]
        

        #bubble sort

        n = len(viajes)

        for a in range(n-1):
            for o in range (0, n - a - 1):
                if viajes[o][0]> viajes[o+1][0]:
                    viajes[o], viajes[o+1] = viajes[o+1], viajes[o]
                if viajes[o][0] == viajes[o+1][0]:
                    if viajes[o][1] > viajes[o+1][1]:
                        viajes[o], viajes[o+1] = viajes[o+1], viajes[o]


        archivofinal.write(f"{cliente}:\n")
        for viaje in viajes:
            año, ciudad = viaje[0], viaje[1]
            archivofinal.write(f"{año} - {ciudad}\n")
        archivofinal.write("\n")
    archivofinal.close()
    return len(diccionarioclientes)




visitadas_por_cliente("viajes.txt")