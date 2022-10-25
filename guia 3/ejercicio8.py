import random #importo random para determinar la posición del robot

tito_x=int(0)
tito_y=int(0)
movimiento=str("")

tito_x=random.randint(-300,300) #hago que el robot ("Tito") se posicione en una coordenada aleatoria en un cuadrado de 600x600
tito_y=random.randint(-300,300)

while movimiento.lower()!="e":
    print("-------------------------------------------------------")
    print(f"La posición actual de Tito es ({tito_x};{tito_y}). ") #muestro la posición actual en cada repeticion
    print("""\nElija uno de los movimientos para tito:
a) Girar al norte y avanzar 10 pasos
b) Girar al sur y avanzar 20 pasos
c) Girar al este y avanzar 10 pasos
d) Girar al oeste y avanzar 20 pasos
e) Salir del programa. """)  #agrego una opción "e" para salir del programa cuando quiera
    movimiento=input(" >")
    if movimiento.lower()=="a":  #sumo o resto pasos a la posición inicial, teniendo en cuenta hacia donde avanza
        tito_y=tito_y+10  #10 pasos al norte
    elif movimiento.lower()=="b":
        tito_y=tito_y-20  #20 pasos al sur
    elif movimiento.lower()=="c":
        tito_x=tito_x+10  #10 pasos al este
    elif movimiento.lower()=="d":
        tito_x=tito_x-20  #20 pasos al oeste
    elif movimiento.lower()!="e":
        print("Esa no es una opción válida.")

print("\nMuchas gracias.")