texto=str("")
primletra=str("")
ultletra=str("")
vocales=("a","e","i","o","u")
igual=int(0)
palvocal=int(0)
total=int(0)
porc=float(0.0)

print("""Introduzca el texto:
(Este debe terminar en punto, y ser separado solo por espacios en blanco.)""")
texto=str(input("   >"))
while texto.endswith(".")==False: #solo deja continuar si el texto termina con un "."
    texto=str(input("El texto DEBE terminar con un punto y solo separarse por espacios en blanco: ")).lower()

texto=texto[0: len(texto)-1]
for palabra in texto.split(): 
    primletra=palabra[0] #guardo la primer letra
    if primletra==ultletra: #si la primer letra es igual a la anterior, se suma uno
        igual=igual+1
    ultletra=palabra[len(palabra)-1] #guardo la ultima letra
    if primletra in vocales and ultletra in vocales: #si ambas letras son vocales, se suma un contador
        palvocal=palvocal+1
    total=total+1 #contador para contar el total de las palabras

print(f"El total de palabras ingresadas es de: {total}")
print(f"\nLa cantidad total de palabras que comienzan y terminan con vocal son: {palvocal}")
porc=round(palvocal*100/total, 2) #calculo el porcentaje de las palabras que cumplen la condición
print(f"Estas suponen un {porc}% sobre el total.")
print(f"\nLa cantidad de palabras que comienzan con la letra de la palabra anterior son: {igual}")