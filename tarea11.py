import random  # <-- Importamos la librería para generar números aleatorios
numero = random.randint(1, 30) # Genera un número al azar entre 1 y 100 (ambos incluidos)
n_usuario = 0
intentos = 5
fin = False
while fin == False:
    n_usuario = int(input("Ingrese un número: "))

    if n_usuario < numero:
        intentos = intentos - 1
        print("\nEl número es mayor a", n_usuario)
        print("\nTe quedan solo", intentos, "intentos")
    elif n_usuario > numero:
        intentos = intentos - 1
        print("\nEl número es menor a", n_usuario)
        print("\nTe quedan solo", intentos, "intentos")
    else:
        fin = True
    
    if intentos == 0:
        fin = True

if intentos > 0:
    print("El número es", numero)
    print("\tGanaste.\n Con", intentos, "restantes")
else:
    print("\tSe acabo el juego.\n El número era", numero)