#declaracion de variables
a=int
b=int
bin=int
res=int

#asignacion de valores
a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))

#calculos de binomio y de resultado
bin=(a+b)**2
res=a**2+2*(a*b)+b**2

print("(",a,"+",b,")**2 =",a,"**2 + 2*(",a,"*",b,") + ",b,"**2")
print(bin, "=", res)