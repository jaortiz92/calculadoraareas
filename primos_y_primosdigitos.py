
def es_primo(n):
    """"Validar si es primo"""
    if n == 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    else:
        for i in range(3,round(n**(1/2)+1)):
            if n % i == 0:
                return False
    return True

def separar(n):
    """"Desagrupar numero par probar si es primo"""
    n = str(n)
    tamano = len(n)
    contador = 0
    for i in n:
        i=int(i)
        if es_primo(i):
            contador += 1
    return contador == tamano

def main(n):
    resultado  = []
    
    for i in range(n+1):
        if es_primo(i):
            resultado.append(i)
        elif separar(i):
            resultado.append(i)

    return resultado


if __name__ == "__main__":
    
    resultado = main(int(input()))
    print (resultado)
