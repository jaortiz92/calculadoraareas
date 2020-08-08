import random
class Numero_Random:
    def __init__(self):
        self.tamano = 1000
        self.numero_aleatorio = random.randint(1,self.tamano)
        self.intentos=1


    def analisis(self,respuesta,objetivo):
        if objetivo != respuesta:
            if  objetivo > respuesta:
                return False, "Mayor"
            else:
                return False, "Menor"
        else:
            return True, None

def busqueda_lineal():
    algoritmo_lineal= Numero_Random()
    objetivo = algoritmo_lineal.numero_aleatorio
    tamano = algoritmo_lineal.tamano
    lista = [random.randint(1, tamano) for i in range(tamano)]
    intentos = 1
    for elemento in lista:
        estado, pista= algoritmo_lineal.analisis(elemento,objetivo)
        if estado:
            print(f'Encontrado {objetivo} {elemento}')
            break
        else:
            intentos += 1
    return intentos

def busqueda_lineal_senal():
    algoritmo_lineal= Numero_Random()
    objetivo = algoritmo_lineal.numero_aleatorio
    tamano = algoritmo_lineal.tamano
    elemento = random.randint(1, tamano)
    intentos = 1
    
    for i in range(tamano):
        estado, pista = algoritmo_lineal.analisis(elemento,objetivo)
        if estado:
            print(f'Encontrado {objetivo} {elemento}')
            break
        elif pista == "Mayor":
            elemento = random.randint(elemento, tamano)
        else:
            elemento = random.randint(1, elemento)
        intentos += 1

    return intentos


# def busqueda_binaria():
#     objetivo = 1000
#     epsilon = 0
#     bajo = 0
#     alto = max(1, objetivo)
#     respuesta = int((alto+bajo)/2)

def run():
    resultado_lineal = busqueda_lineal()
    resultado_linealsenal = busqueda_lineal_senal()
    return resultado_lineal, resultado_linealsenal


if __name__ == "__main__":
    resultadol=[]
    resultadols=[]
    for j in range(100):
        resultado_lineal, resultado_linealsenal =run()
        resultadol.append(resultado_lineal)
        resultadols.append(resultado_linealsenal)

    print("Resultado lineal ", sum(resultadol)/len(resultadol), max(resultadol), min(resultadol))
    print("Resultado lineal con señal ", sum(resultadols)/len(resultadols), max(resultadols), min(resultadols))