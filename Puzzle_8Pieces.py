from collections import deque

# Representação do estado do tabuleiro
class EstadoTabuleiro:
    def __init__(self, tabuleiro, movimentos=None):
        self.tabuleiro = tabuleiro
        self.movimentos = movimentos if movimentos is not None else []

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.tabuleiro)

    def copiar(self):
        novo_tabuleiro = [list(row) for row in self.tabuleiro]
        return EstadoTabuleiro(novo_tabuleiro, self.movimentos[:])

    def movimentar(self, direcao):
        lin, col = self.encontrar_posicao(0)
        novo_lin, novo_col = lin + direcao[0], col + direcao[1]
        if 0 <= novo_lin < 3 and 0 <= novo_col < 3:
            novo_tabuleiro = self.copiar().tabuleiro
            novo_tabuleiro[lin][col], novo_tabuleiro[novo_lin][novo_col] = novo_tabuleiro[novo_lin][novo_col], novo_tabuleiro[lin][col]
            return EstadoTabuleiro(novo_tabuleiro, self.movimentos + [self.tabuleiro[novo_lin][novo_col]])
        return None

    def encontrar_posicao(self, elemento):
        for lin in range(3):
            for col in range(3):
                if self.tabuleiro[lin][col] == elemento:
                    return lin, col

    def eh_estado_objetivo(self):
        return self.tabuleiro == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def obter_movimentos_possiveis(self):
        lin, col = self.encontrar_posicao(0)
        movimentos_possiveis = []
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for direcao in direcoes:
            novo_lin, novo_col = lin + direcao[0], col + direcao[1]
            if 0 <= novo_lin < 3 and 0 <= novo_col < 3:
                movimentos_possiveis.append(direcao)

        return movimentos_possiveis

# Algoritmo de busca em largura (BFS)
def bfs(estado_inicial):
    fila = deque([estado_inicial])
    visitados = set()

    while fila:
        estado_atual = fila.popleft()
        if estado_atual.eh_estado_objetivo():
            return estado_atual.movimentos
        visitados.add(str(estado_atual))

        for direcao in estado_atual.obter_movimentos_possiveis():
            novo_estado = estado_atual.movimentar(direcao)
            if novo_estado and str(novo_estado) not in visitados:
                fila.append(novo_estado)

# Teste com um tabuleiro inicial específico
tabuleiro_inicial = EstadoTabuleiro([[2, 3, 1], [5, 7, 8], [6, 0, 4]])
print("Tabuleiro Inicial:")
print(tabuleiro_inicial)

# Busca em largura
print("\nResolução com BFS:")
passos_bfs = bfs(tabuleiro_inicial)
print(f"Número de passos: {len(passos_bfs)}")
for idx, passo in enumerate(passos_bfs, start=1):
    print(f"Passo {idx}: Mova o número {passo}")

