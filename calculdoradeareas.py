def cuadrado_rectangulo():
    """Determinar el area de un cuadrado o rectangulo
    Imprime el area y el nombre de la figura
    """
    alto= abs(float(input("Por favor indique el alto de la figura en cm: ")))
    ancho= abs(float(input("Por favor indique el ancho de la figura en cm: "))) 
    area=round(alto*ancho,2)
    print(f"El Cuadrado o Rectángulo tiene un área de {area} ")

def circulo():
    """Determinar el area de un Circulo
    Imprime el area y el nombre de la figura
    """
    global PI
    radio = abs(float(input("Por favor indique el radio de la figura en cm: ")))
    area=round(PI*radio**2,2)
    print(f"El Circulo tiene un área de {area} ") 

def triangulo():
    """Determinar el area de un triangulo
    Imprime el area y el nombre de la figura
    """
    alto= abs(float(input("Por favor indique el alto de la figura en cm: ")))
    ancho= abs(float(input("Por favor indique el ancho de la figura en cm: ")))
    area=round(alto*ancho/2,2)
    print(f"El Triangulo tiene un área de {area} ")    

def romboide():
    """Determinar el area de un Romboide
    Imprime el area y el nombre de la figura
    """
    alto= abs(float(input("Por favor indique el alto de la figura en cm: ")))
    ancho= abs(float(input("Por favor indique el ancho de la figura en cm: ")))
    area=round(alto*ancho,2)
    print(f"El Romboide tiene un área de {area} ")    

def trapecio():
    """Determinar el area de un Trapecio
    Imprime el area y el nombre de la figura
    """
    base1= abs(float(input("Por favor indique el tamaño de la base inferior de la figura en cm: ")))
    base2= abs(float(input("Por favor indique el tamaño de la base superior de la figura en cm: ")))
    alto= abs(float(input("Por favor indique el alto de la figura en cm: ")))
    area=round((base1+base2)*alto/2,2)
    print(f"El Trapecio tiene un área de {area} ")     

def pentagono():
    """Determinar el area de un Pentágono Regular
    Imprime el area y el nombre de la figura
    """
    apotema= abs(float(input("Por favor indique el tamaño del apotema (Distancia de cualquiera de sus lados al centro) en cm: ")))
    lado= abs(float(input("Por favor indique la longitude de uno de sus lados en cm: ")))
    area=round(5*lado*apotema/2,2)
    print(f"El Pentágono Regular tiene un área de {area} ")

def hexagono():
    """Determinar el area de un Hexágono Regular
    Imprime el area y el nombre de la figura
    """
    apotema= abs(float(input("Por favor indique el tamaño del apotema (Distancia de cualquiera de sus lados al centro) en cm: ")))
    lado= abs(float(input("Por favor indique la longitud de uno de sus lados en cm: ")))
    area=round(6*lado*apotema/2,2)
    print(f"El Hexágono Regular tiene un área de {area} ")

def rombo():
    """Determinar el area de un Rombo
    Imprime el area y el nombre de la figura
    """
    diagonal_superior= abs(float(input("Por favor indique tamaño de la diagonal superior de la figura en cm: ")))
    diagonal_inferior= abs(float(input("Por favor indique tamaño de la diagonal inferior de la figura en cm: ")))
    area=round(diagonal_inferior*diagonal_superior/2,2)
    print(f"El Triangulo tiene un área de {area} ") 

def run():
    
    """Pedir Figura a procesar y envviar a la respectiva función
        """
    figura=input("""Por favor indicar que figura desea conocer el área
    \n\t1. Cuadrado o Rectángulo
    \t2. Circulo
    \t3. Triangulo
    \t4. Romboide
    \t5. Trapecio
    \t6. Pentágono Regular
    \t7. Hexágono Regular
    \t8. Rombo

    """)

    if figura == "1":
        cuadrado_rectangulo()
    elif figura == "2":
        circulo()
    elif figura == "3":
        triangulo()
    elif figura == "4":
        romboide()
    elif figura == "5":
        trapecio()
    elif figura == "6":
        pentagono()
    elif figura == "7":
        hexagono()
    elif figura == "8":
        rombo()
    else:
        print("Opción invalida por favor vuélvalo a intentar\n\n")
        run()


if __name__ == "__main__":
    PI=3.1416
    for j in range(100):
        if j == 0:
            run()
        continuar = input("""\n\n¿Desea calcular otra área?
        \n\n\t\t\t1. SI 
        \n\t\t\t2. NO
        """)
        if continuar == "1":
            run()
        elif continuar == "2":
            break
        else:
            print("Por favor ingrese una opcion valida")