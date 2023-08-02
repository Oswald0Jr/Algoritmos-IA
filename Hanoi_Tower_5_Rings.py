def hanoi(n, origem, destino, aux):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    hanoi(n-1, origem, aux, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    hanoi(n-1, aux, destino, origem)

def espaco_de_estados_torre_hanoi(n):
    print(f"Espaço de Estados para a Torre de Hanoi com {n} argolas:")
    hanoi(n, 'A', 'C', 'B')

# Teste com até 5 argolas
espaco_de_estados_torre_hanoi(1)
espaco_de_estados_torre_hanoi(2)
espaco_de_estados_torre_hanoi(3)
espaco_de_estados_torre_hanoi(4)
espaco_de_estados_torre_hanoi(5)
