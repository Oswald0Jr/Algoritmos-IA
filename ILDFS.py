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


def busca_em_profundidade_limitada_iterativa(grafo, inicio, objetivo, limite_maximo):
    for limite_profundidade in range(limite_maximo + 1):
        caminho = busca_em_profundidade_limitada(grafo, inicio, objetivo, limite_profundidade)
        if caminho:
            return caminho

    return []  # Caminho não encontrado para nenhum limite de profundidade


# Define o grafo (mantido o mesmo do exemplo anterior)
# ... (o grafo permanece o mesmo)

# Pede ao usuário a cidade de origem e de destino
origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")
limite_maximo = int(input("Digite o limite máximo de profundidade: "))

# Encontra o caminho entre as cidades com a busca em profundidade limitada iterativa
caminho = busca_em_profundidade_limitada_iterativa(grafo, origem, destino, limite_maximo)

# Imprime o resultado
if not caminho:
    print("Caminho não encontrado!")
else:
    print("Caminho:", caminho)
