if __name__ == '__main__':
    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa un numero: "))
    c = int(input("Ingresa un numero: "))

    if a>b:
        if a>c:
            print(f"El mayor es {a}")
        else:
            print(f"El mayor es {c}")
    elif b>c:
        print(f"El mayor es {b}")
    else:
        print(f"El mayor es {c}")