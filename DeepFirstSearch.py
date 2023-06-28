def busca_em_profundidade(grafo, inicio, objetivo):
    # Inicializa a pilha de busca
    pilha = [inicio]

    # Inicializa o dicionário de pais
    pais = {inicio: None}

    # Enquanto houver nós a serem visitados
    while pilha:
        # Retira o último nó da pilha
        atual = pilha.pop()

