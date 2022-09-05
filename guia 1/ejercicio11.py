#declaracion de variables
num=int
mult=int
res=int

#asignacion de valores
num=int(input("Introduzca un número: "))
mult=1

for x in range (10):
    res=0
    res=num*mult
    print(num,"*",mult,"=",res)
    mult=mult+1