#Tarea hasta guia 6
#Primera parte
catalgo = [["The Office",2005,2013,9,770815,["Comedia"]],
["Breaking Bad",2008,2013,9.5,2314919,["Crimen", "Drama", "Suspenso"]],
["Band of Brothers",2001,2001,9.4,559518,["Acción", "Drama", "Histórica"]],
["Game of Thrones",2011,2019,9.2,2422280,["Acción","Aventura","Drama"]],
["The Simpsons",1989,"NA",8.6,451961,["Animación", "Comedia"]],
["The Sopranos",1999,2007,9.2,520737,["Crimen", "Drama"]],
["Attack on Titan",2013,2023,9.1,602664,["Acción", "Aventura", "Animación"]],
["Chernobyl",2019,2019,9.3,943168,["Drama", "Histórica", "Suspenso"]],
["Friends",1994,2004,8.9,1140227,["Comedia", "Romance"]],
["Lost",2004,2010,8.3,638100,["Aventura", "Drama", "Fantasía"]],
["Dark",2017,2020,8.7,488096,["Crimen", "Drama", "Misterio"]],
["Sherlock",2010,2017,9.1,1044777,["Crimen", "Drama", "Misterio"]],
["31 minutos",2002,2014,9.1,1710,["Comedia", "Familiar", "Fantasía"]],
["Stranger Things",2016,2025,8.6,1435806,["Drama", "Fantasía", "Terror"]],
["Narcos",2015,2017,8.7,498592,["Biográfica", "Crimen", "Drama"]],
["The Mandalorian",2019,"NA",8.6,621020,["Acción", "Aventura", "Fantasía"]],
["House of Cards",2013,2018,8.6,545828,["Drama"]]]

def generos_mejor_calificados(series):
    generos = []

    for serie in series:
        rating = serie[-3]
        lista_generos = serie[-1]
        for g in lista_generos:
            g = g.strip()
            indice = -1
            for i in range(len(generos)):
                if generos[i][0] == g:
                    indice = i
                    break

            if indice == -1:
                generos.append([g, [rating]])

            else:
                generos[indice][1].append(rating)

    borrador = []
    for par in generos:
        genero = par[0]
        valores = par[1]
        nota = 0
        for v in valores:
            nota = nota + v
        promedio = nota / len(valores)
        borrador.append([promedio, genero])


    for i in range(len(borrador)):
        for j in range(0,len(borrador) - i -1):
            if borrador[j][0] < borrador[j + 1][0]:
                borrador[j], borrador[j + 1] = borrador[j + 1], borrador[j]

    #print(borrador)
    final = []
    for g in borrador:
        final.append(g[1])
    retorno = final[:5]
    return retorno
entrada = catalgo
print(generos_mejor_calificados(entrada))

#segunda parte
def recomendar_series(series, año, lista_generos):
    retorno = []
    for lista_series in series:
        iniciodelaserie = lista_series[1]
        emisionfinaldelaserie = lista_series[2]

        if iniciodelaserie <= año and (emisionfinaldelaserie == "NA" or emisionfinaldelaserie >= año):
            if lista_generos == []:
                retorno.append([lista_series[0], lista_series[5], lista_series[3], lista_series[4]])
            else:
                contador = 0

                while contador < len(lista_series[5]):
                    if lista_generos[5][contador] in lista_generos:
                        retorno.append([lista_series[0], lista_series[5], lista_series[3], lista_series[4]])
    
    for repeticiones in range(len(retorno)):
        for doblerepeticion in range(0, len(retorno) - repeticiones - 1):
            calificacion = retorno[doblerepeticion][2]
            calificacion2 = retorno[doblerepeticion+1][2]
            if calificacion < calificacion2:
                retorno[doblerepeticion], retorno[doblerepeticion+1] = retorno[doblerepeticion+1], retorno[doblerepeticion]
            
            if calificacion == calificacion2:
                reseñacaso1 = retorno[doblerepeticion][3]
                reseñacaso2 = retorno[doblerepeticion+1][3]
                if reseñacaso1 < reseñacaso2:
                    retorno[doblerepeticion], retorno[doblerepeticion+1] = retorno[doblerepeticion+1], retorno[doblerepeticion]


    retornofinal = []
    for limpiar in retorno:
        retornofinal.append([limpiar[0], limpiar[1]])
    return retornofinal

sseries = catalgo
print(recomendar_series(sseries, 2010,[]))