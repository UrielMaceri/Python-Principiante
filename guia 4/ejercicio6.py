#declaro las listas y variables
meses=list()
cant_dias=list()
n=int(0)
#introduzco los datos en las listas
meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
cant_dias=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n=int(input("Introduzca el numero del mes: "))
#controlo que no se introduzcan numeros fuera del rango 1-12
while n<1 or n>12:
    print("Ese no es un numero valido.")
    n=int(input("Por favor, introduzca un numero entre 1 y 12: "))

#imprimo el me correspondiente a la lista, restandole 1 a n ya que las listas cuentan desde 0
print(f"El mes de {meses[n-1]} ({n}) tiene {cant_dias[n-1]} dias.")
