def txt(texto):
    repeticiones=int(0)
    sin_punto=str("")
    digitos=int(0)
    tres_letras=int(0)
    seis_letras=int(0)
    mas_de_seis=int(0)
    palabra_larga=str("")
    de_totales=int(0)

    while not(texto.endswith(".")):
        print("Ese texto no es valido.")
        texto=input("Por favor, termine con un punto: ")
    sin_punto=texto[:-1].lower()

    for palabra in sin_punto.split():
        repeticiones+=1
        if not palabra.isalpha(): digitos+=1 #a) cuántas palabras tenían al menos un caracter que era en realidad un dígito
        if len(palabra)<=3: tres_letras+=1  #b) cuántas palabras tenían 3 o menos letras
        if len(palabra)>=4 and len(palabra)<=6: seis_letras+=1  #b) cuántas tenían 4 y hasta 6 letras
        if len(palabra)>6: mas_de_seis+=1  #b)cuántas tenían más de 6 letras
        if repeticiones==1 or len(palabra)>len(palabra_larga): palabra_larga=palabra #c) Determinar la longitud de la palabra más larga
        if (palabra.find("de")<len(palabra)/2) and (palabra.find("de")!=-1): de_totales+=1 #d) cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra
    
    print("----------------------------------------------------------------------------------------------------")
    print(f"\nCantidad de palabras que tenían al menos un caracter como digito: {digitos}")
    print(f"Cantidad de palabras con 3 o menos letras: {tres_letras}")
    print(f"Cantidad de palabras con entre 4 y 6 letras: {seis_letras}")
    print(f"Cantidad de palabras con más de 6 letras: {mas_de_seis}")
    print(f"Longitud de la palabra mas larga ({palabra_larga}: {len(palabra_larga)} letras)")
    print(f"Cantidad de palabras contuvieron la expresión 'de' en la primera mitad de la palabra: {de_totales}")


txt(input("Introduzca un texto, debe estar terminado por un punto ('.'): "))