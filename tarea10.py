print("Se sacara un promedio de los números positivos.\n Ingrese números mayor a cero.\n Si presiona 0 se corta el programa.\n")
acum = 0
suma = 0
corte = True
promedio = 0
while corte != 0:
    valor1 = float(input("Ingrese un número: "))
    if valor1 > 0:
        acum = acum + 1
        suma = suma + valor1
        print(suma)
    elif valor1 < 0: 
        print("No cumple con lo especificado")
    else:
        corte = False 
promedio = (suma / acum)
print(promedio)
print("FIN")