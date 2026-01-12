#C 2020 C2
#   estudiante1;estudiante2;estudiante3

#   Andrea Campos;Andrea Campos;Pedro Vasquez



def obtener_representante(nombre_archivo):
    d = {}
    archivo = open(nombre_archivo, "r")

    for linea in archivo: #Recorre la linea
        
        dato = linea.strip().split(";")
        #print(dato)
        for voto in dato: #Recorre la lista de la linea ['Andrea Campos', 'Andrea Campos', 'Pedro Vasquez']
            voto = voto.upper()
            #estudiante = voto.split(";")
            
            #print(estudiante)
            
            
            #print(voto)
            cont = 0
            bool verificador = True;
            if voto not in d: #Si el candidato no esta registrado, Crea el candidato una vez en d
                d[voto] = 0
                d[voto] += 1
                verificador = False
            if verificador:
                d[voto] += 1
            

            
    return d
print(obtener_representante('votos.txt'))
