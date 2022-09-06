#variables
year=int
year2=int
year3=int
nuevo=int
viejo=int
renovar=int

#se limpian las variables dinamicas
viejo=0
nuevo=0
renovar=0

#Se piden por teclado los datos de los años
year=int(input("Introduzca el año de creación del primer cuadro: "))
if year<2000 and year>1901:
    viejo=viejo+1
    renovar=renovar+1
elif year>2000 and year<2012:
    renovar=renovar+1
elif year>2012:
    nuevo=nuevo+1

year2=int(input("Introduzca el año de creación del segundo cuadro: "))
if year2<2000 and year2>1901:
    viejo=viejo+1
    renovar=renovar+1
elif year2>2000 and year2<2012:
    renovar=renovar+1
elif year2>2012:
    nuevo=nuevo+1

year3=int(input("Introduzca el año de creación del tercer cuadro: "))
if year3<2000 and year3>1901:
    viejo=viejo+1
    renovar=renovar+1
elif year3>2000 and year3<2012:
    renovar=renovar+1
elif year3>2012:
    nuevo=nuevo+1

#se crea un condicional para mostrar por pantalla segun los valores conseguidos
if viejo!=0 and nuevo==0:
    print("Hay ",viejo," cuadros pertenecientes al siglo XX")
    print("No hay cuadros con antiguedad inferior a 10 años, renovar stock.")
elif viejo!=0 and nuevo!=0:
    print("Hay ",viejo," cuadros pertenecientes al siglo XX")
    print("Hay ",nuevo," cuadros con antiguedad inferior a 10 años.")
    print("Y hay",renovar," cuadros con antiguedad mayor a 10 años, renovar stock.")
elif viejo==0 and renovar!=0:
    print("No hay cuadros del siglo XX, son todos de este siglo")
    print("Hay",renovar," cuadros con antiguedad mayor a 10 años, renovar stock.")
else:
    print("Todos los cuadros tienen una antiguedad inferior a 10 años.")