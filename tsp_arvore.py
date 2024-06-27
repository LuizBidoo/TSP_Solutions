import sys
from math import inf
import time
import heapq
from collections import defaultdict

def ler_matriz_adjacencia(caminho_do_arquivo):
    matriz_adjacencia = []  # inicia matriz vazia
    with open(caminho_do_arquivo, "r") as file:  # abre arquivo para a leitura
        for linha in file:
            linha_convertida = list(map(int, linha.strip().split()))  # transforma cada linha em uma matriz de inteiros
            matriz_adjacencia.append(linha_convertida)
    return matriz_adjacencia

def mst_prim(matriz_adjacencia, inicio):
    mst = []  # Arvore geradora minima do grafo
    visitados = set()  # Conjunto de vertices visitados
    arestas_candidatas = []  # Heap queue para armazenar arestas candidatas

    def adiciona_arestas(vertice_atual):
        for vizinho, distancia in enumerate(matriz_adjacencia[vertice_atual]):
            if vizinho not in visitados and distancia > 0:
                heapq.heappush(arestas_candidatas, (distancia, vertice_atual, vizinho))

    visitados.add(inicio)
    adiciona_arestas(inicio)

    while arestas_candidatas:
        distancia, vertice_atual, vizinho = heapq.heappop(arestas_candidatas)
        if vizinho not in visitados:
            visitados.add(vizinho)
            mst.append((vertice_atual, vizinho, distancia))
            adiciona_arestas(vizinho)

    return mst

def arvore(mst): ## arvore de adjacencia para percorrer em pre-ordem
    tree = defaultdict(list)
    for vertice_atual, vizinho, distancia in mst:
        tree[vertice_atual].append(vizinho)
        tree[vizinho].append(vertice_atual)
    return tree

def viagem_pre_ordem(tree, vertice_atual, visitados, ordem):
    ordem.append(vertice_atual)
    visitados.add(vertice_atual)
    for vizinho in tree[vertice_atual]: ## recursão nos vizinhos
        if vizinho not in visitados:
            viagem_pre_ordem(tree, vizinho, visitados, ordem)

def calcular_custo_viagem(matriz_adjacencia, ordem):
    custo_total = 0
    for i in range(len(ordem) - 1):
        vertice_atual = ordem[i] 
        proximo_vertice = ordem[i + 1]
        custo_total += matriz_adjacencia[vertice_atual][proximo_vertice]
        # Fechando o ciclo
    custo_total += matriz_adjacencia[ordem[-1]][ordem[0]]
    return custo_total

def approx_tsp_tour(matriz_adjacencia, inicio):
    ordem = []
    visitados = set()
    mst = mst_prim(matriz_adjacencia, inicio)
    tree = arvore(mst)
    viagem_pre_ordem(tree, inicio, visitados, ordem)
    ordem.append(inicio)
    custo = calcular_custo_viagem(matriz_adjacencia, ordem)

    return ordem, custo
    
def main():
    if len(sys.argv) != 2:
        print("Número de argumentos incorreto. Utilize:")
        print("python tsp_nn.py <caminho_do_arquivo>")
        exit(1)

    caminho_do_arquivo = sys.argv[1]
    print(f"Lendo arquivo: {caminho_do_arquivo}")
    matriz_adjacencia = ler_matriz_adjacencia(caminho_do_arquivo)
    print("Matriz de Adjacência:")
    for linha in matriz_adjacencia:
        print(linha)
    while True:
        try:
            inicio = int(input("Escolha o vértice inicial para a aplicação do algoritmo TSP-Aprox: "))
            if inicio < 0 or inicio >= len(matriz_adjacencia):
                raise ValueError("Vértice arbitário inexistente")
            break
        except ValueError:
            print("Entrada inválida. Por favor, forneça um número inteiro válido.")
    ordem, custo = approx_tsp_tour(matriz_adjacencia, inicio)
    print(f"Ciclo Hamiltoniano: {ordem}")
    print(f"Custo total da viagem: {custo}")

if __name__ == "__main__":
    main()

