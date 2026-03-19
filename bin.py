import sys

def exponenciacion_binaria(base, exponente, modulo):
    resultado = 1
    base = base % modulo

    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        
        exponente = exponente // 2
        base = (base * base) % modulo

    return resultado


def main():
    # Leer toda la entrada que manda el autograder
    datos = sys.stdin.read().split()

    base = int(datos[0])
    exponente = int(datos[1])
    modulo = int(datos[2])

    resultado = exponenciacion_binaria(base, exponente, modulo)

    # El autograder solo espera el número
    print(resultado)


if __name__ == "__main__":
    main()it