#declaración de variables
num=int
ult1=int
ult2=int

#divido utilizando solo el resto (%) para dejar el ultimo digito como decimal
num=int(input("Ingrese un numero entero: "))
ult1=num%10
print("El ultimo digito es:", ult1)
ult2=num%100
print("Y los dos ultimos digitos son:",ult2) #esto funciona pero no devuelve resultados como "06" dado que los ceros a la izquierda no se toman en cuenta

#defino una funcion nueva para sacar los ultimos 2 digitos de "num" y transformarlos a una cadena str, como alternativa para mostrar numeros como "05" o "07"
def ults2(num):
    return(str(num)[-2:]) #se toma a num como un str y se extraen los ultimos 2 digitos con "[-2:]" que significa "a partir del final (:) hasta el caracter -2"
print("(utilizando def) Y los dos ultimos digitos son:",ults2(num))