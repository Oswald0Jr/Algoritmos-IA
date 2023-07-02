def busca_em_profundidade(grafo, inicio, objetivo):
    # Inicializa a pilha de busca
    pilha = [inicio]

    # Inicializa o dicionário de pais
    pais = {inicio: None}

    # Enquanto houver nós a serem visitados
    while pilha:
        # Retira o último nó da pilha
        atual = pilha.pop()

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
                # Adiciona o vizinho à pilha
                pilha.append(vizinho)

                # Define o pai do vizinho como sendo o nó atual
                pais[vizinho] = atual

    # Se chegamos aqui, não há caminho possível
    return None

# Pede ao usuário a cidade de origem e de destino
origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")

# Encontra o caminho entre as cidades
caminho = busca_em_profundidade(grafo, origem, destino)

# Imprime o resultado
if caminho is None:
    print("Caminho não encontrado!")
else:
    print("Caminho: ", caminho)
