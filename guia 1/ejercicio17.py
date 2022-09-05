#declaracion de variables
num1=int
num2=int
num3=int
suma=int
res=int

#asignacion de valores
num1=int(input("Introduzca el primer numero a sumar: "))
num2=int(input("Introduzca el segundo: "))
num3=int(input("Introduzca el tercero: "))

suma=num1+num2+num3

#se crea un condicional: si la suma supera el numero 10, se dividirá por 2, y si no, se elevará al cubo 
if suma>10:
    res=0
    res=suma//2
    print(suma,"/ 2 =",res)
else:
    res=0
    res=suma**3
    print(suma,"^ 3 =",res)