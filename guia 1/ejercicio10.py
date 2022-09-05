#decalracion de variables
cant=int
suma=int
cero=0
uno=1

#se introduce la cantidad de digitos a mostrar
cant=int(input("Intoduzaca la cantidad de numeros de la secuencia de fibonacci a mostrar: "))

#susecion de fibonnacci
print("Mostrando ", cant, " valores de la secuencia.")
suma=0
for x in range (cant):
    print(suma)
    cero=uno  #"cero" toma el valor de "uno" 
    uno=suma  #"uno" toma el vlaor anterior
    suma=cero+uno #"cero" es el valor anterior y "uno" es el valor que se muestra, así "suma" se convierte en la suma de de esos dos y muestra el siguiente