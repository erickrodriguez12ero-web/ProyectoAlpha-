

print("Programa de figuras")

print(" ")

print("figura uno triangulo")
print("")

altura = int(input("Altura del triangulo: "))
caracter_expresado = input("ingresa un caracter: ")
print("")
for i in range(1, altura+1):
    for j in range(1,altura-i+1):
        print(" ", end="")

    for j in range(1, (i*2)):
        print(caracter_expresado, end="")
    print()

print(" ")
print("Triangulo escaleno")
print("")

altura = int(input("Altura del triangulo escaleno: "))
caracter_expresado = input ("introduce un * : ")
print("")
for i in range(1,altura+1):
    for j in range (1, altura-i+1):
        print ("", end="")

    for j in range(1, (i*1)):
        print (caracter_expresado, end="")
    print()    





print(" ")
print("Figura tres cuadrado")
print(" ")
def mostrar_cuadrado(tamano, simbolo):
    """
    Muestra un cuadrado de tamaño 'tamano' usando el 'simbolo' indicado.
    """
    # Validaciones
    if not isinstance(tamano, int) or tamano <= 0:
        raise ValueError("El tamaño debe ser un número entero positivo.")
    if not isinstance(simbolo, str) or len(simbolo) == 0:
        raise ValueError("El símbolo debe ser una cadena no vacía.")

    # Construir una línea del cuadrado
    linea = (simbolo + " ") * tamano

    # Imprimir el cuadrado
    for _ in range(tamano):
        print(linea.strip())  # strip() para quitar espacio extra al final


if __name__ == "__main__":
    try:
        # Solicitar datos al usuario
        tamano = int(input("Introduce el tamaño del cuadrado: "))
        simbolo = input("Introduce un * : ")

        mostrar_cuadrado(tamano, simbolo)

    except ValueError as e:
        print(f"Error: {e}")


