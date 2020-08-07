def numero_incorrecto(n):
    n = abs(n)
    for i in range(n):
        print("Numero incorrecto!!!\n")
    main()

def proceso(n):
    segundo_n = n
    suma = 0

    for j in range(segundo_n):
        print(f'{str(n)*abs(n)}={n*n}')
        suma += (n*n)
        n -= 1
    
    n = 1
    for j in range(segundo_n):
        print(f'{str(n)*abs(n)}={n*n}')
        suma += (n*n)
        n += 1

    return suma


def main():
    numero_str = input("Introduce una nuemro entre 1 y 9: ")
    numero_int = int(numero_str)

    if numero_int > 9 or numero_int < 1:
        numero_incorrecto(numero_int)
    else:
        suma = proceso(numero_int)
        print(f'La suma de todos los resultados es {suma}')

    

if __name__ == "__main__":
    for j in range(100):
        if j == 0:
            main()
        continuar = input("""\n\n¿Desea calcular otra área?
        \n\n\t\t\t1. SI 
        \n\t\t\t2. NO
        """)
        if continuar == "1":
            main()
        elif continuar == "2":
            break
        else:
            print("Por favor ingrese una opcion valida")