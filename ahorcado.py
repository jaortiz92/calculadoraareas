def control_de_inputs(letra):
    """validar la letra ingresada po el jugador

    latra string de un solo carracter
    return La misma letra corregida
    """
    assert type(letra) == str, f'{letra} no es una letra'
    assert len(letra) == 1, "Solo debe ingresar una letra"
    return letra

def juegodeahorcado(palabra,nletras):
    """Validar las letras ingresadas y comparar

    palabra string cualquier palabra o frase
    nletras int numero de caracteres 
    return la dummy con la palabra correcta
    """
    dummy= "_"*nletras
    intentos=0
    while palabra!=dummy:
        letra= control_de_inputs(input("Introduzca una letra: ")).upper()
        if palabra.find(letra)>=0:
            print("La letra si se encuentra, muy bien!!!\n")
            contador = 0
            while contador <nletras:
                if palabra[contador]!=letra:
                    contador+=1
                    continue
                else:
                    if contador == 0:
                        dummy2=letra+dummy[contador+1:]
                    elif contador == nletras-1:
                        dummy2=dummy[:contador]+letra
                    else:
                        dummy2=dummy[:contador]+letra+dummy[contador+1:]
                    dummy=dummy2
                    contador+=1
        else:
            intentos+=1
            if intentos==4:
                print("\n\tTe quedan "+str(5-intentos)+" intento")
            else:
                print("\n\tTe quedan "+str(5-intentos)+" intentos")
            if intentos == 5:
                print("\n\tLo siento: Has perdido! :(\n\n\tLa palabra era: "+palabra+"\n\n")
                break
        print("\n\t\t"+dummy+"\n\n")   
    return dummy
            

def run():
    palabra=input("Escriba una palabra o frase, pero no permita que el otro jugador la vea: ")
    palabra = palabra.upper()
    for i in range(100):
        print("\n")
    nletras=len(palabra)
    print("La palabra tiene "+ str(nletras)+" Letras\n")

    dummy = juegodeahorcado(palabra,nletras)

    if palabra==dummy:
        print("\tFelicidades: Haz ganado!!! :)\n\n")   


if __name__ == "__main__":
    for j in range(100):
        run()
        continuar = input(""""¿Quieres volver a jugar?
        \n\n\t\t\t1. SI 
        \n\t\t\t2. NO
        """)
        if continuar == "1":
            run()
        elif continuar == "2":
            break
        else:
            print("Por favor ingrese una opcion valida")