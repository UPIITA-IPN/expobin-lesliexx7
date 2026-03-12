
def exponenciacion_binaria(M, e, n):
    
    # Convertimos el exponente a binario
    e_bin = bin(e)[2:]  
    
    # Inicialización
    if e_bin[0] == '1':
        C = M
    else:
        C = 1

    # Recorremos los bits restantes
    for bit in e_bin[1:]:
        
        # (a) C = C^2 mod n
        C = (C * C) % n
        
        # (b) si el bit es 1 multiplicamos por M
        if bit == '1':
            C = (C * M) % n

    return C


# Pedir datos al usuario
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
modulo = int(input("Ingrese el módulo: "))

# Calcular resultado
resultado = exponenciacion_binaria(base, exponente, modulo)

print("Resultado:", resultado)
