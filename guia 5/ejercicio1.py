sin_punto=str("")
lista=list()
lista=[]

def txt(texto):
    while not(texto.endswith(".")):
        print("Ese texto no es valido.")
        texto=input("Por favor, termine con un punto: ")
    sin_punto=texto[:-1]
    return sin_punto

def palabras():
    for palabra in sin_punto.split():
        if palabra.endswith(","):
            palabra=palabra[:-1]
            lista.append(palabra)
        else:
            lista.append(palabra)
    return lista

txt(input("Introduzca un texto, debe terminar con un punto: "))
palabras()
print(lista)