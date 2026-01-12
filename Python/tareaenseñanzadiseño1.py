series=[["The Office",2005,2013,9,770815,["Comedia"]],
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

# Pregunta 1
def generos_mejor_calificados(lista):
   #aviso que esto lo estoy programando en telefono, por si llegas a ver algo rarito o asi, es que mi pc murio masomenos por la pantalla, en la semana trato de comprarme otra XD
   generoslista = []
   sumaparadespuessacarpromedio = [] #esto va a hacer una lista con ceros para igualar con la lista de generos, cada cero le corresponde a un genero (basicamente van a estar ligados)
   contadorvecesqueserepite = [] #aqui lo mismo
   contadorwhile = 0 #al final este no lo ocupé porque la idea del while era más larga, pero, se entiende y lo dejo acá para que se vea que intenté de otras formas xD
   #pd, al final, si lo voy a ocupar más adelante, me di cuenta recien pero igual dejo el mensaje de arriba porque filo

   for series in lista: #esto va a ir recorriendo la lista valor por valor dentro de la lista, como los valores son otras listas, recorreré listas dentro de las listas
      genero = series[5] #con esto solo nos fijamos en los generos
      for generos in genero: #los revisamos ya que todos los valores dentro de los generos son una lista
         if generos not in generoslista: #en caso que no este el genero en la lista vacia de generos, se agrega
            generoslista.append(generos)
            sumaparadespuessacarpromedio.append (series[3])
            contadorvecesqueserepite.append(1)
         else:
            dondeesta = generoslista.index(generos)
            sumaparadespuessacarpromedio[dondeesta] += series[3]
            contadorvecesqueserepite[dondeesta] += 1
   promedio = []
   while contadorwhile < len(sumaparadespuessacarpromedio):
      calculo = sumaparadespuessacarpromedio[contadorwhile] / contadorvecesqueserepite[contadorwhile]
      promedio.append(round(calculo, 2))
      contadorwhile += 1

   #recapitulando, en generoslista tengo todos los generos sin repetir, en sumaparadespuessacarpromedio tengo la suma de todas las valoraciones
   #y en contadorvecesqueserepite tengo la cantidad de veces que sale un genero, dividi la suma con la cantidad de veces que se repetia un genero ya que
   #necesitaba el promedio normal, pero, redondee a 2 decimales ya que si no lo hago salen numeros muy largos pero si lo hago con 1 decimal me devuelve valores
   #parecidos que puede interferir con el calculo, ej, crimen se redondeaba a 9.1 pero familiar ya tenia 9.1 entonces quedaban como iguales
   #aunque en verdad crimen tenia un valor de 9.04, lo que hace incierta la medicion

   #ahora voy a juntar cada genero con su promedio, ya después de eso ordeno las cosas porque si las ordeno asi solamente me va a quedar todo disparejo xD

   contador2 = 0
   generosconpromedio = []
   while contador2 < len(generoslista):
      generosconpromedio.append([generoslista[contador2], promedio[contador2]])
      contador2 += 1

   numero = len(generosconpromedio) #va a funcionar de iterable en mi bubble sort, tuve que buscarlo en youtube porque uno del 702 dijo que
   #lo mencionaron en clases y a nosotros no entonces igual lo busqué para ocuparlo, sino no se me ocurre como hacerlo solo

   for veces in range(numero): #osea, va a ejecutarse el numero de veces que tenga la variable numero, pero, a su vez numero tiene el valor del largo de la lista
      for o in range( 0, numero - veces - 1): #o es el indice actual que estoy comparando, pero, no se me ocurre un nombre asi que le di letra al azar
         #0,numero-veces-1 va a ir reduciendo el final de la lista para que no se repita infinitamente este parametro
         if generosconpromedio[o][1] < generosconpromedio[o+1][1]: #si quisiera la lista de menor a mayor el signo seria al reves
            generosconpromedio[o], generosconpromedio[o+1] = generosconpromedio[o+1], generosconpromedio[o] #esto va a intercambiar las posiciones de la lista
   
   #ahora por ultimo voy a quitar las valoraciones y le hago return

   generosordenados = []

   for generosfinal in generosconpromedio:
      generosordenados.append([generosfinal[0]])

   #lista de prints por si quieres probar uno por uno los resultados que da la funcion para ejecutarse
   #print (generoslista)
   #print (sumaparadespuessacarpromedio)
   #print (contadorvecesqueserepite)
   #print(promedio)
   #print(generosconpromedio)
   #print(generosordenados)
   return generosordenados[:5]

print("P1:")
print(generos_mejor_calificados(series))

# Pregunta 2
def recomendar_series(lista, año, lista_generos):
   listavacia = [] #para guardar la lista nueva
   for series in lista: #esto va a ir indice por indice para indicarme cada serie
      #este desglose es netamente para informacion de la lista, asi no subo a verla de nuevo a cada rato
      ini = series[1]
      fin = series[2]
      calificacion = series [3]
      cantidadreseñas = series [4]
      genero = series[5]
      if ini <= año and (fin == "NA" or fin >= año): #aqui veo si es del mismo año, antes o despues de ese año, ya que me sirve las que toquen el año puesto
         if lista_generos == []:
            listavacia.append([series[0], genero, series[3], series[4]]) #si la lista está vacía, no me interesa filtrar por genero y guardo la calificacion y la cantidad de reseñas para ordenar despues
         else:
            flag = False #esta flag solamente va a tener la funcion de dar paso o no a un if que voy a explicar más adelante y no me gustan las flag pero es que no puedo ocupar break xD
            contador = 0 #para el while
            while contador < len(genero):
               if genero[contador] in lista_generos:
                  flag = True #abajito explico por que la flaaaggg
               contador += 1
            if flag:
               listavacia.append([series[0], genero, series[3], series[4]])
            #la flag era para darle paso a este if, que, si encontraba en una serie con más de una categoria la categoria que nosotros necesitabamos
            #la iba a agregar a la lista, en caso contrario, simplemente va a pasar de largo y series va a cambiar su valor dependiendo de la lista
   numero = len(listavacia) #voy a volver a hacer el bubble sort entonces no creo que sea necesario explicar esto, solo voy a comparar más cosas (calificacion y numero de votos)

   for veces in range(numero):
      for a in range(0, numero - veces - 1):
         calificacion1 = listavacia[a][2]
         calificacion2 = listavacia[a+1][2]
         if calificacion1 < calificacion2:
            listavacia[a], listavacia[a+1] = listavacia[a+1], listavacia[a]
         reseñas1 = listavacia[a][3]
         reseñas2 = listavacia[a+1][3]
         if calificacion1 == calificacion2:
            if reseñas1 < reseñas2:
               listavacia[a], listavacia[a+1] = listavacia[a+1], listavacia[a]
   listafinal = []
   for depurar in listavacia:#depurar porque elimina elementos solamente, este for cumple solo la funcion de añadir a la listafinal el nombre y genero
      listafinal.append([depurar[0], depurar[1]])

   return listafinal #retorna la lista modificada

#consideraciones: ocupo range porque se implementó en la guia rapida de listas, no como range solamente pero al decir list(range(a)) me doy a entender que si podemos ocuparlo.
#el código se puede optimizar muchisimo más, pero, se comprenderá que el entorno en el que lo hice no es el más óptimo
#para referencias como el bubble sort busque material externo, pero, ocupe cosas que si están dentro de los limites hasta la unidad 6
# link de la biblioteca de python del bubble sort (el video no lo tengo): https://ellibrodepython.com/bubble-sort

print("P2:")
print(recomendar_series(series,2017,["Drama"]))
print(recomendar_series(series,2020,["Animación"]))
print(recomendar_series(series,2010,[]))
print(recomendar_series(series,2022,["Fantasía","Animación"]))
print(recomendar_series(series,2024,["Biográfica"]))
