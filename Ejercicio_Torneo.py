equipos=list()
codigo_resultado=list()

equipos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
codigo_resultado=["P", "E", "G"]

def menu():
    opcion=int(0)
    print("""--------------Bienvenido--------------
Por favor. elija una opción:
1. introducir un 
2. aaaaa
3. Salir""")
    opcion=int(input("> "))
    while opcion!=3:
        if opcion==1: Introducir_()
        elif opcion==2: aaaaa()
        else: print("Esa no es una opción válida")