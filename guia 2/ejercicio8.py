#declaro las variables
cantv=int(0)
ventas=int(0)
total=int(0)
ventas100=int(0)
ventas400=int(0)
ventas50=int(0)

#creo un ciclo que se repitte hasta que se introduce cualquier numero menor que 1
cantv=int(input("Introduzca la cantidad de unidades vendidas: "))
while cantv>0:
    ventas=ventas+1 #cuento ventas totales 
    total=total+cantv #y sumo las unidades vendidas en cada ciclo
    if cantv>=100 and cantv<=300:  #creo condicionales para sumar a los contadores de las respectivas condiciones
        ventas100=ventas100+1
    elif cantv>=400 and cantv<=600:
        ventas400=ventas400+1
    elif cantv<50:
        ventas50=ventas50+1
    cantv=int(input("Introduzca una nueva cantidad de unidades vendidas: "))

print("\n-----------------------------------------------------------") #separador
#para evitar que se muestre un mensaje con total 0, creo un if
if ventas!=0:
    print(f"El total de ventas diferentes ingresadas es de: {ventas}")
    print(f"La cantidad total de unidades vendidas es de {total}")
    if ventas100!=0: #dentro el primer if, creo uno por cada condicion anterior para que se muestren solo aquellas cuyo contador sea 1 o mas
        print(f"La cantidad de ventas con unidades entre 100 y 300 son {ventas100}")
    if ventas400!=0:
        print(f"La cantidad de ventas con unidades entre 400 y 600 son {ventas400}")
    if ventas50!=0:
        print(f"La cantidad de ventas con unidades menores a 50 son {ventas50}")
else:
    print("No se realizaron ventas.")