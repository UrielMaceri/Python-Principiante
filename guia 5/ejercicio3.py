def analisis_texto(texto): #funcion
    #variables locales
    repeticiones=int(0)
    sin_punto=str("")
    palabra_mas_larga=int(0)
    vocales=("e", "i", "o", "u")
    resto_vocales=int(0)
    solo_a=int(0)
    solo_a_porcentaje=float(0.0)

    #Validación para que se introduzca un texto terminado en un punto
    while not(texto.endswith(".")):
        print("Ese texto no es valido.")
        texto=input("Por favor, termine con un punto: ")
    sin_punto=texto[:-1].lower()

    for palabra in sin_punto.split():
        repeticiones+=1

        if repeticiones==1 or len(palabra)>len(palabra_mas_larga): palabra_mas_larga=palabra # (a)

        for letra in palabra:                              #
            if letra.lower() in vocales: resto_vocales+=1  # (b)
        if resto_vocales==0: solo_a+=1                     #
        resto_vocales=0

    solo_a_porcentaje=(solo_a*100)/repeticiones # (c)
    print("\n-------------------------------------------------------------------------------")
    print(f"La longitud de la palabra mas larga ({palabra_mas_larga}) es de {len(palabra_mas_larga)} letras.")
    print(f"La cantidad de palabras que tienen como unica vocal a la letra a es {solo_a}.")
    print(f"Las cuales representan un {round(solo_a_porcentaje, 2)}% de las {repeticiones} palabras ingresadas.")
    print("-------------------------------------------------------------------------------")

analisis_texto(input("Introduzca un texto (debe finalizar por un punto): "))