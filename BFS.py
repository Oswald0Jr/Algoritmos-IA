# Define o grafo
grafo = {
    'Oradea': ['Zerind', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Sibiu': ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def busca_em_extensao(grafo, inicio, objetivo):
    # Inicializa a fila de busca
    fila = [inicio]

    # Inicializa o dicionário de pais
    pais = {inicio: None}

    # Enquanto houver nós a serem visitados
    while fila:
        # Retira o primeiro nó da fila
        atual = fila.pop(0)

        # Se encontramos o objetivo, retorna o caminho percorrido
        if atual == objetivo:
            caminho = []
            while atual != None:
                caminho.append(atual)
                atual = pais[atual]
            return caminho[::-1]

        # Para cada vizinho do nó atual
        for vizinho in grafo[atual]:
            # Se ainda não visitamos o vizinho
            if vizinho not in pais:
                # Adiciona o vizinho à fila
                fila.append(vizinho)

                # Define o pai do vizinho como sendo o nó atual
                pais[vizinho] = atual

    # Se chegamos aqui, não há caminho possível
    return None

# Pede ao usuário a cidade de origem e de destino
origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")

# Encontra o caminho entre as cidades
caminho = busca_em_extensao(grafo, origem, destino)

# Imprime o resultado
if busca_em_extensao(grafo, origem, destino) == False:
    print("Caminho não encontrado!")
else:
    print("Caminho: ", busca_em_extensao(grafo, origem, destino))
