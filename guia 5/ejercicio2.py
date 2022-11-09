def carga_numeros(n):
    total=int(0)
    lista=list()
    porcentaje=int(0)
    ultimo_digito=int(0)
    n_menor=int(0)
    menores_7=str("Si")

    while n!=0:
        total+=1
        if n%2==0: porcentaje+=1 # a) Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números ingresados.
        if n%10==4 or n%10==5: ultimo_digito+=1 # b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.
        if n%3==0:
            if total==1 or n<n_menor: n_menor=n # c) Determinar el menor de los números ingresados que sean divisibles por 3.
        
        lista.append(int(n))

        n=int(input("Introduzca otro numero: "))

    for num in lista: #Determinar si la secuencia estaba formada sólo por números menores de 7
        if num>7:
            menores_7="No"
    

    porcentaje= (porcentaje*100)/total #determino el procentaje 
    #muetro resultados por pantalla
    print(f"El porcentaje de numeros pares sobre los {total} numeros ingresados es de {round(porcentaje, 2)}%.")
    print(f"La cantidad de números ingresados que tenían su último dígito igual a 4 o igual a 5 es de {ultimo_digito}.")
    print(f"El menor numero divisible por 3 ingresado es {n_menor}")
    print(f"La secuencia estaba formada solo por numeros menores de 7? {menores_7}") 

carga_numeros(int(input("Introduzca un numero (si introduce 0, se cancela la carga de numeros): ")))