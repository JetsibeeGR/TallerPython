if __name__ == '__main__':
    entero = 42
    decimal = 3.14
    complejo = 2 + 3j
    booleano = True
    cadena = "Hola, python"
    binario = bytes([50, 100, 150])

    print("Tipos basicos")
    print("Entero: ", entero)
    print("Decimal:", decimal)
    print("complejo", complejo)
    print("booleano: ", booleano)
    print("cadena:", cadena)
    print("binario:", binario, "\n")

    #Estructura de datos avanzadas
    lista = [1, 2, 3, "cuatro"] # list
    tupla = (5, 6, 7, "ocho")# tuple

    conjunto = {9, 10, "once", "doce"}# set
    diccionario={"clave1": "valor1", "clave2": 20}  # d:

    print("Estructuras avanzadas:")
    print("Lista:", lista)
    print("Tupla:", tupla)
    print("Conjunto:", conjunto)
    print("Diccionario:", diccionario, "\n")

    nulo = None
    rango = range(3)

    print("Tipos especiales: ")
    print("Nulo:", nulo)
    print("Rango:", list(rango))

    print("\n Iterando sobre el rango:")
    for numero in rango:
        print(numero)