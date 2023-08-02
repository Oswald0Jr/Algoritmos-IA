from collections import deque

# Representação do estado da Torre de Hanói
class EstadoHanoi:
    def __init__(self, torres, movimentos=None):
        self.torres = torres
        self.movimentos = movimentos if movimentos is not None else []

    def __str__(self):
        return str(self.torres)

    def copiar(self):
        return EstadoHanoi([torre[:] for torre in self.torres], self.movimentos[:])

    def mover_disco(self, origem, destino):
        novo_estado = self.copiar()
        disco = novo_estado.torres[origem].pop()
        novo_estado.torres[destino].append(disco)
        novo_estado.movimentos.append((origem, destino))
        return novo_estado

    def eh_estado_objetivo(self):
        return len(self.torres[0]) == 0 and len(self.torres[1]) == 0

def obter_movimentos_possiveis(estado_atual):
    movimentos_possiveis = []
    for origem in range(3):
        if estado_atual.torres[origem]:
            for destino in range(3):
                if origem != destino and (not estado_atual.torres[destino] or estado_atual.torres[origem][-1] < estado_atual.torres[destino][-1]):
                    movimentos_possiveis.append((origem, destino))
    return movimentos_possiveis

def bfs(torres_iniciais):
    fila = deque([EstadoHanoi(torres_iniciais)])
    visitados = set([str(torres_iniciais)])

    while fila:
        estado_atual = fila.popleft()
        if estado_atual.eh_estado_objetivo():
            return estado_atual.movimentos
        movimentos_possiveis = obter_movimentos_possiveis(estado_atual)
        for movimento in movimentos_possiveis:
            novo_estado = estado_atual.mover_disco(movimento[0], movimento[1])
            if str(novo_estado.torres) not in visitados:
                visitados.add(str(novo_estado.torres))
                fila.append(novo_estado)

# Teste com a Torre de Hanói de 5 argolas
torres_iniciais = [[5, 4, 3, 2, 1], [], []]
print("Torres Iniciais:")
print(torres_iniciais)

passos_bfs = bfs(torres_iniciais)
print("\nPassos para resolver a Torre de Hanói:")
for idx, movimento in enumerate(passos_bfs, start=1):
    origem, destino = movimento
    print(f"Passo {idx}: Mova o disco da torre {origem + 1} para a torre {destino + 1}")
