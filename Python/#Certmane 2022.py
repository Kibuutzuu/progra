#Certmane 2022

#   fecha,equipo1,goles_equipo1,equipo2,goles_equipo2

#   1872-11-30,Scotland,0,England,0

#   aaaa-mm-dd

def desempeño_anual(nombre_archivo, equipo, año):
        #   equipo-año.txt
        #   Chile-2010.txt
        #   ordenados por fecha
        #   2010-01-20 contra Panama, Victoria: 2 a 1
    archivo = open(nombre_archivo, "r", encoding="UTF-8")
    d = {}
    for linea in archivo:
        dato = linea.strip().split(",")
        fecha = dato[0]
        equipo1 = dato[1]
        gol1 = int(dato[2])
        equipo2 = dato[3]
        gol2 = int(dato[4])
        year = fecha.split("-")
        y = int(year[0])
        vic = "Victoria"
        der = "Derrota"
        draw = "Empate"
        #print(y)
        #print(dato)
        if y == año:
            if equipo1 == equipo or equipo2 == equipo:
                if equipo not in d:
                    d[equipo] = []
                if equipo1 == equipo:
                    favor = gol1
                    contra = gol2
                    rival = equipo2
                    
                    if gol1 == gol2:
                        resultado = draw
                    elif gol1 >= gol2:
                        resultado = vic
                    
                    elif gol1 <= gol2:
                        resultado = der
                    
                    else:
                        continue
                    formato = (f"{fecha} contra {rival}, {resultado}: {favor} a {contra}")
                    d[equipo].append(formato)
                    #d[equipo].append((fecha,equipo2,resultado,favor,contra))
                if equipo2 == equipo:
                    favor = gol2
                    contra = gol1
                    rival = equipo1
                    
                    if gol2 == gol1:
                        resultado = draw
                    elif gol2 >= gol1:
                        resultado = vic
                    
                    elif gol2 <= gol1:
                        resultado = der
                    
                    else:
                        continue
                    formato = (f"{fecha} contra {rival}, {resultado}: {favor} a {contra}")
                    d[equipo].append(formato)
                    #d[equipo].append((fecha,equipo1,resultado,favor,contra))
    formato = f"{equipo}-{año}.txt"
    archivo_salida = open(formato, "w")
    for llave in d[equipo]:
        
        
        #print(llave)
        
        archivo_salida.write(f"{llave}\n")
    archivo_salida.close()

    archivo.close()



    # cantidad de partidos encontrados
    return len(d[equipo])
print(desempeño_anual('resultados.txt', 'Chile', 2010)) # 15

def partidos_por_rival(nombre_archivo, equipo):

    archivo = open(nombre_archivo, "r", encoding="UTF-8")
    d = {}
    for linea in archivo:
        dato = linea.strip().split(",")
        fecha = dato[0]
        equipo1 = dato[1]
        gol1 = int(dato[2])
        equipo2 = dato[3]
        gol2 = int(dato[4])
        year = fecha.split("-")
        y = int(year[0])

        if equipo == equipo1:
            if equipo2 not in d:
                d[equipo2] = 0
            d[equipo2] += 1
                
        if equipo == equipo2:
            if equipo1 not in d:
                d[equipo1] = 0
            d[equipo1] += 1
    #aux = []
    #sort = sorted
    formato = f"rivales-{equipo}.txt"
    archivo_salida = open(formato, "w")   
    for llave, dato in d.items():
        #print(f"{llave}: {dato}")
        archivo_salida.write(f"{llave}: {dato}\n")
        #aux.append(())
    archivo_salida.close()
    #return len(aux)
    return len(d)
#contador de veces jugados contra paisa para chile
print(partidos_por_rival('resultados.txt', 'Chile'))

