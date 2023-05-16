from collections import deque

# Representação do labirinto
labirinto = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 2, 0, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# Posição inicial do Pac-Man
pacman_pos = (0, 0)

# Posições das bolinhas maiores
bolinhas_pos = [(2, 1), (2, 5)]

# Movimentos possíveis (cima, baixo, esquerda, direita)
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(labirinto, origem, destino):
    fila = deque()
    visitados = set()

    fila.append((origem, []))
    visitados.add(origem)

    while fila:
        pos, caminho = fila.popleft()

        if pos == destino:
            return caminho

        for movimento in movimentos:
            nova_pos = (pos[0] + movimento[0], pos[1] + movimento[1])

            if (
                0 <= nova_pos[0] < len(labirinto)
                and 0 <= nova_pos[1] < len(labirinto[0])
                and labirinto[nova_pos[0]][nova_pos[1]] != 1
                and nova_pos not in visitados
            ):
                fila.append((nova_pos, caminho + [nova_pos]))
                visitados.add(nova_pos)

    return None


def calcular_distancias(labirinto, pacman_pos, bolinhas_pos):
    distancias = []
    
    for bolinha_pos in bolinhas_pos:
        distancia = bfs(labirinto, pacman_pos, bolinha_pos)
        distancias.append((bolinha_pos, len(distancia)))

    return sorted(distancias, key=lambda x: x[1])


def mover_pacman(labirinto, pacman_pos, destino):
    caminho = bfs(labirinto, pacman_pos, destino)

    if caminho:
        for pos in caminho:
            labirinto[pacman_pos[0]][pacman_pos[1]] = 0
            pacman_pos = pos
            labirinto[pacman_pos[0]][pacman_pos[1]] = 3
            imprimir_labirinto(labirinto)
    else:
        print("Destino inalcançável!")


def imprimir_labirinto(labirinto):
    for linha in labirinto:
        print(" ".join(str(celula) for celula in linha))
    print()


# Inicializar Pac-Man no labirinto
labirinto[pacman_pos[0]][pacman_pos[1]] = 3

# Calcular as distâncias das bolinhas maiores em relação ao Pac-Man
bolinhas_ordenadas = calcular_distancias(labirinto, pacman_pos, bolinhas_pos)

# Mover o Pac-Man para as bolinhas maiores
for bolinha in bolinhas_ordenadas:
    bolinha_pos, _ = bolinha
    mover_pacman(labirinto, pacman_pos, bolinha_pos)
