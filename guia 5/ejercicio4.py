def analisis_texto(texto): #funcion
    #variables locales
    repeticiones=int(0)
    sin_punto=str("")
    letra_t="t"
    solo_t=int(0)
    solo_t_total=int(0)
    solo_t_porcentaje=float(0.0)
    palabra_anterior=int(0)
    cantidad_mayor_anterior=int(-1)
    letra_c="c"
    pares_y_c=int(0)


    #Validación para que se introduzca un texto terminado en un punto
    while not(texto.endswith(".")):
        print("Ese texto no es valido.")
        texto=input("Por favor, termine con un punto: ")
    sin_punto=texto[:-1].lower()

    for palabra in sin_punto.split():
        repeticiones+=1

        for letra in palabra:                              # (a)
            if letra.lower()==letra_t: solo_t+=1           #
        if solo_t==1: solo_t_total+=1                 # (a) y (d)
        solo_t=0 

        if repeticiones==1 or len(palabra)>palabra_anterior:   #
            cantidad_mayor_anterior+=1                         # (b)
        palabra_anterior=len(palabra)                          #

        if (palabra.startswith("c") or palabra.startswith("C")) and len(palabra)%2==0: pares_y_c+=1  # (c)

    solo_t_porcentaje=(solo_t_total*100)/repeticiones # (d)
    print("\n---------------------------------------------------------------------------------------")
    print(f"La cantidad de palabras que solamente aparece una unica vez la letra t es de {solo_t_total}.")
    print(f"Estas suponen un {round(solo_t_porcentaje, 2)}% sobre las {repeticiones} palabras introducidas.")
    print(f"La cantidad de palabras cuya cantidad de letras es mayor a su predecesora es de {cantidad_mayor_anterior}.")
    print(f"La cantidad de palabras con la cantidad de letras pares y comienzan con la letra 'c' es de {pares_y_c}.")

analisis_texto(input("Introduzca un texto (debe estar terminado por un punto): "))