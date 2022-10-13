disc=int(0)
dos=int(0)
una=int(0)
sinreal=int(0)
porc=float(0.0)
total=int(0)
seguir=str("si")

while seguir.lower()=="si" or seguir.lower()=="s":
    disc=int(input("Ingrese un discriminante: "))
    
    if disc>0:
        dos=dos+1
    elif disc==0:
        una=una+1
    else:
        sinreal=sinreal+1
    
    total=total+1 #contador para calcular el porcentaje

    seguir=str(input("Desesa seguir ingresando valores? (si/no): "))


print(f"Total de discriminantes con dos raices: {dos}")
print(f"Total de discriminantes con una raíz: {una}")
print(f"Total de discriminantes sin solución real: {sinreal}")

porc=sinreal*100/total
print(f"{sinreal} suponen un {porc}% sobre el total de números ingresados.")