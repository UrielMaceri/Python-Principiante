vendedor=int(1)
opcion=str("si")
venta=int(0)
cat1=int(0)
cat2=int(0)
cat3=int(0)
cat4=int(0)
total=int(0)

while opcion.lower()=="si":
    vendedor=int(input("""Seleccione una de las categorías de vendedor
si se introduce 0, se cerrará el programa (1-4): """))
    if vendedor==1:
        venta=int(input("Introduzca el valor de la venta: $"))
        cat1=cat1+(venta+(venta*0.10))
        total=total+cat1
        opcion=str(input("Desea introducir mas datos? (si/no): "))
        while opcion.lower()!="si" and opcion.lower()!="no":
            print("Esa no es una opción válida.")
            opcion=str(input("Introduzca solo si o no: "))
    elif vendedor==2:
        venta=int(input("Introduzca el valor de la venta: $"))
        cat2=cat2+(venta+(venta*0.25))
        total=total+cat2
        opcion=str(input("Desea introducir mas datos? (si/no): "))
        while opcion.lower()!="si" and opcion.lower()!="no":
            print("Esa no es una opción válida.")
            opcion=str(input("Introduzca solo si o no: "))
    elif vendedor==3:
        venta=int(input("Introduzca el valor de la venta: $"))
        cat3=cat3+(venta+(venta*0.30))
        total=total+cat3
        opcion=str(input("Desea introducir mas datos? (si/no): "))
        while opcion.lower()!="si" and opcion.lower()!="no":
            print("Esa no es una opción válida.")
            opcion=str(input("Introduzca solo si o no: "))
    elif vendedor==4:
        venta=int(input("Introduzca el valor de la venta: $"))
        cat4=cat4+(venta+(venta*0.40))
        total=total+cat4
        opcion=str(input("Desea introducir mas datos? (si/no): "))
        while opcion.lower()!="si" and opcion.lower()!="no":
            print("Esa no es una opción válida.")
            opcion=str(input("Introduzca solo si o no: "))
    elif vendedor==0:
        print("El programa se cerrará.")
        opcion="no"
    else:
        print("Esa no es una opción válida, reingrese.")
    


print(f"La cantidad total de ventas de la categoría 1, es de ${cat1}")
print(f"La cantidad total de ventas de la categoría 2, es de ${cat2}")
print(f"La cantidad total de ventas de la categoría 3, es de ${cat3}")
print(f"La cantidad total de ventas de la categoría 4, es de ${cat4}")
print(f"La cantidad de ventas totales es ${total}")