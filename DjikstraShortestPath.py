import heapq

# Define o grafo das cidades com os pesos das arestas
grafo = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def dijkstra(grafo, origem, fim):
    # Inicializa as distâncias para cada vértice com um valor "infinito"
    distancias = {vertice: float('inf') for vertice in grafo}

    # A distância do nó inicial é 0
    distancias[origem] = 0

    # Define a fila de prioridade com as distâncias iniciais
    fila = [(0, origem)]

    # Define um dicionário para armazenar os predecessores de cada nó no caminho mais curto
    predecessores = {}

    # Enquanto a fila não estiver vazia
    while fila:
        # Pega o nó com a menor distância da fila
        distancia_atual, no_atual = heapq.heappop(fila)

        # Se já encontrou o destino, retorna o caminho mais curto
        if no_atual == fim:
            caminho = []
            while no_atual != origem:
                caminho.insert(0, no_atual)
                no_atual = predecessores[no_atual]
            caminho.insert(0, origem)
            return caminho

        # Para cada vizinho do nó atual
        for vizinho, peso in grafo[no_atual].items():

            # Calcula a distância até o vizinho
            dist = distancias[no_atual] + peso

            # Se encontrou um caminho mais curto para o vizinho, atualiza as informações
            if dist < distancias[vizinho]:
                distancias[vizinho] = dist
                predecessores[vizinho] = no_atual
                heapq.heappush(fila, (dist, vizinho))

    # Se não encontrou um caminho, retorna False
    return False

# Imprime o resultado

origem = input("Digite a origem: ")
fim = input("Digite o destino: ")
print("Caminho mais curto: ",dijkstra(grafo, origem, fim))
