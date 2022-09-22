#declaro las variables
pob=int(0)
sexo=str("")
edad=int(0)
m=int(0)
m80=int(0)
f=int(0)
f18=int(0)

#pido por teclado la cantidad de datos a ingresar
pob=int(input("Introduzca la cantidad de habitantes (sin puntos ni comas): "))
print("\n********************************************************************")
#comienza el ciclo
for x in range(pob):
    sexo=str(input(f"Introduzca el sexo de la persona nº{x+1} (solo M/F): "))
    while (sexo.lower()!="m") and (sexo.lower()!="f"):
        sexo=str(input("Por favor, solo introducir una de las opciones solicitadas (M/F): ")) #ciclo para que solo se introduzcan valores correspondientes
    edad=int(input(f"Introduzca la edad de la persona nº{x+1}: "))
    #comienzan a sumarse los contadores dependiendo de si cumplen o no las condiciones
    if sexo.lower()=="m":
        m=m+1
        if edad>80:
            m80=m80+1
    if sexo.lower()=="f":
        f=f+1
        if edad>4 and edad<18:
            f18=f18+1
print("********************************************************************")
print("\n------------------------------------------------------------------------") #lineas 12, 28, 29: separadores
#primer condicional para la cantidad de habitantes
if m>f:
    print("La mayor cantidad de habitantes son hombres.")
elif f>m:
    print("La mayor cantidad de habitantes son mujeres.")
else:
    print("La cantidad de hombre y mujeres es la misma.")

if f18>0:
    print(f"Hay {f18} mujere/s que están en edad escolar.")
if m80>0:
    print(f"Hay {m80} hombre/s con edad mayor a 80 años.")
