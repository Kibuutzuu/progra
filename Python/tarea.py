ancho = int(input("Ingrese el ancho del terreno (m): ")) ##datos requeridos por la guia
largo = int(input("Ingrese el largo del terreno (m): "))
lado = int(input("Ingrese el lado de cada sembradio (m): "))

if lado <= ancho and lado <= largo:
     sembradios = lado * lado ##calculos requeridos por guía, no explicitamente pero si implicitamente
     terreno_total = ancho * largo
     n_sembradios = int(terreno_total / sembradios)
     print(f"Se plantarán {n_sembradios} sembradios de {lado} x {lado} m.")##prints para no hacerlos después
     print(f"El total sembrado será de {sembradios*n_sembradios} m2") ##sembradios * n_sembradios es el total que se plantará
     print(f"El sobrante no sembrado en el terreno será de {terreno_total-(sembradios*n_sembradios)} m2") ##se le resta al terreno total para saber lo que no se va a poder plantar
     if n_sembradios <= 200: ##condicionales por tabla, sirve de igual manera si el ultimo elif es solo un else, ya que es decir "si no pasa nada de esto, entonces es esto"
        montototal = (4*350 + 1*450 + 3 * 1400) * n_sembradios * sembradios
     elif 200 < n_sembradios and n_sembradios <= 400:
        montototal = (4*300 + 1*350 + 3 * 1200) * n_sembradios * sembradios
     elif 400 < n_sembradios and n_sembradios <= 1000:
        montototal = (4*250 + 1*250 + 3 * 1000) * n_sembradios * sembradios
     elif n_sembradios > 1000:
        montototal = (4*200 + 1*150 + 3 * 800) * n_sembradios * sembradios
     subsidio = int(sembradios*n_sembradios/10000) * float(15) ##está adaptado para que dé con .0 solamente, en el ejemplo de 200x100 de lado 99 da 1.9 y eso termina dando un numero erroneo, adapté la fórmula solamente con el int.
     print(f"El costo de los sensores será: M$ {round(montototal/1000000,2)}") ##monto redondeado y dividido para que de en M con 2 decimales, lo pidió la guía
     print(f"El subsidio del gobierno será: M$ {subsidio}") ##el subsidio eran 15 M cada 10000, por eso la fórmula está arriba, para no hacer largo el código
     print(f"Costo total de la plantación: M$ {round(round(montototal/1000000,2) - subsidio, 2)}") ##ahora al total se le resta el subsidio y se redondea, eso solamente, es optimizable pero si funciona no se toca 
else:
    print("Error: No hay solucion posible.") ##si no se cumple la condicion de que los lados deben ser más pequeños que el ancho ***Y*** el largo, se imprime esto, ya que si pusieramos "O" (or) sólo consideraría cumplir con 1 de los 2 requisitos

    ##los condicionales están en ese orden para no repetir código, si se hubiera hecho al revés se habría tenido que crear más código para encapsular casos completos, de esta forma se evita entrar en elifs ocasionales ya que si no hace estrictamente esto, te bota el mensaje directamente
