def busca_em_profundidade_limitada(grafo, inicio, objetivo, limite):
    if inicio == objetivo:
        return [inicio]  # Encontrou o objetivo

    if limite == 0:
        return []  # Limite de profundidade atingido

    if inicio not in grafo:
        return []  # Vértice não existe no grafo

    for vizinho in grafo[inicio]:
        caminho = busca_em_profundidade_limitada(grafo, vizinho, objetivo, limite - 1)
        if caminho:
            return [inicio] + caminho  # Encontrou caminho válido

    return []  # Caminho não encontrado


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

# Pede ao usuário a cidade de origem e de destino
origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")
limite_profundidade = int(input("Digite o limite de profundidade: "))

# Encontra o caminho entre as cidades com a busca em profundidade limitada
caminho = busca_em_profundidade_limitada(grafo, origem, destino, limite_profundidade)

# Imprime o resultado
if not caminho:
    print("Caminho não encontrado!")
else:
    print("Caminho:", caminho)
